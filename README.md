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