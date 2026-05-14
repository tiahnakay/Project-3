# AI LOG
### AI Tool:
Gemini

### Prompts & Responses
Errors that popped up in the terminal are what I submitted into the AI tool to understand what the error is and how to fix it. 

The Prompt: Error Message - "(venv) ... RuntimeError: The current Flask app is not registered with this 'SQLAlchemy' instance. Did you forget to call 'init_app'..."

AI Output: Explained the FLask-SQLAlchemy registration requirement and provided an updated app.py using app.app_context().

My Modification:
Integrated with app.app_context(): block and moved the db.create_all() call inside it to ensure the database initializes correctly.

The Prompt: Error Message - "(venv) ... RuntimeError: The current Flask app is not registered with this 'SQLAlchemy' instance. (Repeat Error)"

AI Output: Identified a circular import between app.py and models.py. Suggested the "Factory Pattern" by creating extensions.py

My Modification: Created extensions.py to hold the db instance, allowing both app.py and models.py to import without looping.

The Prompt: "jinja2.exceptions.TemplateNotFound: index.html"

AI Output: Explained that flask requires a specific folder named templates to locate html files.

My Modification: Created the templates directory ad moved the index.html into it to resolve the pathing error.