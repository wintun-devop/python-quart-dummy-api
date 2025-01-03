from server import app_instance

#import blue print
from server.routes.default import servertest_bp
from server.routes.auth.register import register_bp
from server.routes.auth.login import login_bp
from server.routes.auth.refresh_token import refresh_token_bp
from server.routes.auth.logout import logout_bp
from server.routes.product.product import product_bp
from server.routes.product.products import products_bp



#create instance
app = app_instance()


#blueprint register here
app.register_blueprint(servertest_bp)
app.register_blueprint(register_bp)
app.register_blueprint(login_bp)
app.register_blueprint(refresh_token_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(product_bp)
app.register_blueprint(products_bp)

if __name__ == "__main__":
    app.run()
