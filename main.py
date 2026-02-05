from flask import Flask, render_template
import redis
import mysql.connector
import time
import json

app = Flask(__name__)

def connect_redis():
    r = redis.Redis(
            host="localhost",
            port=6379,
            password="<your_redis_password>",
            decode_responses=True
        )
    return r

def connect_mysql():
    connection = mysql.connector.connect(
        host="localhost",
        user="<your_mysql_db_user>",
        password="<your_mysql_db_user_password>",
        database="<your_database>"
    )
    return connection

def get_courses_from_redis():
    try:
        redis_client = connect_redis()
        courses = redis_client.get('courses')
        if courses:
            return json.loads(courses)
        return None
    except Exception as e:
        print(f"Redis error: {e}")
        return None

def get_courses_from_mysql():
    try:
        connection = connect_mysql()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM best_selling_courses")
        courses = cursor.fetchall()
        cursor.close()
        connection.close()

        if not courses:
            return []
        
        try:
            # Cache in Redis for future requests
            redis_client = connect_redis()
            redis_client.setex('courses', 60, json.dumps(courses))
        except Exception as e:
            print(f"Redis caching error: {e}")
        
        return courses
    except Exception as e:
        print(f"MySQL error: {e}")
        return []

@app.route('/')
def index():
    start_time = time.time()

    courses = get_courses_from_redis()
    if not courses:
        courses = get_courses_from_mysql()
        database = "MySQL"
    else:
        database = "Redis"

    end_time = time.time()
    load_time = end_time - start_time

    return render_template('index.html', courses=courses, load_time=load_time, database=database)

if __name__ == "__main__":

    app.run(debug=True, port=5000)
