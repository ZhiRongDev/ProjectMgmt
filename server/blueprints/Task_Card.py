from flask import Flask, jsonify, request, Response, Blueprint
from flask_cors import CORS

Task_Card_bp = Blueprint('Task_Card', __name__)

# enable CORS
CORS(Task_Card_bp)

# query 範例:
# http://127.0.0.1:5001/Task_Card?User_ID=xxx&Project_ID=xxx&type=Project
# http://127.0.0.1:5001/Task_Card?User_ID=xxx&Task_Card_ID=xxx&type=Task_Card
@Task_Card_bp.route('/Task_Card', methods=['GET', 'POST', 'PUT', 'DELETE'])
def Task_Card_operstion():
    # 表示前端送過來的 Query
    User_ID = request.args.get('User_ID')
    type = request.args.get('type')

    # if User_ID 存在於資料庫
    if (True):
        if request.method == 'GET':
            # 回傳跟特定 Project_ID 相關的所有協作者
            if(type == ""):
                if(True):
                    # db return example
                    return_data = []
                    
                    response_object = {
                        'status': 'success',
                        'response': '取得 Project collaborator 成功',
                        'method': 'GET',
                        'route': ''
                    }
                    response_object["return_data"] = return_data
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