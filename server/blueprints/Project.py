from flask import Flask, jsonify, request, Response, Blueprint
from flask_cors import CORS

Project_bp = Blueprint('Project', __name__)

# enable CORS
CORS(Project_bp)

# query 範例:
# http://127.0.0.1:5001/Project?User_ID=xxx&type=list
# http://127.0.0.1:5001/Project?User_ID=xxx&Project_ID=xxx&type=specified
@Project_bp.route('/Project', methods=['GET', 'POST', 'PUT', 'DELETE'])
def Project_operstion():
    # 表示前端送過來的 Query
    User_ID = request.args.get('User_ID')

    # if User_ID 存在於資料庫
    if (True):
        if request.method == 'GET':
            type = request.args.get('type')
            # 取得 User_ID 相關的所有 Project
            if(type == 'list'):
                if(True):
                    # db return example
                    return_data = [
                        {
                            "Project_ID": "abc",
                            "Project_Name": "project 1",
                            "Project_Color": "pink",
                        },
                        {
                            "Project_ID": "def",
                            "Project_Name": "project 2",
                            "Project_Color": "blue",
                        },
                    ]

                    response_object = {
                        'status': 'success',
                        'response': '取得 Project list 成功',
                        'method': 'GET',
                        'route': ''
                    }
                    response_object["return_data"] = return_data
                    return jsonify(response_object)
                # 失敗路徑
                else:
                    return Response(
                        response = "取得 Project 失敗",
                        status = 400,
                )
            
            # 取得特定 Project_ID 的所有相關資料
            elif(type == 'specified'):
                Project_ID = request.args.get('Project_ID')
                if(True):
                    # db return example
                    return_data = {
                        "Project_ID": "abc",
                        "Project_Name": "project 1",
                        "Project_Color": "pink",
                        "Project_WorksOn": [
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
                        ],
                        "Task_List": [
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
                                        "Task_WorksOn": [
                                            {
                                                "User_ID": '456',
                                                "User_Name": 'jenny',
                                                "User_Mail": 'jenny@gmail.com',
                                                "User_Avatar": 'https://randomuser.me/api/portraits/women/81.jpg',
                                            },
                                        ],
                                        "Todo": [
                                            {
                                                "Todo_ID": '798234',
                                                "Todo_Text": 'todo text',
                                                "Todo_Status": True
                                            }
                                        ],
                                        "Comment": [
                                            {
                                                "Commenter_ID": '456',
                                                "Commenter_Name": 'jenny',
                                                "Comment_Text": 'Comment_Text'
                                            }
                                        ],
                                    }
                                ]
                            },
                        ],
                    }

                    response_object = {
                        'status': 'success',
                        'response': '取得 specified Project 成功',
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
            
        # 新增專案
        # http://127.0.0.1:5001/Project?User_ID=xxx
        elif request.method == 'POST':
            # post_data format
            # {
            #     Project_ID: "",
            #     Project_Name: "",
            #     Project_Color: "",
            # }

            post_data = request.get_json()
            # print(post_data)

            if(True):
                response_object = {
                    'status': 'success',
                    'response': '新增成功',
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

        # 更新專案資料
        # http://127.0.0.1:5001/Project?User_ID=xxx
        elif request.method == 'PUT':
            # put_data format
            # {
            #     Project_ID: "",
            #     Project_Name: "",
            #     Project_Color: "",
            # }

            put_data = request.get_json()
            # print(put_data)

            if(True):
                response_object = {
                    'status': 'success',
                    'response': '修改成功',
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
            
        # 刪除專案
        # http://127.0.0.1:5001/Project?User_ID=xxx&Project_ID=xxx
        elif request.method == 'DELETE':
            Project_ID = request.args.get('Project_ID')
            if(True):
                response_object = {
                    'status': 'success',
                    'response': '刪除 Project 成功',
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