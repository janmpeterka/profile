from .controllers.integrations import integrations_blueprint


def create_module(app, **kwargs):
    app.register_blueprint(integrations_blueprint)
