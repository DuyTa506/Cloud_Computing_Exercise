# How to run Flask application and mongo using docker compose :

## Prerequisite :
Step 0 :
 
```
pip install -r requirements.txt
```

 step 1: Run

```
docker compose up 
```

Step 2: Navigate to `http://localhost:5000/` !
 
p/s: you should pass mount directory path with mongo :

change line :- /home/duy/Flask-mongo-example/db_storage in docker-compose.ml file to your real directory

Step 3 : Use the app and add student 
Step 4 : To verify data update, please run the check_db.py

```
python check_db.py 
```
