from quart import jsonify,make_response,Blueprint,request

#database import
from server.models.db import db_session
from server.models import Product
from sqlalchemy.exc import SQLAlchemyError,IntegrityError

from server.resources.apis_paths import PRODUCT_API
#input helper
from server.utils.helpers import to_lower_case,to_dict

#authorization
from quart_jwt_extended import (
                                jwt_required,
                                get_jwt_identity
                                )

#declare blue print
product_bp = Blueprint('product',__name__,url_prefix=PRODUCT_API)
@product_bp.route("/",methods=['POST'])
@jwt_required
async def create_product():
    req_body = await request.get_json()
    try:
        add_product = Product(name=req_body["name"],model_no=to_lower_case(req_body["model"]),price=req_body["price"],qty=req_body["qty"],description=req_body["description"])
        db_session.add(add_product)
        db_session.commit()
        result = db_session.query(Product).filter_by(model_no=to_lower_case(req_body["model"])).first()
        response = to_dict(result)
        return await make_response(jsonify(response),201)
    except IntegrityError as e:
        print("e",e)
        db_session.rollback()
        error = {"status": "fail", "message": "Product already exist."}
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


@product_bp.route("/",methods=['GET'])
@jwt_required
async def get_product():
    id = request.args.get('id')
    try:
        product = db_session.query(Product).filter_by(id=id).first()
        if product is None:
            return await make_response(jsonify({"status": "fail", "message": "Not Found"}), 404)
        result = to_dict(product)
        return await make_response(jsonify(result),200)
    except SQLAlchemyError as e:
        print("ee",e)
        error={"status":"fail","message":"internal server error"}
        return await make_response(jsonify(error), 500)
    except Exception as e:
        print("eee",e)        
        error = {"status": "fail", "message": "An unexpected error occurred"}
        return await make_response(jsonify(error), 500)


@product_bp.route("/",methods=['PUT'])
@jwt_required
async def update_product():
    req_body = await request.get_json()
    try:
        product = db_session.query(Product).filter_by(id=req_body["id"]).first()
        if product is None:
            return await make_response(jsonify({"status": "fail", "message": "Not Found"}), 404)
        # python ternary conditional expression
        product.name =product.name if req_body["name"] is None else req_body["name"]
        product.model_no = product.model_no if req_body["model"] is None else req_body["model"]
        product.price = product.price if req_body["price"] is None else req_body["price"]
        product.qty =product.qty if req_body["qty"] is None else req_body["qty"]
        product.country_origin = product.country_origin if req_body["country_origin"] is None else req_body["country_origin"]
        product.description = product.description if req_body["description"] is None else req_body["description"]
        db_session.commit()
        result = {
                "name":req_body["name"],
                "model":req_body["model"],
                "price":req_body["price"],
                "qty":req_body["qty"],
                "country_origin":req_body["country_origin"],
                "description":req_body["description"]
        }
        return await make_response(jsonify(result), 200)
    except IntegrityError as e:
        print("e",e)
        db_session.rollback()
        error = {"status": "fail", "message": "Product model already exist."}
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


@product_bp.route("/",methods=['DELETE'])
@jwt_required
async def delete_product():
    req_body = await request.get_json()
    try:
        product = db_session.query(Product).filter_by(id=req_body["id"]).first()
        if product is None:
            return await make_response(jsonify({"status": "fail", "message": "Not Found"}), 404)
        db_session.delete(product) 
        db_session.commit()
        return await make_response(jsonify({"status":"success","message": "Deleted"}), 200)
    except IntegrityError as e:
        print("e",e)
        db_session.rollback()
        error = {"status": "fail", "message": "Product model already exist."}
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
    