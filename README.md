# How to run Flask application and mongo using docker compose :

## Prerequisite :
First, ensure that you installed Docker and docker compose

Please check this [link](https://docs.docker.com/engine/install/ubuntu/)

âfter that, install requirements packages via terminal
```
pip install -r requirements.txt
```
## Run and test :
 step 1: Run

```
docker compose up 
```

Step 2: Navigate to `http://localhost:5000/` !
 
p/s: you should pass mount directory path with mongo :

change line : /home/duy/Flask-mongo-example/db_storage in docker-compose.ml file to your real directory

Step 3 : Use the app and add student 

Step 4 : To verify data update, please run the check_db.py

```
python check_db.py 
```
