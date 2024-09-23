# https://github.com/corydolphin/flask-cors/blob/master/examples/blueprints_based_example.py
from flask import Flask, jsonify, request, Response
from blueprints.User import User_bp
from blueprints.Project import Project_bp
from blueprints.WorksOn import WorksOn_bp
from blueprints.Task_List import Task_List_bp
from blueprints.Task_Card import Task_Card_bp
from blueprints.Todo import Todo_bp
from blueprints.Comment import Comment_bp

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

app.register_blueprint(User_bp)
app.register_blueprint(Project_bp)
app.register_blueprint(WorksOn_bp)
app.register_blueprint(Task_List_bp)
app.register_blueprint(Task_Card_bp)
app.register_blueprint(Todo_bp)
app.register_blueprint(Comment_bp)

# if __name__ == '__main__':
#     # app.run()
#     app.run(host='127.0.0.1', port=5001)

""" Blueprint 內撰寫的範例格式如下 (變數名稱就直接叫做 query_name, post_data, return_data, response_object......):

@app.route('/example', methods=['POST'])
def example():
    # 表示網址有包含 query, 例如 /example?User_ID=xxx&query_name=123
    User_ID = request.args.get('User_ID')
    query_name = request.args.get('query_name')

    # if User_ID 存在於資料庫
    if (True):
        if request.method == 'POST':

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
                # 回傳資料 (如果是 GET 才需要附上 return_data)
                return_data = {
                    "User_ID": "123",
                    "User_Name": "jordan",
                    "User_Mail": "jordan@gmail.com",
                    "User_Avatar": "https://randomuser.me/api/portraits/men/1.jpg"
                }

                # 請務必附上以下資訊，用於顯示在前端 & Debug
                response_object = {
                    'status': 'success',
                    'response': '登入成功',
                    'method': 'POST',
                    'route': '/example'
                }
                response_object["return_data"] = return_data
                return jsonify(response_object)
                
            # 失敗路徑，麻煩根據失敗原因撰寫 Response, 會直接顯示在前端
            elif:
                return Response(
                    response = "失敗，帳號錯誤",
                    status = 400,
                )
            else:
                return Response(
                    response = "失敗，密碼錯誤",
                    status = 400,
                )
    
    else:
        return Response(
            response = "驗證失敗",
            status = 400,
        )
"""

"""
GET: 根據給予的 xx_ID 回傳資料
POST: 根據 post_data 新增資料庫
PUT: 根據 put_data 修改資料庫
DELETE: 根據給予的 xx_ID 刪除資料
"""