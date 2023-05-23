from flask import Flask, jsonify, request, Response, Blueprint
from flask_cors import CORS

Task_List_bp = Blueprint('Task_List', __name__)

# enable CORS
CORS(Task_List_bp)

# query 範例:
# http://127.0.0.1:5001/Task_List?User_ID=xxx&Project_ID=xxx&type=all
@Task_List_bp.route('/Task_List', methods=['GET', 'POST', 'PUT', 'DELETE'])
def Task_List_operation():
    # 表示前端送過來的 Query
    User_ID = request.args.get('User_ID')
    type = request.args.get('type')
    
    # if User_ID 存在於資料庫
    if (True):
        if request.method == 'GET':
            Project_ID = request.args.get('Project_ID')

            # 取得所有跟 Project_ID 相關的 Task_List 資料
            if(type == 'all'):
                if(True):
                    # db return example
                    return_data = [
                        
                    ]

                    response_object = {
                        'status': 'success',
                        'response': '取得 Task_List 成功',
                        'method': 'GET',
                        'route': '/Project?type=' + type + '&Project_ID=' + Project_ID
                    }
                    response_object["return_data"] = return_data
                    return jsonify(response_object)
                # 失敗路徑
                else:
                    return Response(
                        response = "取得 Task_List 失敗",
                        status = 400,
                    )
    
    else:
        return Response(
            response = "驗證失敗",
            status = 400,
        )