from quart import jsonify,make_response,Blueprint,request
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
        # create the jwt and go make response
        token_attributes={"id":"1","username":user_name}
        access_token = create_access_token(identity=token_attributes,fresh=True)
        refresh_token = create_refresh_token(identity=token_attributes)
        response=jsonify({**token_attributes,"access_token": access_token,"refresh_token": refresh_token,"authenticated":True})
        set_access_cookies(response,access_token)
        set_refresh_cookies(response,refresh_token)
        return await make_response(response,200)
    except:
        # print(e)
        error1={"status":"fail","message":"internal server error"}
        return await make_response(jsonify(error1),500)
