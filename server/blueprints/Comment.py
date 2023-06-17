from flask import Flask, jsonify, request, Response, Blueprint
from flask_cors import CORS

import sqlite3

Comment_bp = Blueprint('Comment', __name__)

# enable CORS
CORS(Comment_bp)

@Comment_bp.route('/Comment', methods = ['POST', 'DELETE'])
def Comment():
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
            # print(post_data)

            Commenter_ID = post_data.get('Commenter_ID')
            Comment_addTime = post_data.get('Comment_addTime')
            Commenter_Name = post_data.get('Commenter_Name')
            Comment_Text = post_data.get('Comment_Text')
            Task_Card_ID = post_data.get('Task_Card_ID')

            # print(Commenter_ID, Comment_addTime, Commenter_Name, Comment_Text, Task_Card_ID)
            
            post_success = False

            if(Commenter_ID and Comment_addTime and Commenter_Name and Comment_Text and Task_Card_ID):
                con = sqlite3.connect("./sql/ProjectMgmt.db")
                cur = con.cursor()
    
                # 預設是 True
                cur.execute("""
                    INSERT INTO Comment VALUES (?, ?, ?, ?, ?)
                """, (Commenter_ID, Comment_addTime, Commenter_Name, Comment_Text, Task_Card_ID))

                con.commit()
                
                ret = cur.execute(""" SELECT * FROM Comment WHERE Commenter_ID=? AND Comment_addTime=? """, (Commenter_ID, Comment_addTime))
                db_result = ret.fetchall()

                if (len(db_result) != 0):
                    print("成功新增留言")
                    print(db_result)
                    post_success = True

                con.close()

            if(post_success):
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
            Comment_addTime = request.args.get('Comment_addTime')
            # print(Commenter_ID, Comment_addTime)

            del_success = False

            if (Commenter_ID and Comment_addTime):
                con = sqlite3.connect("./sql/ProjectMgmt.db")
                cur = con.cursor()
                cur.execute("DELETE FROM Comment WHERE Commenter_ID=? AND Comment_addTime=?", (Commenter_ID, Comment_addTime))
                con.commit()
                con.close()
                del_success = True

            if(del_success):
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
        print("驗證失敗")
        return Response(
            response = "驗證失敗",
            status = 400,
        )