from flask import Flask, jsonify
from flask_cors import CORS


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

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
                                "User_ID": '',
                                "User_Name": '',
                                "User_Mail": '',
                                "User_Avatar": '',
                                "User_Password": ''
                            }
                        ],
                    }
                ]
            },
        ],
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()