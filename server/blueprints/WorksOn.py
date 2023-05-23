from flask import Flask, jsonify, request, Response, Blueprint
from flask_cors import CORS

WorksOn_bp = Blueprint('WorksOn', __name__)

# enable CORS
CORS(WorksOn_bp)

# query 範例:
# http://127.0.0.1:5001/WorksOn?User_ID=xxx&Project_ID=xxx&type=Project
# http://127.0.0.1:5001/WorksOn?User_ID=xxx&Task_Card_ID=xxx&type=Task_Card
@WorksOn_bp.route('/WorksOn', methods=['GET', 'POST', 'PUT', 'DELETE'])
def WorksOn_operstion():
    # 表示前端送過來的 Query
    User_ID = request.args.get('User_ID')
    type = request.args.get('type')

    # if User_ID 存在於資料庫
    if (True):
        if request.method == 'GET':
            # 回傳跟特定 Project_ID 相關的所有協作者
            if(type == "Project"):
                Project_ID = request.args.get('Project_ID')

                if(True):
                    # db return example
                    return_data = [
                        {
                            "User_ID": '123',
                            "User_Name": 'jordan',
                            "User_Mail": 'jordan@gmail.com',
                            "User_Avatar": 'https://randomuser.me/api/portraits/men/1.jpg'
                        },
                        {
                            "User_ID": '456',
                            "User_Name": 'jenny',
                            "User_Mail": 'jenny@gmail.com',
                            "User_Avatar": 'https://randomuser.me/api/portraits/women/81.jpg',
                        },
                        {
                            "User_ID": '789',
                            "User_Name": 'selina',
                            "User_Mail": 'selina@gmail.com',
                            "User_Avatar": 'https://randomuser.me/api/portraits/women/82.jpg',
                        }
                    ]

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

            # 回傳跟特定 Task_Card_ID 相關的所有協作者
            elif(type == "Task_Card"):
                Task_Card_ID = request.args.get('Task_Card_ID')
                if(True):
                    # db return example
                    return_data = [
                        {
                            "User_ID": '456',
                            "User_Name": 'jenny',
                            "User_Mail": 'jenny@gmail.com',
                            "User_Avatar": 'https://randomuser.me/api/portraits/women/81.jpg',
                        },
                    ]

                    response_object = {
                        'status': 'success',
                        'response': '取得 Task_Card collaborator 成功',
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