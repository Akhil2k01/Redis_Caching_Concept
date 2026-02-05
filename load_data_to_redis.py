import redis
import random
import string

def connect_redis():
    r = redis.Redis(
            host="localhost",
            port=6379,
            password="redis@test",
            decode_responses=True
        )
    return r

def load_data_to_redis(data):
    r = connect_redis()
    
    for idx, course_data in enumerate(data):
        key = f"course:{idx+1}"
        value = ", ".join(str(val) for val in course_data)
        r.set(key, value, ex=60)

    print(f"Loaded {len(data)} sample data into Redis with expiration of 60 seconds.")

def generate_random_course():
    course_name = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 15)))
    instructor = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 10)))
    students_enrolled = random.randint(100,500)
    price = round(random.uniform(10.0, 99.99), 2)
    rating = round(random.uniform(3.0, 5.0), 1)
    return course_name, instructor, students_enrolled, price, rating

def load_courses_to_redis():
    r = connect_redis()

    for idx in range(1, 1001):
        course_data = generate_random_course()
        key = f"course:{idx}"
        value = ", ".join(str(val) for val in course_data)
        r.set(key, value, ex=60)

    print("Loaded 1000 courses into Redis with expiration of 60 seconds.")

if __name__ == "__main__":
    sample_data = [
        ("Maths", "Alice", 200, 49.99, 4.5),
        ("Science", "Bob", 150, 59.99, 4.2),
        ("Computer", "Charlie", 300, 79.99, 4.8)
    ]
    load_data_to_redis(sample_data)
    load_courses_to_redis()