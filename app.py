from flask import Flask, render_template, request, redirect, url_for, flash
from extensions import db
from sqlalchemy import func
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = 'shocker_studios_secret' # Required for flashing messages
    
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'inventory.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    with app.app_context():
        from models import Project, Printer, PrintJob
        db.create_all()

    @app.route('/')
    def home():
        # Requirement: Summary Dashboard (Aggregate Functions)
        p_count = db.session.query(func.count(Project.project_id)).scalar()
        pr_count = db.session.query(func.count(Printer.printer_id)).scalar()
        
        # Requirement: Relationship Management (Read)
        projects = Project.query.all()
        return render_template('index.html', projects=projects, p_count=p_count, pr_count=pr_count)

    @app.route('/project/add', methods=['POST'])
    def add_project():
        name = request.form.get('project_name')
        # Requirement: Data Validation
        if not name or len(name.strip()) == 0:
            flash("Project name cannot be empty!")
            return redirect(url_for('home'))

        new_project = Project(project_name=name)
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('home'))

    @app.route('/project/delete/<int:id>', methods=['POST'])
    def delete_project(id):
        project = Project.query.get_or_404(id)
        db.session.delete(project)
        db.session.commit()
        return redirect(url_for('home'))

    @app.route('/project/start/<int:id>', methods=['POST'])
    def start_print(id):
        project = Project.query.get_or_404(id)
        # Requirement: Transaction Logic (Multi-step update)
        try:
            project.status = "Printing..."
            # Placeholder: In a full app, you'd select a printer ID here
            new_job = PrintJob(project_id=id) 
            db.session.add(new_job)
            db.session.commit()
        except:
            db.session.rollback()
            flash("Error processing print transaction.")
        return redirect(url_for('home'))

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)