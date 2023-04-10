from flask import Flask,template_rendered

def initialization():
    web = Flask(__name__)
    web.config["SECRET_KEY"] = 'Sasikaran'
    web.run()