# https://github.com/corydolphin/flask-cors/blob/master/examples/blueprints_based_example.py

from flask import Flask, jsonify, request, Response
from blueprints.User import User_bp
from blueprints.Project import Project_bp
from blueprints.Task_List import Task_List_bp

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

app.register_blueprint(User_bp)
app.register_blueprint(Project_bp)
app.register_blueprint(Task_List_bp)

if __name__ == '__main__':
    app.run()

""" Blueprint 內撰寫的範例格式如下 (變數名稱就直接叫做 query_name, post_data, return_data, response_object......):

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

            # 請務必附上以下資訊，用於顯示在前端 & Debug
            response_object = {
                'status': 'success',
                'response': '登入成功',
                'method': 'POST',
                'route': '/example'
            }
            response_object["return_data"] = return_data
            return jsonify(response_object)
            
        # 失敗路徑，麻煩根據失敗原因撰寫 Response，會直接顯示在前端
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
"""

