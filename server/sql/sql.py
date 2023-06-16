import sqlite3

db = sqlite3.connect('ProjectMgmt.db')
cursor = db.cursor()
print('Connect ok')

#建立table: user
cursor.execute("DROP TABLE IF EXISTS `user`;")
cursor.execute('''
CREATE TABLE user  
(   
    `User_ID` varchar(10) NOT NULL,
    `User_Name` varchar(15) DEFAULT NULL,
    `User_Mail` varchar(30) DEFAULT NULL,
    `User_Avatar` varchar(30) DEFAULT NULL,
    `User_Password` varchar(30) DEFAULT NULL,

    PRIMARY KEY (`User_ID`)
); 
''')


#建立table: Project
cursor.execute("DROP TABLE IF EXISTS `Project`;")
cursor.execute('''
CREATE TABLE Project  
(   
    `Project_ID` varchar(10) NOT NULL,
    `Project_Name` varchar(30) DEFAULT NULL,
    `Project_Color` varchar(15) DEFAULT NULL,
    `Mgr_ID` varchar(10) DEFAULT NULL,

    PRIMARY KEY (`Project_ID`),
    
    CONSTRAINT `mgridFK` 
    FOREIGN KEY (`Mgr_ID`) 
    REFERENCES `user` (`User_ID`) 
    ON DELETE CASCADE

); 
''')


#建立table: task_card
cursor.execute("DROP TABLE IF EXISTS `task_card`;")
cursor.execute('''
CREATE TABLE task_card  
(   
    `Task_Card_ID` varchar(10) NOT NULL,
    `Task_Card_Name` varchar(30) DEFAULT NULL,
    `Task_Card_Text` varchar(60) DEFAULT NULL,
    `Task_Card_StartTime` datetime DEFAULT NULL,
    `Task_Card_EndTime` datetime DEFAULT NULL,
    `Task_Card_Status` tinyint(1) DEFAULT NULL,
    `Task_List_ID` varchar(10) DEFAULT NULL,

    PRIMARY KEY (`Task_Card_ID`),
    
    CONSTRAINT `taskidFK` 
    FOREIGN KEY (`Task_List_ID`) 
    REFERENCES `task_list` (`Task_List_ID`) 
    ON DELETE CASCADE
); 
''')


#建立table: task_list
cursor.execute("DROP TABLE IF EXISTS `task_list`;")
cursor.execute('''
CREATE TABLE task_list  
(   
    `Task_List_ID` varchar(10) NOT NULL,
    `Task_List_Name` varchar(30) DEFAULT NULL,
    `Task_List_Status` tinyint(1) DEFAULT NULL,
    `Project_ID` varchar(10) DEFAULT NULL,

    PRIMARY KEY (`Task_List_ID`),

    CONSTRAINT `projectidFK` 
    FOREIGN KEY (`Project_ID`) 
    REFERENCES `project` (`Project_ID`) 
    ON DELETE CASCADE
); 
''')


#建立table: todo
cursor.execute("DROP TABLE IF EXISTS `todo`;")
cursor.execute('''
CREATE TABLE todo  
(   
    `Todo_ID` varchar(10) NOT NULL,
    `Todo_Text` varchar(45) DEFAULT NULL,
    `Todo_Status` tinyint(1) DEFAULT NULL,
    `Task_Card_ID` varchar(10) DEFAULT NULL,

    PRIMARY KEY (`Todo_ID`),

    CONSTRAINT `taskcardidFK` 
    FOREIGN KEY (`Task_Card_ID`) 
    REFERENCES `task_card` (`Task_Card_ID`)
); 
''')


#建立table: Comment
cursor.execute("DROP TABLE IF EXISTS `Comment`;")
cursor.execute('''
CREATE TABLE Comment  
(   
    `Commenter_ID` varchar(10) NOT NULL,
    `Commenter_Name` varchar(15) DEFAULT NULL,
    `Comment_Text` varchar(60) DEFAULT NULL,
    `Task_Card_ID` varchar(10) DEFAULT NULL,
    
    PRIMARY KEY (`Commenter_ID`),

    CONSTRAINT `taskcardFK` 
    FOREIGN KEY (`Task_Card_ID`) 
    REFERENCES `task_card` (`Task_Card_ID`)

); 
''')


#建立table: project_workson
cursor.execute("DROP TABLE IF EXISTS `project_workson`;")
cursor.execute('''
CREATE TABLE project_workson  
(   
    `User_ID` varchar(10) NOT NULL,
    `Project_ID` varchar(10) NOT NULL,

    PRIMARY KEY (`User_ID`,`Project_ID`),

    CONSTRAINT `projectFK` 
    FOREIGN KEY (`Project_ID`) 
    REFERENCES `project` (`Project_ID`),

    CONSTRAINT `userFK` 
    FOREIGN KEY (`User_ID`) 
    REFERENCES `user` (`User_ID`)

); 
''')


#建立table: task_workson
cursor.execute("DROP TABLE IF EXISTS `task_workson`;")
cursor.execute('''
CREATE TABLE task_workson  
(   
    `User_ID` varchar(10) NOT NULL,
    `Task_Card_ID` varchar(10) NOT NULL,

    PRIMARY KEY (`User_ID`,`Task_Card_ID`),

    CONSTRAINT `cardtaskFK` 
    FOREIGN KEY (`Task_Card_ID`) 
    REFERENCES `task_card` (`Task_Card_ID`),

    CONSTRAINT `usertaskFK` 
    FOREIGN KEY (`User_ID`) 
    REFERENCES `user` (`User_ID`)

); 
''')

db.commit()
db.close()

# cursor.execute("LOCK TABLES `comment` WRITE; ")
# cursor.execute("UNLOCK TABLES;")

# r = cursor.execute("select name from sqlite_master where type='table' order by name")
# print (cursor.fetchall())
# for i in r:
#     print(i)

# cursor.execute("SELECT * FROM project")
# col_name_list = [tuple[0] for tuple in cursor.description]
# # print(cursor.description)
# print(col_name_list)

# cursor.execute("PRAGMA table_info(project)")
# print (cursor.fetchall())
print("Success!")