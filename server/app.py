from flask import Flask, jsonify, request, Response
from flask_cors import CORS

## 以下是假資料(模擬某個 User 的相關資料)
user_example = {
    "User_ID": "123",
    "User_Name": "jordan",
    "User_Mail": "jordan@gmail.com",
    "User_Avatar": "https://randomuser.me/api/portraits/men/1.jpg",
    "User_Password": "123456",
    
    "Project": [
        {
            "Project_ID": "abc",
            "Project_Name": "project 1",
            "Project_Color": "pink",
            "Project_Collaborators": [
                {
                    "User_ID": "123",
                    "User_Name": "jordan",
                    "User_Mail": "jordan@gmail.com",
                    "User_Avatar": "https://randomuser.me/api/portraits/men/1.jpg",
                },
                {
                    "User_ID": '456',
                    "User_Name": 'selina',
                    "User_Mail": 'selina@gmail.com',
                    "User_Avatar": 'https://randomuser.me/api/portraits/women/81.jpg',
                },
                {
                    "User_ID": '789',
                    "User_Name": 'jenny',
                    "User_Mail": 'jenny@gmail.com',
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
            ],
        },
    ],
}

################################################################

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

"""範例格式如下，固定用以下格式回傳
(變數名稱就直接叫做 query_name, post_data, return_data, response_object......):

@app.route('/example', methods=['POST'])
def example():
    if request.method == 'POST':
        # 表示網址有包含 query，例如 /example?query_name=123
        query_name = request.args.get('query_name')

        # 前端送過來的資料格式
        # post_data format
        # {
        #   'User_Mail': "",
		# 	'User_Password': "",
        # }

        # 轉成可以用的 JSON
        post_data = request.get_json()

        # 撈 DB 資料
        # 成功路徑
        if (xxx):
            # 回傳資料
            return_data = {
                "User_ID": "123",
                "User_Name": "jordan",
                "User_Mail": "jordan@gmail.com",
                "User_Avatar": "https://randomuser.me/api/portraits/men/1.jpg"
            }

            # 請務必附上以下資訊方便 Degug
            response_object = {
                'status': 'success',
                'method': 'POST',
                'route': '/example'
            }
            response_object["return_data"] = return_data
            return jsonify(response_object)
            
        # 失敗路徑，麻煩根據失敗原因撰寫 Response，會直接顯示在前端
        elif:
            return Response(
                "失敗，帳號錯誤",
                status = 400,
            )
        else:
            return Response(
                "失敗，密碼錯誤",
                status = 400,
            )
"""

# query 範例:
# http://127.0.0.1:5001/user?type=sign-in
@app.route('/User', methods=['POST'])
def User_operation():
    if request.method == 'POST':
        type = request.args.get('type')
        # 登入功能，回傳 User 資訊
        if (type == "sign-in"):
            # post_data format
            # {
            #   'User_Mail': "",
            # 	'User_Password': "",
            # }

            post_data = request.get_json()
            Mail = post_data['User_Mail']
            Password = post_data['User_Password']

            # 成功路徑
            # if mail in DB
            if (True):
                # if passward is correct
                if (True):
                    # return User information
                    return_data = {
                        "User_ID": "123",
                        "User_Name": "jordan",
                        "User_Mail": "jordan@gmail.com",
                        "User_Avatar": "https://randomuser.me/api/portraits/men/1.jpg"
                    }

                    response_object = {
                        'status': 'success',
                        'method': 'POST',
                        'route': '/user?type=sign-in'
                    }
                    response_object["return_data"] = return_data
                    return jsonify(response_object)
            # 失敗路徑
            else:
                return Response(
                    "登入失敗",
                    status = 400,
                )
        
        # 註冊功能，註冊完只需要回傳成功訊息
        elif (type == "sign-up"):
            # post_data format
            # {
            #     'User_ID': "",
            #     'User_Name': "",
            #     'User_Mail': "",
            #     'User_Avatar': "",
            #     'User_Password': ""
            # }
            post_data = request.get_json()

            # 成功路徑
            # if User_ID Not in DB
            if(True):
                # if User_Mail Not in DB, save post_data as new User in DB, and return to frontend
                if(True):                
                    response_object = {
                        'status': 'success',
                        'method': 'POST',
                        'route': '/user?type=sign-up'
                    }
                    return jsonify(response_object)
            # 失敗路徑
            else:
                return Response(
                    "註冊失敗",
                    status = 400,
                )

# query 範例:
# http://127.0.0.1:5001/project?User_ID=xxx&type=all
@app.route('/Project', methods=['GET'])
def Project_operstion():
    if request.method == 'GET':
        # 表示前端送過來的 Query
        User_ID = request.args.get('User_ID')
        type = request.args.get('type')

        # 取得所有跟 User_ID 相關的 Project 資料
        if(type == 'all'):
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
                'method': 'GET',
                'route': '/Project?type=' + type + '&User_ID=' + User_ID
            }
            response_object["return_data"] = return_data
            return jsonify(response_object)
        # 失敗路徑
        else:
            return Response(
                "xx失敗",
                status = 400,
            )

# query 範例:
# http://127.0.0.1:5001/Task_List&type=all&Project_ID=xxx
@app.route('/Task_List', methods=['GET'])
def Task_List_operation():
    if request.method == 'GET':
        # 表示前端送過來的 Query
        Project_ID = request.args.get('Project_ID')
        type = request.args.get('type')

        # 取得所有跟 User_ID 相關的 Project 資料
        if(type == 'all'):
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
                'method': 'GET',
                'route': '/Project?type=' + type + '&Project_ID=' + Project_ID
            }
            response_object["return_data"] = return_data
            return jsonify(response_object)
        # 失敗路徑
        else:
            return Response(
                "xx失敗",
                status = 400,
            )


if __name__ == '__main__':
    app.run()
