# ProjectMgmt
1112 Database System final project, a basic project management system for team members.

Frontend using **Vue.js + Vite + Pinia** and backend using **Flask + sqlite3**, further information were documented in [documents](https://github.com/ZhiRongDev/ProjectMgmt/tree/main/documents).

[The website is deployed](https://projectmgmt-fgfs.onrender.com) on render.com.

## Project Setup
Install the dependency for **client** inside the `root` directory

```
$ npm install
```

(Optional) Set up the virtual environment for **server** inside the `server` directory

```
$ cd ./server
$ python -m venv env

$ ./env/Scripts/activate
or
$ source ./env/bin/activate

(env)$
```

Install the dependency for Flask

```
(env)$ pip install -r requirements.txt
```

Start the client inside the `root` directory

```
$ npm run dev
```

Start the server inside the `server` directory

```
$ flask run --port=5001 --debug
```

or 

```
$ python app.py
```

The sqlite3 db file is `server/sql/ProjectMgmt.db`. You can recreate `ProjectMgmt.db` using this command inside the `server/sql` directory

```
$ python sql.py
```

## Contributors
|組員|系級|學號|
|-|-|-|
|程至榮|資科碩一|111753151|
|吳邁龍|資科碩一|111753150|
|蘇柏鈞|資科碩一|111753133|
|吳家瑩|資科碩一|111753221|
|黃滋宥|資科碩一|111753224|