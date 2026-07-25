"""
Database Models for Mining Planning Software
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()


class MineType(enum.Enum):
    COAL = "coal"
    METAL = "metal"
    MINERAL = "mineral"


class ResourceClassification(enum.Enum):
    MEASURED = "measured"
    INDICATED = "indicated"
    INFERRED = "inferred"


class Mine(Base):
    """Represents a mining site/operation"""
    __tablename__ = 'mines'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    mine_type = Column(Enum(MineType), nullable=False)
    location = Column(String(255), nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    status = Column(String(50), default='active')  # active, inactive, planning
    established_date = Column(DateTime, default=datetime.utcnow)
    total_area_hectares = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Resource(Base):
    """Represents geological resources (coal seams, ore bodies, mineral deposits)"""
    __tablename__ = 'resources'
    
    id = Column(Integer, primary_key=True)
    mine_id = Column(Integer, ForeignKey('mines.id'), nullable=False)
    name = Column(String(255), nullable=False)
    resource_type = Column(String(100), nullable=False)  # coal, iron_ore, copper, etc.
    classification = Column(Enum(ResourceClassification), nullable=False)
    quantity_tonnes = Column(Float, nullable=False)
    grade_percentage = Column(Float)  # For metals/minerals
    depth_meters = Column(Float)
    area_hectares = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Equipment(Base):
    """Represents mining equipment"""
    __tablename__ = 'equipment'
    
    id = Column(Integer, primary_key=True)
    mine_id = Column(Integer, ForeignKey('mines.id'), nullable=False)
    name = Column(String(255), nullable=False)
    equipment_type = Column(String(100), nullable=False)  # excavator, loader, truck, drill
    capacity = Column(Float)  # tonnes or units
    status = Column(String(50), default='operational')  # operational, maintenance, idle
    purchase_date = Column(DateTime)
    operating_hours = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Production(Base):
    """Records daily/monthly production data"""
    __tablename__ = 'production'
    
    id = Column(Integer, primary_key=True)
    mine_id = Column(Integer, ForeignKey('mines.id'), nullable=False)
    resource_id = Column(Integer, ForeignKey('resources.id'))
    production_date = Column(DateTime, nullable=False)
    quantity_tonnes = Column(Float, nullable=False)
    grade_percentage = Column(Float)
    equipment_used = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)


class Workforce(Base):
    """Employee and contractor records"""
    __tablename__ = 'workforce'
    
    id = Column(Integer, primary_key=True)
    mine_id = Column(Integer, ForeignKey('mines.id'), nullable=False)
    employee_id = Column(String(50), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    role = Column(String(100), nullable=False)  # operator, supervisor, engineer, etc.
    department = Column(String(100))
    is_contractor = Column(Boolean, default=False)
    hire_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String(50), default='active')  # active, on_leave, terminated
    created_at = Column(DateTime, default=datetime.utcnow)


class FinancialRecord(Base):
    """Financial planning and tracking"""
    __tablename__ = 'financial_records'
    
    id = Column(Integer, primary_key=True)
    mine_id = Column(Integer, ForeignKey('mines.id'), nullable=False)
    record_type = Column(String(50), nullable=False)  # cost, revenue, budget
    category = Column(String(100), nullable=False)  # equipment, labor, energy, etc.
    amount = Column(Float, nullable=False)
    currency = Column(String(10), default='USD')
    record_date = Column(DateTime, nullable=False)
    description = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)


class SafetyIncident(Base):
    """Safety and incident tracking"""
    __tablename__ = 'safety_incidents'
    
    id = Column(Integer, primary_key=True)
    mine_id = Column(Integer, ForeignKey('mines.id'), nullable=False)
    incident_date = Column(DateTime, nullable=False)
    incident_type = Column(String(100), nullable=False)  # injury, near_miss, equipment_damage
    severity = Column(String(50))  # low, medium, high, critical
    description = Column(String(1000))
    employees_involved = Column(Integer, default=0)
    status = Column(String(50), default='open')  # open, investigating, closed
    created_at = Column(DateTime, default=datetime.utcnow)
