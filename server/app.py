from flask import Flask, jsonify, request
from flask_cors import CORS

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/user/sign-in', methods=['POST'])
def signIn():
    if request.method == 'POST':
        post_data = request.get_json()
        # post_data 格式
        
        print(post_data)
        
        response_object = {'status': 'success'}
        return jsonify(response_object)

@app.route('/user/sign-up', methods=['POST'])
def signUp():
    if request.method == 'POST':
        post_data = request.get_json()
        # post_data 格式
        # {
        #     User_ID: "",
        #     User_Name: "",
        #     User_Mail: "",
        #     User_Avatar: "",
        #     User_Password: ""
        # }

        # print(post_data)
        response_object = {'status': 'success'}
        return jsonify(response_object)
        

@app.route('/project', methods=['GET'])
def get_project():
    data = {
        "Project": [
            {
                "Project_ID": "abc",
                "Project_Name": "project 1",
                "Project_Color": "pink",
                "Project_Collaborators": [
                    {
                        "User_ID": '2320948',
                        "User_Name": 'selina',
                        "User_Mail": 'selina@gmail.com',
                        "User_Avatar": 'https://randomuser.me/api/portraits/women/81.jpg',
                    }
                ]
            },
            {
                "Project_ID": "def",
                "Project_Name": "project 2",
                "Project_Color": "blue",
                "Project_Collaborators": [
                    {
                        "User_ID": '2320948',
                        "User_Name": 'selina',
                        "User_Mail": 'selina@gmail.com',
                        "User_Avatar": 'https://randomuser.me/api/portraits/women/81.jpg',
                    }
                ]
            }
        ]
    }
    return jsonify(data)

# GET 方法 -> 一次取得所有需要的資料 
@app.route('/tasklist', methods=['GET'])
def get_task_list():
    data = {
        "Task_List": [
            {
                "Task_List_ID": '12345',
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
                                "Todo_ID": 'abc',
                                "Todo_Text": 'todo text',
                                "Todo_Status": True
                            }
                        ],
                        "Comment": [
                            {
                                "Commenter_ID": 'cba',
                                "Commenter_Name": 'commenter_Name',
                                "Comment_Text": 'Comment_Text'
                            }
                        ],
                        "collaborators": [
                            {
                                "User_ID": '2320948',
                                "User_Name": 'selina',
                                "User_Mail": 'selina@gmail.com',
                                "User_Avatar": 'https://randomuser.me/api/portraits/women/81.jpg',
                            },
                        ],
                    }
                ]
            },
        ],
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run()
