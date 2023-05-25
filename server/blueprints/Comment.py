from flask import Flask, jsonify, request, Response, Blueprint
from flask_cors import CORS

Comment_bp = Blueprint('Comment', __name__)

# enable CORS
CORS(Comment_bp)

@Comment_bp.route('/Comment', methods = ['POST', 'DELETE'])
def Comment():
    # 表示前端送過來的 Query
    User_ID = request.args.get('User_ID')

    # if User_ID 存在於資料庫
    if (True):
        if request.method == 'POST':
            if(True):
                response_object = {
                    'status': 'success',
                    'response': '新增留言成功',
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

        elif request.method == 'DELETE':
            Commenter_ID = request.args.get('Commenter_ID')
            print(Commenter_ID)

            if(True):
                response_object = {
                    'status': 'success',
                    'response': '刪除留言成功',
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