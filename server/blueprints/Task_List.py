from flask import Flask, jsonify, request, Response, Blueprint
from flask_cors import CORS

import sqlite3

Task_List_bp = Blueprint('Task_List', __name__)

# enable CORS
CORS(Task_List_bp)

@Task_List_bp.route('/Task_List', methods=['POST', 'PUT', 'DELETE'])
def Task_List():
    # 表示前端送過來的 Query
    User_ID = request.args.get('User_ID')
    Project_ID = request.args.get('Project_ID')

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

            Task_List_ID = post_data.get('Task_List_ID')
            Task_List_Name = post_data.get('Task_List_Name')
            Task_List_Status = True

            # if(Task_List_Name):
            #     Task_List_Name.replace(" ", "")

            post_success = False

            if(Task_List_ID and Task_List_Name):
                con = sqlite3.connect("./sql/ProjectMgmt.db")
                cur = con.cursor()
    
                # 預設是 True
                cur.execute("""
                    INSERT INTO Task_List VALUES (?, ?, ?, ?)
                """, (Task_List_ID, Task_List_Name, Task_List_Status, Project_ID))

                con.commit()
                
                ret = cur.execute(""" SELECT * FROM Task_List WHERE Task_List_ID=? """, (Task_List_ID, ))
                db_result = ret.fetchall()

                if (len(db_result) != 0):
                    print("成功新增任務列表")
                    print(db_result)
                    post_success = True

                con.close()

            # 修改成功
            if(post_success):
                response_object = {
                    'status': 'success',
                    'response': '新增 Task_List 成功',
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

        # query 範例:
        # http://127.0.0.1:5001/Task_List?User_ID=xxx
        elif request.method == 'PUT':

            put_data = request.get_json()
            print(put_data)
            
            Task_List_ID = put_data.get('Task_List_ID')
            
            set_str = ""
            exe_tuple = ()

            for key, value in put_data.items():
                if key != 'Task_List_ID':
                    set_str = set_str + key + "=? "
                    exe_tuple = exe_tuple + (value, )
            
            exe_str = "UPDATE Task_List SET " + set_str + "WHERE Task_List_ID=" + Task_List_ID

            put_success = False
            con = sqlite3.connect("./sql/ProjectMgmt.db")
            cur = con.cursor()
            cur.execute(exe_str, exe_tuple)
            con.commit()
            con.close()
            put_success = True

            # 修改成功
            if(put_success):
                response_object = {
                    'status': 'success',
                    'response': '修改 Task_List 成功',
                    'method': 'PUT',
                    'route': ''
                }
                return jsonify(response_object)
            # 失敗路徑
            else:
                return Response(
                    response = "取得 Task_List 失敗",
                    status = 400,
                )

        # http://127.0.0.1:5001/Task_List?User_ID=xxx&Task_List_ID=xxx
        elif request.method == 'DELETE':
            Task_List_ID = request.args.get('Task_List_ID')
            print(Task_List_ID)

            del_success = False

            if (Task_List_ID):
                con = sqlite3.connect("./sql/ProjectMgmt.db")
                cur = con.cursor()
                cur.execute("DELETE FROM Task_List WHERE Task_List_ID=?", (Task_List_ID, ))
                con.commit()
                con.close()
                del_success = True

            # 允許刪除
            if(del_success):
                response_object = {
                    'status': 'success',
                    'response': '刪除 Task_List 成功',
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