from flask import Flask, jsonify, request, Response, Blueprint
from flask_cors import CORS

import sqlite3

Project_bp = Blueprint('Project', __name__)

# enable CORS
CORS(Project_bp)

# query 範例:
# http://127.0.0.1:5001/Project?User_ID=xxx
@Project_bp.route('/Project', methods=['GET', 'POST', 'PUT', 'DELETE'])
def Project():
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
        if request.method == 'GET':
            return_data = []
            get_success = False

            con = sqlite3.connect("./sql/ProjectMgmt.db")
            cur = con.cursor()
            ret = cur.execute(f"""SELECT Project_ID FROM Project_WorksOn WHERE User_ID = {User_ID}""") 

            db_result = ret.fetchall()

            for project in db_result:
                id = project[0]
                ret = cur.execute(f"""SELECT * FROM Project WHERE Project_ID = {id}""") 
                project_list = ret.fetchone()
                # print(project_list)

                if(project_list):
                    new_project = {
                        "Project_ID": project_list[0],
                        "Project_Name": project_list[1],
                        "Project_Color": project_list[2],
                    }
                    return_data.append(new_project)
                        
            get_success = True
            con.close()

            if(get_success):
                response_object = {
                    'status': 'success',
                    'response': '取得 Project list 成功',
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
            
        # 新增專案
        # http://127.0.0.1:5001/Project?User_ID=xxx
        elif request.method == 'POST':
            post_data = request.get_json()
            print(post_data)

            Project_ID = post_data.get('Project_ID')
            Project_Name = post_data.get('Project_Name')
            Project_Color = post_data.get('Project_Color') or "#15CCB5"
            Mgr_ID = User_ID

            post_success = False

            if(Project_ID and Project_Name):
                con = sqlite3.connect("./sql/ProjectMgmt.db")
                cur = con.cursor()

                # 預設是 True
                cur.execute("""
                    INSERT INTO Project VALUES (?, ?, ?, ?)
                """, (Project_ID, Project_Name, Project_Color, Mgr_ID))

                con.commit()

                cur.execute("""
                    INSERT INTO Project_WorksOn VALUES (?, ?)
                """, (User_ID, Project_ID))

                con.commit()
                
                ret = cur.execute(""" SELECT * FROM Project WHERE Project_ID=? """, (Project_ID, ))
                db_result = ret.fetchone()

                if (db_result):
                    print("成功新增 Project")
                    print(db_result)
                    post_success = True

                con.close()

            if(post_success):
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
            put_data = request.get_json()
            print(put_data)
            
            Project_ID = put_data.get('Project_ID')
            
            set_str = ""
            exe_tuple = ()

            for key, value in put_data.items():
                if key != 'Project_ID':
                    set_str = set_str + key + "=?, "
                    exe_tuple = exe_tuple + (value, )

            set_str =  set_str[:-2] 
            exe_str = "UPDATE Project SET " + set_str + " WHERE Project_ID=" + Project_ID
            print(exe_str)
            print(exe_tuple)
            
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
                    'response': '修改 Project 成功',
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
        # http://127.0.0.1:5001/Project?User_ID=xxx&Project_ID=xxx
        elif request.method == 'DELETE':
            Project_ID = request.args.get('Project_ID')
            print(Project_ID)

            del_success = False

            if (Project_ID):
                con = sqlite3.connect("./sql/ProjectMgmt.db")
                cur = con.cursor()
                cur.execute("DELETE FROM Project WHERE Project_ID=?", (Project_ID, ))
                con.commit()
                con.close()
                del_success = True

            if(del_success):
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
    else:
        return Response(
            response = "驗證失敗",
            status = 400,
        )
    
# http://127.0.0.1:5001/Project/Content?User_ID=xxx&Project_ID=xxx
@Project_bp.route('/Project/Content', methods=['GET'])
def Project_Content():
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
        if request.method == 'GET':
            # 取得特定 Project_ID 所有相關內容
            Project_ID = request.args.get('Project_ID')

            Project_exist = False

            con = sqlite3.connect("./sql/ProjectMgmt.db")
            cur = con.cursor()
            ret = cur.execute(f"""SELECT * FROM Project_WorksOn WHERE Project_ID = {Project_ID}""")
            db_result = ret.fetchall()

            for worksOn in db_result:
                if worksOn[0] == User_ID:
                    Project_exist = True

            if(Project_exist):
                return_data = {}

                # Project Info
                con = sqlite3.connect("./sql/ProjectMgmt.db")
                cur = con.cursor()
                ret = cur.execute(f"""SELECT * FROM Project WHERE Project_ID = {Project_ID}""")
                Project_result = ret.fetchone() 

                return_data["Project_ID"] = Project_ID
                return_data["Project_Name"] = Project_result[1]
                return_data["Project_Color"] = Project_result[2]

                # Project_WorksOn
                Project_WorksOn = []
                ret = cur.execute(f"""SELECT * FROM Project_WorksOn WHERE Project_ID ={Project_ID}""")
                Project_WorksOn_result = ret.fetchall()

                for item in Project_WorksOn_result:
                    ret = cur.execute(f"""SELECT * FROM User WHERE User_ID ={item[0]}""")
                    User_result = ret.fetchone()

                    Project_WorksOn.append({
                        "User_ID": User_result[0],
                        "User_Name": User_result[1],
                        "User_Mail": User_result[2],
                        "User_Avatar": User_result[3]
                    }) 

                return_data["Project_WorksOn"] = Project_WorksOn

                # Task_List
                Task_List = []
                ret = cur.execute(f"""SELECT * FROM task_list WHERE Project_ID ={Project_ID}""")
                Task_List_result = ret.fetchall()

                for Task_List_result_item in Task_List_result:
                    Task_List_item = {}
                    Task_List_item["Task_List_ID"] = Task_List_result_item[0]
                    Task_List_item["Task_List_Name"] = Task_List_result_item[1]
                    Task_List_item["Task_List_Status"] = Task_List_result_item[2]
                    
                    # Task_Card
                    Task_Card = []
                    ret = cur.execute(f"""SELECT * FROM Task_Card WHERE Task_List_ID ={Task_List_item["Task_List_ID"]}""")
                    Task_Card_result = ret.fetchall()

                    for Task_Card_result_item in Task_Card_result:
                        Task_Card_item = {}
                        Task_Card_item["Task_Card_ID"] = Task_Card_result_item[0]
                        Task_Card_item["Task_Card_Name"] = Task_Card_result_item[1]
                        Task_Card_item["Task_Card_Text"] = Task_Card_result_item[2]
                        Task_Card_item["Task_Card_StartTime"] = Task_Card_result_item[3]
                        Task_Card_item["Task_Card_EndTime"] = Task_Card_result_item[4]
                        Task_Card_item["Task_Card_Status"] = Task_Card_result_item[5]
                        
                        # Task_WorksOn
                        Task_WorksOn = []
                        ret = cur.execute(f"""SELECT * FROM Task_WorksOn WHERE Task_Card_ID ={Task_Card_item["Task_Card_ID"]}""")
                        Task_WorksOn_result = ret.fetchall()
                        
                        for Task_WorksOn_result_item in Task_WorksOn_result:
                            Task_WorksOn_item = {}
                            ret = cur.execute(f"""SELECT * FROM User WHERE User_ID ={Task_WorksOn_result_item[0]}""")
                            worker_info = ret.fetchone()
                            Task_WorksOn_item["User_ID"] = worker_info[0]
                            Task_WorksOn_item["User_Name"] = worker_info[1]
                            Task_WorksOn_item["User_Mail"] = worker_info[2]
                            Task_WorksOn_item["User_Avatar"] = worker_info[3]
                            
                            Task_WorksOn.append(Task_WorksOn_item)

                        Task_Card_item["Task_WorksOn"] = Task_WorksOn

                        # Todo
                        Todo = []
                        ret = cur.execute(f"""SELECT * FROM Todo WHERE Task_Card_ID ={Task_Card_item["Task_Card_ID"]}""")
                        Todo_result = ret.fetchall()

                        for Todo_result_item in Todo_result:
                            Todo_item = {}
                            Todo_item["Todo_ID"] = Todo_result_item[0]
                            Todo_item["Todo_Text"] = Todo_result_item[1]
                            Todo_item["Todo_Status"] = Todo_result_item[2]
                            
                            Todo.append(Todo_item)

                        Task_Card_item["Todo"] = Todo
                        
                        # Comment
                        Comment = []
                        ret = cur.execute(f"""SELECT * FROM Comment WHERE Task_Card_ID ={Task_Card_item["Task_Card_ID"]}""")
                        Comment_result = ret.fetchall()

                        for Comment_result_item in Comment_result:
                            Comment_item = {}
                            Comment_item["Comment_ID"] = Comment_result_item[0]
                            Comment_item["Commenter_ID"] = Comment_result_item[1]
                            Comment_item["Commenter_Name"] = Comment_result_item[2]
                            Comment_item["Comment_Text"] = Comment_result_item[3]

                            ret = cur.execute(f"""SELECT * FROM User WHERE User_ID ={Comment_item["Commenter_ID"]}""")
                            Commenter_info = ret.fetchone()

                            Comment_item["Commenter_Mail"] = Commenter_info[2]
                            Comment_item["Commenter_Avatar"] = Commenter_info[3]

                            Comment.append(Comment_item)

                        Task_Card_item["Comment"] = Comment
                        
                        # append
                        Task_Card.append(Task_Card_item)
                    
                    Task_List_item["Task_Card"] = Task_Card
                    
                    # append
                    Task_List.append(Task_List_item)

                return_data["Task_List"] = Task_List

                con.close()

                response_object = {
                    'status': 'success',
                    'response': '取得 specified Project 成功',
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

    else:
        return Response(
            response = "驗證失敗",
            status = 400,
        )