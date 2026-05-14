# 3D Printing Management System

### Project Description
This application is a management tool for 3D printing labs. It allows users to track printing hardware (Printers) and manage the production queue (Projects). It is designed to streamline the workflow from project creation to live print tracking.

### Installation Instructions
1. Clone the repository to your local machine.
2. Create a virtual environment: `python -m venv venv`.
3. Activate the venv: `.\venv\Scripts\activate` (Windows).
4. Install dependencies: `pip install flask flask-sqlalchemy`.

### Database Setup
The application uses **SQLite** for easy portability. 
- The schema is automatically generated on the first run of the application via `db.create_all()`.
- Alternatively, you can review the structure in `models.py` or the provided `schema.sql`.

### Usage
1. Launch the server: `python app.py`.
2. Navigate to `http://127.0.0.1:5000` in your browser.
3. **Important:** Register at least one printer using the "Register Printer" form.
4. Add a project to the queue.
5. Click **"Start Print"** to trigger a SQL Transaction that links the project to a printer and updates its status.



## Part I 
### 1. Orginal Functional Dependencies
* **Printers**: printer_id -> model_name, serial_number, purchase_date, last_maintenance_date, firmware_version
* **Materials**: material_id -> material_type, color, weight_grams_start, weight_grams_current, received_date, expiration_date, storage_location
* **Projects**: project_id -> project_name, client_name, start_date, deadline_date, project_description, status
* **PrintJobs**: job_id -> project_id, printer_id, material_id, start_time, end_time, print_settings_profile

### 2. Anomaly Identification
* **Update Anomaly**: Changing a model's firmware requires updating every individual printer of that type, risking inconsistent data.
* **Insertion Anomaly**: New printer model specs cannot be added until a specific physical machine is purchased.
* **Deletion Anomaly**: Deleting a retired printer record accidentally erases all technical data for that model type.

### 3. Decomposition Steps
To reach 3rd Normal Form, I seprated attributes that depend on other non-key attributes:
1. Moved model_name  and firmware into a new PrinterModels table.
2. Moved material_type and color into a new MeterialSpecs table.

### 4. Final Relational Schema
* **PrinterModels**: (model_id [PK], model_name, firmware_version)
* **Printers**: (printer_id [PK], model_id[FK], serial_number, purchase_date, last_maintenance_date)
* **MaterialSpecs**: (spec_id [PK], material_type, color)
* **Materials**:(material_id [PK], spec_id [FK], weight_grams_start, weight_grams_current, received_date, expiration_date, storage_location)
* **Projects**: (project_id [PK], project_name, client_name, start_date, deadline_date, project_description, status)
* **PrintJobs**: (job_id [PK], project_id [FK], printer_id [FK], material_id [FK], start_time, end_time, print_settings_profile)