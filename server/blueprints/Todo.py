from flask import Flask, jsonify, request, Response, Blueprint
from flask_cors import CORS

import sqlite3

Todo_bp = Blueprint('Todo', __name__)

# enable CORS
CORS(Todo_bp)

@Todo_bp.route('/Todo', methods=['POST', 'PUT', 'DELETE'])
def Todo():
    # 表示前端送過來的 Query
    User_ID = request.args.get('User_ID')
    
    con = sqlite3.connect("./sql/ProjectMgmt.db")
    cur = con.cursor()
    ret = cur.execute(""" SELECT * FROM user WHERE User_ID=? """, (User_ID, ))
    db_result = ret.fetchall()
    con.close()

    User_exist = False
    if (len(db_result) != 0):
        User_exist = True

    # if User_ID 存在於資料庫
    if (User_exist):
        if request.method == 'POST':
            post_data = request.get_json()
            print(post_data)

            Todo_ID = post_data.get('Todo_ID')
            Todo_Text = post_data.get('Todo_Text')
            Todo_Status = True
            Task_Card_ID = post_data.get('Task_Card_ID')

            post_success = False

            if (Todo_ID and Todo_Text and Todo_Status and Task_Card_ID):
                con = sqlite3.connect("./sql/ProjectMgmt.db")
                cur = con.cursor()
    
                # 預設是 True
                cur.execute("""
                    INSERT INTO Todo VALUES (?, ?, ?, ?)
                """, (Todo_ID, Todo_Text, Todo_Status, Task_Card_ID))

                con.commit()
                
                ret = cur.execute(""" SELECT * FROM Todo WHERE Todo_ID=? """, (Todo_ID, ))
                db_result = ret.fetchone()

                if (db_result):
                    print("成功新增 Todo")
                    print(db_result)
                    post_success = True

                con.close()

            if(post_success):                
                response_object = {
                    'status': 'success',
                    'response': '新增待辦事項成功',
                    'method': 'GET',
                    'route': ''
                }
                return jsonify(response_object)
            # 失敗路徑
            else:
                return Response(
                    response = "失敗",
                    status = 400,
                )

        elif request.method == 'PUT':
            put_data = request.get_json()
            print(put_data)

            Todo_ID = put_data.get('Todo_ID')
            Todo_Status = put_data.get('Todo_Status')

            put_success = False

            if(Todo_ID):
                con = sqlite3.connect("./sql/ProjectMgmt.db")
                cur = con.cursor()

                cur.execute("""
                    UPDATE Todo
                    SET Todo_Status=?
                    WHERE Todo_ID=?
                """, (Todo_Status, Todo_ID))

                con.commit()
                con.close()
                put_success = True

            if(put_success):
                response_object = {
                    'status': 'success',
                    'response': '更新待辦成功',
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
        
        elif request.method == 'DELETE':
            Todo_ID = request.args.get("Todo_ID")
            
            del_success = False

            if (Todo_ID):
                con = sqlite3.connect("./sql/ProjectMgmt.db")
                cur = con.cursor()
                cur.execute("DELETE FROM Todo WHERE Todo_ID=?", (Todo_ID, ))
                con.commit()
                con.close()
                del_success = True

            if(del_success):                
                response_object = {
                    'status': 'success',
                    'response': '刪除待辦成功',
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