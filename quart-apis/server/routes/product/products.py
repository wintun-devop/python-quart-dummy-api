from quart import jsonify,make_response,Blueprint,request

#database import
from server.models.db import db_session
from server.models import Product
from sqlalchemy.exc import SQLAlchemyError,IntegrityError
from server.resources.apis_paths import PRODUCTS_API
from server.utils.helpers import to_dict


#declare blue print
products_bp = Blueprint('products',__name__,url_prefix=PRODUCTS_API)
@products_bp.route("/",methods=['GET'])
async def get_products():
    try:
        result = db_session.query(Product).all()
        products = [to_dict(product) for product in result]
        return await make_response(jsonify(products),200)
    except SQLAlchemyError as e:
        print("ee",e)
        error={"status":"fail","message":"internal server error"}
        return await make_response(jsonify(error), 500)
    except Exception as e:
        print("eee",e)
        error = {"status": "fail", "message": "An unexpected error occurred"}
        return await make_response(jsonify(error), 500)

    

