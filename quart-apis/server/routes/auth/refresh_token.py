
from quart import jsonify,make_response,Blueprint,request


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

from server.resources.apis_paths import AUTH_REFRESH_TOKEN_API_LINK

#declare blue print
refresh_token_bp = Blueprint('refresh',__name__,url_prefix=AUTH_REFRESH_TOKEN_API_LINK)

@refresh_token_bp.route('/', methods=['GET'])
@jwt_refresh_token_required  #Require a valid refresh token for this route
async def refresh():
    # Set the JWT access cookie in the response
    try:
        current_user = get_jwt_identity()
        print("referse attribute",current_user)
        access_token = create_access_token(identity=current_user,fresh=False)
        refresh_token = create_refresh_token(identity=current_user)
        respone = jsonify({'refresh': True,'access_token':access_token,'refresh_token':refresh_token,**current_user})
        print("the response",respone)
        set_access_cookies(respone, access_token)
        set_refresh_cookies(respone,refresh_token)
        return await make_response(respone, 200)
    except Exception as e:
        # print(e)
        return await make_response(jsonify({"status":"Login expired!","msg":"Login Again!"}),400)