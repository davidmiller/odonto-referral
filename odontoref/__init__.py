"""
odontoref - Our OPAL Application
"""
from opal.core import application

class Application(application.OpalApplication):
    flow_module   = 'odontoref.flow'
    javascripts   = [
        'js/odontoref/routes.js',
        'js/opal/controllers/discharge.js',
        # Uncomment this if you want to implement custom dynamic flows.
        # 'js/odontoref/flow.js',
    ]
    styles = [
        "css/odonto.css"
    ]
