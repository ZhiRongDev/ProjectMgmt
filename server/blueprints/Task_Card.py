from flask import Flask, jsonify, request, Response, Blueprint
from flask_cors import CORS

import sqlite3
import datetime

Task_Card_bp = Blueprint('Task_Card', __name__)

# enable CORS
CORS(Task_Card_bp)

# query 範例:
# http://127.0.0.1:5001/Task_Card?User_ID=xxx
@Task_Card_bp.route('/Task_Card', methods=['POST', 'PUT', 'DELETE'])
def Task_Card():
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

            Task_Card_ID = post_data.get('Task_Card_ID')
            Task_Card_Name = post_data.get('Task_Card_Name')
            Task_Card_Text = post_data.get('Task_Card_Text')
            Task_Card_StartTime = datetime.date.today()
            Task_Card_EndTime = datetime.date.today()
            Task_Card_Status = True
            Task_List_ID = post_data.get('Task_List_ID')

            post_success = False

            if(Task_Card_ID and Task_Card_Name and Task_Card_Text and Task_List_ID):
                con = sqlite3.connect("./sql/ProjectMgmt.db")
                cur = con.cursor()
    
                cur.execute("""
                    INSERT INTO Task_Card VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (Task_Card_ID, Task_Card_Name, Task_Card_Text, Task_Card_StartTime, Task_Card_EndTime, Task_Card_Status, Task_List_ID))

                con.commit()

                cur.execute("""
                    INSERT INTO Task_WorksOn VALUES (?, ?)
                """, (User_ID, Task_Card_ID))

                con.commit()
                
                ret = cur.execute(""" SELECT * FROM Task_Card WHERE Task_Card_ID=? """, (Task_Card_ID, ))
                db_result = ret.fetchall()

                if (len(db_result) != 0):
                    print("成功新增任務卡")
                    print(db_result)
                    post_success = True

                con.close()

            # 修改成功
            if(post_success):
                response_object = {
                    'status': 'success',
                    'response': '新增 Task_Card 成功',
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

        elif request.method == 'PUT':
            put_data = request.get_json()
            print(put_data)

            Task_Card_ID = put_data.get('Task_Card_ID')

            set_str = ""
            exe_tuple = ()

            for key, value in put_data.items():
                if key != 'Task_Card_ID':
                    set_str = set_str + key + "=?, "
                    exe_tuple = exe_tuple + (value, )
            
            set_str =  set_str[:-2]
            exe_str = "UPDATE Task_Card SET " + set_str + "WHERE Task_Card_ID=" + Task_Card_ID
            
            put_success = False
            con = sqlite3.connect("./sql/ProjectMgmt.db")
            cur = con.cursor()
            cur.execute(exe_str, exe_tuple)
            con.commit()
            con.close()
            put_success = True

            if(put_success):                
                response_object = {
                    'status': 'success',
                    'response': '修改 Task_Card 成功',
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

        # http://127.0.0.1:5001/Task_List?User_ID=xxx&Task_Card_ID=xxx
        elif request.method == 'DELETE':
            Task_Card_ID = request.args.get('Task_Card_ID')
            print(Task_Card_ID)

            del_success = False

            if (Task_Card_ID):
                con = sqlite3.connect("./sql/ProjectMgmt.db")
                cur = con.cursor()
                cur.execute("DELETE FROM Task_Card WHERE Task_Card_ID=?", (Task_Card_ID, ))
                con.commit()
                con.close()
                del_success = True

            # 允許刪除
            if(del_success):
                response_object = {
                    'status': 'success',
                    'response': '刪除 Task_Card 成功',
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