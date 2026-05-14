from flask import Flask, render_template
from extensions import db
import os

def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'inventory.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    with app.app_context():
        from models import Printer, Project, PrinterModel, Material, MaterialSpec, PrintJob
        db.create_all()
    @app.route('/')
    def home():
        return render_template('index.html')
    
    return app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
