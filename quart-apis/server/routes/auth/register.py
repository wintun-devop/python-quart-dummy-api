from quart import jsonify,make_response,Blueprint,request
#import bcrypt
from server import bcrypt

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
        response = {
            'id':"1",
            'username':user_name,
            'email':user_email
        }
        return await make_response(jsonify(response),201)
     except:
        error={"status":"fail","message":"internal server error"}
        raise error

     