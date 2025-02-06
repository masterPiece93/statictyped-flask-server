from typing import Any, Final
from flask import Flask, g
import db
from modules.auth import auth_bp
from modules.commons import common_bp
from modules.api import api
import app_global_exception_handler
import app_custom_server_codes

DEBUG: Final[bool] = True

app = Flask(__name__)

@app.route('/')
def landing() -> Any:
    return "HOME"

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(common_bp, url_prefix="/commons")
app.register_blueprint(api, url_prefix="/api")

app_custom_server_codes.initialize(app)
app_global_exception_handler.register(app)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    
    db.inititalize(app)
    db.insert_seed_data(app)
    app.run(debug=DEBUG)
