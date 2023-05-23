from flask import Flask, jsonify, request, Response, Blueprint
from flask_cors import CORS

Project_bp = Blueprint('Project', __name__)

# enable CORS
CORS(Project_bp)

# query 範例:
# http://127.0.0.1:5001/Project?User_ID=xxx&type=all
# http://127.0.0.1:5001/Project?User_ID=xxx&Project_ID=xxx&type=specified
@Project_bp.route('/Project', methods=['GET', 'POST', 'PUT', 'DELETE'])
def Project_operstion():
    if request.method == 'GET':
        # 表示前端送過來的 Query
        User_ID = request.args.get('User_ID')
        type = request.args.get('type')

        # 取得所有跟 User_ID 相關的 Project 資料
        if(type == 'all'):
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
                    'response': '取得 Project 成功',
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
        
        # 取得特定 Project_ID 的相關資料
        elif(type == 'specified'):
            Project_ID = request.args.get('Project_ID')

            if(True):
                # db return example
                return_data = {
                    "Project_Name": 'project 1',
                    "Project_Color": 'pink'
                }

                response_object = {
                    'status': 'success',
                    'response': '取得 Project 成功',
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
        User_ID = request.args.get('User_ID')
        # post_data format
        # {
        #     Project_ID: "",
        #     Project_Name: "",
        #     Project_Color: "",
        # }

        post_data = request.get_json()
        print(post_data)

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
        User_ID = request.args.get('User_ID')
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
    elif request.method == 'DELETE':
        # 表示前端送過來的 Query
        User_ID = request.args.get('User_ID')
        type = request.args.get('type')

        if(type == 'all'):
            return 0
        
        # 刪除特定 Project_ID 的相關資料
        elif(type == 'specified'):
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