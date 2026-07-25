"""
Mining Planning Software - Main Flask Application
"""
from flask import Flask, jsonify
from flask_restful import Api
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
api = Api(app)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'postgresql://user:password@localhost/mining_db'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False


# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'Mining Planning Software API',
        'version': '1.0.0'
    })


# API Routes will be registered here
# Example structure:
# from resources.mines import MineResource, MineListResource
# api.add_resource(MineListResource, '/api/mines')
# api.add_resource(MineResource, '/api/mines/<int:mine_id>')


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False') == 'True'
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=debug_mode
    )
