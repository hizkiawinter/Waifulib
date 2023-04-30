from flask import Flask, jsonify
from config import Config
from database import db,ma 
from Waifulib.Blueprints.routes import api 
from Waifulib.Blueprints.errors import err

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
ma.init_app(app)
with app.app_context():
    db.create_all()
    app.register_blueprint(api, url_prefix='/')
    app.register_blueprint(err)

if __name__ == '__main__':
    app.run(debug=True) 



