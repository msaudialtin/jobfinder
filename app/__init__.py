# """Entry point to the Flask application"""
# from flask import Flask, redirect
# from flask_jwt_extended import JWTManager
# from .config import Config
# from .routes.auth_routes import auth_routes
# from .routes.user_routes import user_routes
# from .routes.job_routes import job_routes
# from .middlewares import setup_middlewares


# def create_app(config_class=Config):
#     """Create the Flask app instance"""
#     app = Flask(__name__)
#     app.config["JWT_SECRET_KEY"] = config_class.SECRET_KEY
#     JWTManager(app)
#     setup_middlewares(app)

#     # Define routes
#     @app.route("/")
#     def index():
#         return redirect("/login")

#     # Registering blueprints from your routes modules
#     app.register_blueprint(auth_routes)
#     app.register_blueprint(user_routes, url_prefix="/user")
#     app.register_blueprint(job_routes, url_prefix="/job")
#     return app
