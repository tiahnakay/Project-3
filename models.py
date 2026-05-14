from extensions import db
from datetime import datetime

class PrinterModel(db.Model):
    __tablename__ = 'printer_models'
    model_id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(100), nullable=False)
    firmware_version = db.Column(db.String(50))
    printers = db.relationship('Printer', backref='model', lazy=True)

class Printer(db.Model):
    __tablename__ = 'printers'
    printer_id = db.Column(db.Integer, primary_key=True)
    model_id = db.Column(db.Integer, db.ForeignKey('printer_models.model_id'))
    serial_number = db.Column(db.String(100), unique=True, nullable=False)
    last_maintenance_date = db.Column(db.Date)
    jobs = db.relationship('PrintJob', backref='printer', lazy=True)

class MaterialSpec(db.Model):
    __tablename__ = 'material_specs'
    spec_id = db.Column(db.Integer, primary_key=True)
    material_type = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(30), nullable=False)
    materials = db.relationship('Material', backref='specification', lazy=True)

class Material(db.Model):
    __tablename__ = 'materials'
    material_id = db.Column(db.Integer, primary_key=True)
    spec_id = db.Column(db.Integer, db.ForeignKey('material_specs.spec_id'))
    weight_grams_current = db.Column(db.Float)
    storage_location = db.Column(db.String(100))
    jobs = db.relationship('PrintJob', backref='material', lazy=True)

class Project(db.Model):
    __tablename__ = 'projects'
    project_id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), default='pending')
    jobs = db.relationship('PrintJob', backref='project', lazy=True)

class PrintJob(db.Model):
    __tablename__ = 'print_jobs'
    job_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'))
    printer_id = db.Column(db.Integer, db.ForeignKey('printers.printer_id'))
    material_id = db.Column(db.Integer, db.ForeignKey('materials.material_id'))
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)