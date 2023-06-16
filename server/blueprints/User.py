from flask import Flask, jsonify, request, Response, Blueprint
from flask_cors import CORS

import sqlite3

User_bp = Blueprint('User', __name__)

# enable CORS
CORS(User_bp)

# query 範例:
# http://127.0.0.1:5001/User?type=sign-in
# http://127.0.0.1:5001/User?type=sign-up
@User_bp.route('/User', methods=['POST'])
def User():
    type = request.args.get('type')
    
    if request.method == 'POST':
        # 登入功能，回傳 User 資訊
        if (type == "sign-in"):
            # 取得前端 request
            post_data = request.get_json()

            User_Mail = post_data.get('User_Mail')
            User_Password = post_data.get('User_Password')
            User_Mail.replace(" ", "")
            User_Password.replace(" ", "")

            con = sqlite3.connect("./sql/ProjectMgmt.db")
            cur = con.cursor()
            
            ret = cur.execute(""" SELECT * FROM user WHERE User_Mail=? AND User_Password=? """, (User_Mail, User_Password))
            db_result = ret.fetchall()

            user_info = {}
            if (len(db_result) != 0):
                user_info = db_result[0]

            con.close()

            # 成功路徑
            if (user_info):
                return_data = {
                    "User_ID": user_info[0],
                    "User_Name": user_info[1],
                    "User_Mail": user_info[2],
                    "User_Avatar": user_info[3]
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
            # get frontend request
            post_data = request.get_json()
            print(post_data)

            User_ID = post_data.get("User_ID")
            User_Name = post_data.get("User_Name")
            User_Mail = post_data.get("User_Mail")
            User_Avatar = post_data.get("User_Avatar")
            User_Password = post_data.get("User_Password")
            
            User_Name.replace(" ", "")
            User_Mail.replace(" ", "")
            User_Avatar.replace(" ", "")
            User_Password.replace(" ", "")

            # Default return false
            signUp_success = False

            if(User_ID and User_Name and User_Mail and User_Avatar and User_Password):
                con = sqlite3.connect("./sql/ProjectMgmt.db")
                cur = con.cursor()
                
                # 記得要用 (User_Mail, )，加上逗號以後才會是 tuple 
                ret = cur.execute(""" SELECT * FROM user WHERE User_Mail=?""", (User_Mail, ))
                db_result = ret.fetchall()

                if (len(db_result) != 0):
                    print("資料庫已經有這個 Email")

                else:
                    cur.execute("""
                        INSERT INTO user VALUES (?, ?, ?, ?, ?)
                    """, (User_ID, User_Name, User_Mail, User_Avatar, User_Password))

                    con.commit()

                    ret = cur.execute(""" SELECT * FROM user WHERE User_Mail=? """, (User_Mail, ))
                    db_result = ret.fetchall()
                    
                    if (len(db_result) != 0):
                        print("成功註冊")
                        print(db_result)
                        signUp_success = True

                con.close()

            else:
                pass

            # 成功路徑
            # if User_ID Not in DB
            if(signUp_success):
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
