from flask import Flask,render_template
#from jobplus.models import db
from jobplus.config import configs

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    #db.init_app(app)

    @app.route('/')
    def index():
        return 'hello jobplus11'
       # return render_template('index.html')
    
    return app
