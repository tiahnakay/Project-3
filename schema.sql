-- 1. Printer metadata
CREATE TABLE PrinterModels(
    model_id INTEGER PRIMARY KEY AUTOINCREMENT,
    modle_name TEXT NOT NULL,
    firmware_version TEXT
);

-- 2. Physical Inventory
CREATE TABLE Printers(
    printer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_id INTEGER NOT NULL,
    serial_number TEXT UNIQUE NOT NULL,
    purhcase_date DATE,
    last_maintenance_date DATE,
    FOREIGN KEY (model_id) REFERENCES PrinterModels(model_id)
);

-- 3. Material Specifications
CREATE TABLE MaterialSpecs(
    spec_id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_type TEXT NOT NULL,
    color TEXT NOT NULL,
);

-- 4. Material Inventory
CREATE TABLE Materials(
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    spec_id INTEGER,
    weight_grams_current REAL,
    storage_location TEXT,
    FOREIGN KEY (spec_id) REFERENCES MaterialSpecs(spec_id)
);

-- 5. Project Tracking
CREATE TABLE Projects(
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT NOT NULL,
    client_name TEXT,
    start_date DATE,
    deadline_date DATE,
    status TEXT DEFAULT 'Pending'
);

-- 6. Print Jobs
CREATE TABLE PrintJobs(
    job_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER,
    printer_id INTEGER,
    material_id INTEGER,
    start_time DATETIME,
    end_time DATETIME,
    settings_profile TEXT,
    FOREIGN KEY (project_id) REFERENCES Projects(project_id),
    FOREIGN KEY (printer_id) REFERENCES Printers(printer_id),
    FOREIGN KEY (material_id) REFERENCES Materials(material_id)
);