from flask import Flask, jsonify, request, Response, Blueprint
from flask_cors import CORS

User_bp = Blueprint('User', __name__)

# enable CORS
CORS(User_bp)

# query 範例:
# http://127.0.0.1:5001/User?type=sign-in
# http://127.0.0.1:5001/User?type=sign-up
@User_bp.route('/User', methods=['POST'])
def User_operation():
    if request.method == 'POST':
        type = request.args.get('type')
        # 登入功能，回傳 User 資訊
        if (type == "sign-in"):
            # post_data format
            # {
            #   'User_Mail': "",
            # 	'User_Password': "",
            # }

            post_data = request.get_json()
            Mail = post_data['User_Mail']
            Password = post_data['User_Password']

            # 成功路徑
            # if mail in DB
            if (True):
                # if passward is correct
                if (True):
                    # return User information
                    return_data = {
                        "User_ID": "123",
                        "User_Name": "jordan",
                        "User_Mail": "jordan@gmail.com",
                        "User_Avatar": "https://randomuser.me/api/portraits/men/1.jpg"
                    }

                    response_object = {
                        'status': 'success',
                        'response': '登入成功',
                        'method': 'POST',
                        'route': '/user?type=sign-in'
                    }
                    response_object["return_data"] = return_data
                    return jsonify(response_object)
            # 失敗路徑
            else:
                return Response(
                    response = "登入失敗",
                    status = 400,
                )
        
        # 註冊功能，註冊完只需要回傳成功訊息
        elif (type == "sign-up"):
            # post_data format
            # {
            #     'User_ID': "",
            #     'User_Name': "",
            #     'User_Mail': "",
            #     'User_Avatar': "",
            #     'User_Password': ""
            # }
            post_data = request.get_json()

            # 成功路徑
            # if User_ID Not in DB
            if(True):
                # if User_Mail Not in DB, save post_data as new User in DB, and return to frontend
                if(True):                
                    response_object = {
                        'status': 'success',
                        'response': '註冊成功',
                        'method': 'POST',
                        'route': '/user?type=sign-up'
                    }
                    return jsonify(response_object)
            # 失敗路徑
            else:
                return Response(
                    response = "註冊失敗",
                    status = 400,
                )

