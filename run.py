from werkzeug.wrappers import Response
from werkzeug.wsgi import SharedDataMiddleware
from lib.app import App
from os import path

def run_sapp(config):
    app = App(config)
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app,{
        '/public':config['public_path'],
        '/uploads':config['upload_folder']
    
    })
   
    return app

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    config={
        'db' :{
            'host':'localhost',
            'user':'postgres',
            'password':'postgres',
            'dbname':'TraceARAP',

        },
        'upload_folder': path.join(path.dirname(__file__), 'uploads'),
        'public_path': path.join(path.dirname(__file__), 'public'),
        'template_path': path.join(path.dirname(__file__), 'views'),
    }

    app=run_sapp(config)
    run_simple('localhost', 4000, app, use_debugger=True, use_reloader=True, reloader_type='watchdog')
