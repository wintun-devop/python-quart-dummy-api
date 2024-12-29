from quart import jsonify,make_response,Blueprint,request
#import bcrypt
from server import bcrypt
#database import
from server.models.db import db_session
from server.models import User
from sqlalchemy.exc import SQLAlchemyError

#import api prefix
from server.resources.apis_paths import AUTH_REGISTER_API_LINK




#declare blue print
register_bp = Blueprint('register',__name__,url_prefix=AUTH_REGISTER_API_LINK)
@register_bp.route("/",methods=['POST'])
async def create_user():
     req_body = await request.get_json()
     try:
        user_name=req_body["username"]
        user_email=req_body["email"]
        user_password=req_body["password"]
        #hasing passsword
        hash_password = bcrypt.generate_password_hash(user_password).decode('utf-8')
        print("hash password",hash_password)
        add_user = User(email=user_email,password=hash_password,username=user_name)
        db_session.add(add_user)
        db_session.commit()
        result = db_session.query(User).filter_by(email=user_email).first()
        print("re",result)
        response = {
            'id':result.id,
            'username':user_name,
            'email':user_email,
            'profile':result.profile
        }
        return await make_response(jsonify(response),201)
     except SQLAlchemyError as e:
        print("err",e)
        print("type",type(e))
        error={"status":"fail","message":"internal server error"}
        return error

     