from flask import Flask, jsonify, request, Response, Blueprint
from flask_cors import CORS

import sqlite3

WorksOn_bp = Blueprint('WorksOn', __name__)

# enable CORS
CORS(WorksOn_bp)

@WorksOn_bp.route('/WorksOn/Project_WorksOn', methods=['POST', 'DELETE'])
def Project_WorksOn():
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

            # Project_WorksOn 一次只會新增一筆 User_ID
            post_data = request.get_json()
            print(post_data)

            Project_ID = post_data.get('Project_ID')
            add_User_Mail = post_data.get('User_Mail')
            add_User_ID = ""

            post_success = False

            con = sqlite3.connect("./sql/ProjectMgmt.db")
            cur = con.cursor()
            ret = cur.execute(""" SELECT * FROM user WHERE User_Mail=? """, (add_User_Mail, ))
            db_result = ret.fetchone()
            con.close()

            if (db_result):
                print(db_result)
                add_User_ID = db_result[0]

                con = sqlite3.connect("./sql/ProjectMgmt.db")
                cur = con.cursor()
    
                cur.execute("""
                    INSERT INTO Project_WorksOn VALUES (?, ?)
                """, (add_User_ID, Project_ID))

                con.commit()
                
                ret = cur.execute(""" SELECT * FROM Project_WorksOn WHERE User_ID=? AND Project_ID=?""", (add_User_ID, Project_ID))
                db_result = ret.fetchone()

                if (db_result):
                    print("成功新增 Project_WorksOn")
                    print(db_result)
                    post_success = True

                con.close()

            if(post_success):
                response_object = {
                    'status': 'success',
                    'response': '新增 Project_WorksOn 成功',
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
            Project_ID = request.args.get('Project_ID')
            Worker_ID = request.args.get('Worker_ID')
            print(Worker_ID)
            print(Project_ID)

            del_success = False

            if (Worker_ID and Project_ID):
                con = sqlite3.connect("./sql/ProjectMgmt.db")
                cur = con.cursor()
                
                cur.execute("DELETE FROM Project_WorksOn WHERE User_ID=? AND Project_ID=?", (Worker_ID, Project_ID))
                con.commit()

                # Need to delete Task_WorksOn either 
                ret = cur.execute(f"""
                    SELECT Task_WorksOn.Task_Card_ID
                    FROM Task_WorksOn, Task_Card, Task_List, Project
                    WHERE 
                        Task_WorksOn.Task_Card_ID = Task_Card.Task_Card_ID AND
                        Task_Card.Task_List_ID = Task_List.Task_List_ID AND
                        Task_List.Project_ID = Project.Project_ID AND
                        Task_WorksOn.User_ID = {User_ID} AND
                        Project.Project_ID = {Project_ID}
                """)

                db_result = ret.fetchall()

                for item in db_result:
                    cur.execute("DELETE FROM Task_WorksOn WHERE User_ID=? AND Task_Card_ID=?", (Worker_ID, item[0]))
                    con.commit()

                print("Testing !!")
                print(db_result)

                con.close()
                del_success = True

            if(del_success):
                response_object = {
                    'status': 'success',
                    'response': '刪除 Project_WorksOn 成功',
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
    

@WorksOn_bp.route('/WorksOn/Task_WorksOn', methods=['POST', 'DELETE'])
def Task_WorksOn():
    # 表示前端送過來的 Query
    User_ID = request.args.get('User_ID')

    con = sqlite3.connect("./sql/ProjectMgmt.db")
    cur = con.cursor()
    ret = cur.execute(""" SELECT * FROM user WHERE User_ID=? """, (User_ID, ))
    db_result = ret.fetchone()
    con.close()

    User_exist = False
    if (db_result):
        User_exist = True

    # if User_ID 存在於資料庫
    if (User_exist):
        if request.method == 'POST':
            # Task_WorksOn 一次會新增多筆 User_ID
            post_data = request.get_json()
            print(post_data)
    
            Task_Card_ID = post_data.get('Task_Card_ID')
            User_ID_List = post_data.get('User_ID_List')

            post_success = False
            insert_data = []

            for User_ID in User_ID_List:
                insert_data.append( (User_ID, Task_Card_ID) )

            if (Task_Card_ID and User_ID_List):
                con = sqlite3.connect("./sql/ProjectMgmt.db")
                cur = con.cursor()
    
                cur.executemany("""
                    INSERT INTO Task_WorksOn VALUES (?, ?)
                """, insert_data)

                con.commit()

                print("成功新增 Project_WorksOn")
                post_success = True

                con.close()

            if(post_success):
                response_object = {
                    'status': 'success',
                    'response': '新增 Task_WorksOn 成功',
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
            Task_Card_ID = request.args.get('Task_Card_ID')
            Worker_ID = request.args.get('Worker_ID')
            print(Worker_ID)
            print(Task_Card_ID)

            del_success = False

            if (Task_Card_ID and Worker_ID):
                con = sqlite3.connect("./sql/ProjectMgmt.db")
                cur = con.cursor()
                cur.execute("DELETE FROM Task_WorksOn WHERE User_ID=? AND Task_Card_ID=?", (Worker_ID, Task_Card_ID))
                con.commit()
                con.close()
                del_success = True
            
            if(del_success):
                response_object = {
                    'status': 'success',
                    'response': '刪除 Task_WorksOn 成功',
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