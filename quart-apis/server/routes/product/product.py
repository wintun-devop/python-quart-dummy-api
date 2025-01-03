from quart import jsonify,make_response,Blueprint,request

#database import
from server.models.db import db_session
from server.models import Product
from sqlalchemy.exc import SQLAlchemyError,IntegrityError

from server.resources.apis_paths import PRODUCT_API

#declare blue print
product_bp = Blueprint('product',__name__,url_prefix=PRODUCT_API)
@product_bp.route("/",methods=['POST'])
async def create_product():
    req_body = await request.get_json()
    try:
        add_product = Product(name=req_body["name"],model_no=req_body["model"],price=req_body["price"],qty=req_body["qty"],description=req_body["description"])
        db_session.add(add_product)
        db_session.commit()
        result = db_session.query(Product).filter_by(model_no=req_body["model"]).first()
        print("product",result)
        response = {
            'id':result.id,
            'created':result.created
        }
        return await make_response(jsonify(response),201)
    except IntegrityError as e:
        print("e",e)
        db_session.rollback()
        error = {"status": "fail", "message": "A user with this email or usernname already exists"}
        return await make_response(jsonify(error), 400) 
    except SQLAlchemyError as e:
        print("ee",e)
        db_session.rollback()
        error={"status":"fail","message":"internal server error"}
        return await make_response(jsonify(error), 500)
    except Exception as e:
        print("eee",e)
        db_session.rollback()
        error = {"status": "fail", "message": "An unexpected error occurred"}
        return await make_response(jsonify(error), 500)

