from flask import Flask, jsonify, request, Response, Blueprint
from flask_cors import CORS

Todo_bp = Blueprint('Todo', __name__)

# enable CORS
CORS(Todo_bp)

@Todo_bp.route('/Todo', methods=['POST', 'PUT', 'DELETE'])
def Todo():
    # 表示前端送過來的 Query
    User_ID = request.args.get('User_ID')

    # if User_ID 存在於資料庫
    if (True):
        if request.method == 'POST':
            post_data = request.get_json()
            print(post_data)

            if(True):                
                response_object = {
                    'status': 'success',
                    'response': '新增待辦事項成功',
                    'method': 'GET',
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
                    'response': '更新待辦成功',
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
        
        elif request.method == 'DELETE':
            if(True):                
                response_object = {
                    'status': 'success',
                    'response': '刪除待辦成功',
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