from flask import Flask, jsonify, request, Response, Blueprint
from flask_cors import CORS

Task_Card_bp = Blueprint('Task_Card', __name__)

# enable CORS
CORS(Task_Card_bp)

# query 範例:
# http://127.0.0.1:5001/Task_Card?User_ID=xxx
@Task_Card_bp.route('/Task_Card', methods=['POST', 'PUT', 'DELETE'])
def Task_Card_operstion():
    # 表示前端送過來的 Query
    User_ID = request.args.get('User_ID')

    # if User_ID 存在於資料庫
    if (True):
        if request.method == 'POST':
            post_data = request.get_json()
            print(post_data)
            
            # 修改成功
            if(True):
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


        if request.method == 'PUT':
            # put_data format
            # {
            #     "Task_Card_ID": '',
            #     "Task_Card_Name": '',
            #     "Task_Card_Text": '',
            #     "Task_Card_StartTime": '',
            #     "Task_Card_EndTime": '',
            #     "Task_Card_Status": '',
            # }

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