from flask import Flask, jsonify, request, Response, Blueprint
from flask_cors import CORS
import sqlite3
import json

Task_Card_bp = Blueprint('Task_Card', __name__)

# enable CORS
CORS(Task_Card_bp)

# query 範例:
# http://127.0.0.1:5001/Task_Card?User_ID=xxx
@Task_Card_bp.route('/Task_Card', methods=['POST', 'PUT', 'DELETE'])
def Task_Card():
    # 表示前端送過來的 Query
    User_ID = request.args.get('User_ID')

    # if User_ID 存在於資料庫
    if (True):
        if request.method == 'POST':
            post_data = request.get_json()
            print(post_data)
            
            data = json.loads(post_data)

            print(data)

            # print("測試")
            # print(User_ID)

            db = sqlite3.connect("./sql/ProjectMgmt.db")
            cursor = db.cursor()

            cursor.execute("SELECT User_ID FROM user WHERE User_ID={}".format(User_ID))
            result = cursor.fetchone()
            pflag = 0
            
            # 修改成功
            if(result != None):
                response_object = {
                    'status': 'success',
                    'response': '新增 Task_Card 成功',
                    'method': 'POST',
                    'route': ''
                }
                return jsonify(response_object)
            # 失敗路徑
            else:
                return Response(
                    response = "失敗",
                    status = 400,
                )


        elif request.method == 'PUT':
            put_data = request.get_json()
            print(put_data)
            
            if(True):                
                response_object = {
                    'status': 'success',
                    'response': '修改 Task_Card 成功',
                    'method': 'PUT',
                    'route': ''
                }
                return jsonify(response_object)
            # 失敗路徑
            else:
                return Response(
                    response = "失敗",
                    status = 400,
                )

        # http://127.0.0.1:5001/Task_List?User_ID=xxx&Task_Card_ID=xxx
        elif request.method == 'DELETE':
            Task_Card_ID = request.args.get('Task_Card_ID')
            print(Task_Card_ID)

            # 允許刪除
            if(True):
                response_object = {
                    'status': 'success',
                    'response': '刪除 Task_Card 成功',
                    'method': 'DELETE',
                    'route': ''
                }
                return jsonify(response_object)
            # 失敗路徑
            else:
                return Response(
                    response = "失敗",
                    status = 400,
                )

    else:
        return Response(
            response = "驗證失敗",
            status = 400,
        )