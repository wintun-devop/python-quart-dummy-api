
from quart import jsonify,make_response,Blueprint,request

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


from server.resources.apis_paths import AUTH_LOGOUT_API_LINK

#declare blue print
logout_bp = Blueprint('logout',__name__,url_prefix=AUTH_LOGOUT_API_LINK)
@logout_bp.route('/', methods=['DELETE'])
def logout():
    respone = jsonify({"authenticated":False})
    unset_jwt_cookies(respone)
    return respone, 200