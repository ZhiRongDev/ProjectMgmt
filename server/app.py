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

# 登入功能，回傳 User 資訊
@app.route('/user/sign-in', methods=['POST'])
def signIn():
    if request.method == 'POST':
        # post_data format
        # {
        #   'User_Mail': "",
		# 	'User_Password': "",
        # }

        post_data = request.get_json()
        Mail = post_data['User_Mail']
        Password = post_data['User_Password']

        # if mail in DB
        if (True):
            # if passward is correct
            if (True):
                # return User information
                UserInfo = {
                    "User_ID": "123",
                    "User_Name": "jordan",
                    "User_Mail": "jordan@gmail.com",
                    "User_Avatar": "https://randomuser.me/api/portraits/men/1.jpg"
                }

                response_object = {'status': 'success'}
                response_object["UserInfo"] = UserInfo
                return jsonify(response_object)
        else:
            return Response(
                "登入失敗",
                status = 400,
            )
# 描述: 註冊功能
@app.route('/user/sign-up', methods=['POST'])
def signUp():
    if request.method == 'POST':
        # post_data format
        # {
        #     'User_ID': "",
        #     'User_Name': "",
        #     'User_Mail': "",
        #     'User_Avatar': "",
        #     'User_Password': ""
        # }
        post_data = request.get_json()

        # if User_ID Not in DB
        if(False):
            # if User_Mail Not in DB, save post_data as new User in DB, and return to frontend
            if(True):                
                response_object = {'status': 'success'}
                return jsonify(response_object)
        else:
            return Response(
                "註冊失敗",
                status = 400,
            )


@app.route('/project', methods=['GET'])
def get_project():
    global user_example
    # data = user_example["Project"]

    response_object = {'status': 'success'}
    # response_object["Project"] = data

    return jsonify(response_object)

# GET 方法 -> 一次取得所有需要的資料 
@app.route('/tasklist', methods=['GET'])
def get_task_list():
    global user_example
    # data = user_example["Task_List"]
    
    response_object = {'status': 'success'}
    # response_object["Task_List"] = data

    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
