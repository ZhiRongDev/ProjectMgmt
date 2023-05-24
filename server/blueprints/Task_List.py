from flask import Flask, jsonify, request, Response, Blueprint
from flask_cors import CORS

Task_List_bp = Blueprint('Task_List', __name__)

# enable CORS
CORS(Task_List_bp)

@Task_List_bp.route('/Task_List', methods=['POST', 'PUT', 'DELETE'])
def Task_List_operation():
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
                    'response': '新增 Task_List 成功',
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

        # query 範例:
        # http://127.0.0.1:5001/Task_List?User_ID=xxx
        elif request.method == 'PUT':
            # put_data format
            # {
            #     'Task_List_ID': '',
            #     'Task_List_Name': '',
            #     'Task_List_Status': ''
            # }

            put_data = request.get_json()
            print(put_data)
            
            # 修改成功
            if(True):
                response_object = {
                    'status': 'success',
                    'response': '修改 Task_List 成功',
                    'method': 'PUT',
                    'route': ''
                }
                return jsonify(response_object)
            # 失敗路徑
            else:
                return Response(
                    response = "取得 Task_List 失敗",
                    status = 400,
                )

        # http://127.0.0.1:5001/Task_List?User_ID=xxx&Task_List_ID=xxx
        elif request.method == 'DELETE':
            Task_List_ID = request.args.get('Task_List_ID')
            print(Task_List_ID)
            # 允許刪除
            if(True):
                response_object = {
                    'status': 'success',
                    'response': '刪除 Task_List 成功',
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