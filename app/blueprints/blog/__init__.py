from app.blueprints.blog.controllers.main import blog_blueprint


def create_module(app, **kwargs):
    app.register_blueprint(blog_blueprint)
