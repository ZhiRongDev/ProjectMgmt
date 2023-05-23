from flask import Flask, jsonify, request, Response, Blueprint
from flask_cors import CORS

Task_List_bp = Blueprint('Task_List', __name__)

# enable CORS
CORS(Task_List_bp)

# query 範例:
# http://127.0.0.1:5001/Task_List?User_ID=xxx&Project_ID=xxx&type=all
@Task_List_bp.route('/Task_List', methods=['GET'])
def Task_List_operation():
    if request.method == 'GET':
        # 表示前端送過來的 Query
        User_ID = request.args.get('User_ID')
        Project_ID = request.args.get('Project_ID')
        type = request.args.get('type')

        # 取得所有跟 Project_ID 相關的 Project 資料
        if(type == 'all'):
            if(True):
                # db return example
                return_data = [
                    {
                        "Task_List_ID": '77889',
                        "Task_List_Name": 'List1',
                        "Task_List_Status": True,
                        "Task_Card": [
                            {
                                "Task_Card_ID": '54321',
                                "Task_Card_Name": 'Card1',
                                "Task_Card_Text": 'Card1 text',
                                "Task_Card_StartTime": '1998',
                                "Task_Card_EndTime": '2021',
                                "Task_Card_Status": True,
                                "Todo": [
                                    {
                                        "Todo_ID": '798234',
                                        "Todo_Text": 'todo text',
                                        "Todo_Status": True
                                    }
                                ],
                                "Comment": [
                                    {
                                        "Commenter_ID": '5648',
                                        "Commenter_Name": 'jenny',
                                        "Comment_Text": 'Comment_Text'
                                    }
                                ],
                                "Task_Card_Collaborators": [
                                    {
                                        "User_ID": '789',
                                        "User_Name": 'jenny',
                                        "User_Mail": 'jenny@gmail.com',
                                        "User_Avatar": 'https://randomuser.me/api/portraits/women/82.jpg',
                                    },
                                ],
                            }
                        ]
                    },
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