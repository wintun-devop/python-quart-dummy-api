from quart import jsonify,make_response,Blueprint,request
#import bcrypt
from server import bcrypt
#
from server.models.db import db_session
from server.models import User
from sqlalchemy.exc import SQLAlchemyError,IntegrityError

#import bcrypt
from server import bcrypt

#jwt function import
from quart_jwt_extended import (
                                jwt_required,
                                set_access_cookies,
                                set_refresh_cookies,
                                create_access_token,
                                create_refresh_token,
                                unset_jwt_cookies,
                                jwt_refresh_token_required,
                                get_jwt_identity
                                )

#import api prefix
from server.resources.apis_paths import AUTH_LOGIN_API_LINK

#declare blue print
login_bp = Blueprint('login',__name__,url_prefix=AUTH_LOGIN_API_LINK)
@login_bp.route("/",methods=['POST'])
async def login():
    req_body = await request.get_json()
    print("r",req_body)
    try:
        user_name=req_body["username"]
        user_password=req_body["password"]
        #check user as email
        check_email_result = db_session.query(User).filter_by(email=user_name).first()
        if check_email_result is not None:
            hash_password = check_email_result.password
            isPasswordCorrect =await bcrypt.async_check_password_hash(hash_password,user_password)
            """ if password is correct  """
            if isPasswordCorrect:
                # create the jwt and go make response
                token_attributes={"id":check_email_result.id,"username":check_email_result.username,"email":check_email_result.email}
                access_token = create_access_token(identity=token_attributes,fresh=True)
                refresh_token = create_refresh_token(identity=token_attributes)
                response=jsonify({**token_attributes,"access_token": access_token,"refresh_token": refresh_token,"authenticated":True})
                set_access_cookies(response,access_token)
                set_refresh_cookies(response,refresh_token)
                return await make_response(response,200)
            else:
                return await make_response(jsonify({'status':'fail','msg':'email or password incorrect.'}),401)
        #check user as username
        check_username_result = db_session.query(User).filter_by(username=user_name).first()
        if check_username_result is not None:
            hash_password = check_username_result.password
            isPasswordCorrect =await bcrypt.async_check_password_hash(hash_password,user_password)
            # create the jwt and go make response
            """ if password is correct  """
            if isPasswordCorrect:
                # create the jwt and go make response
                token_attributes={"id":check_username_result.id,"username":check_username_result.username,"email":check_username_result.email}
                access_token = create_access_token(identity=token_attributes,fresh=True)
                refresh_token = create_refresh_token(identity=token_attributes)
                response=jsonify({**token_attributes,"access_token": access_token,"refresh_token": refresh_token,"authenticated":True})
                set_access_cookies(response,access_token)
                set_refresh_cookies(response,refresh_token)
                return await make_response(response,200)
            else:
                return await make_response(jsonify({'status':'fail','msg':'email or password incorrect.'}),401)
        # default case
        return  await make_response(jsonify({'status':'fail','msg':'email or password incorrect.'}),401)
    except Exception as e:
        # print(e)
        error1={"status":"fail","message":"internal server error"}
        return await make_response(jsonify(error1),500)
