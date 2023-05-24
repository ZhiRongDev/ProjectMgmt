from flask import Flask, jsonify, request, Response, Blueprint
from flask_cors import CORS

WorksOn_bp = Blueprint('WorksOn', __name__)

# enable CORS
CORS(WorksOn_bp)

@WorksOn_bp.route('/WorksOn', methods=['POST', 'DELETE'])
def WorksOn():
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
                    'response': '新增協作者成功',
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
        elif request.method == 'DELETE':
            Project_ID = request.args.get('Project_ID')
            Worker_ID = request.args.get('Worker_ID')
            print(Worker_ID)
            print(Project_ID)

            if(True):
                response_object = {
                    'status': 'success',
                    'response': '刪除成功',
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