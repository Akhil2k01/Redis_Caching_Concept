import random
import string
import mysql.connector

def connect_mysql():
    connection = mysql.connector.connect(
        host="localhost",
        user="akhil",
        password="password",
        database="mysql_db"
    )

    print("Connected to MySQL database.")

    return connection

def create_table_if_not_exists():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS best_selling_courses (
        id INT AUTO_INCREMENT PRIMARY KEY,
        course_name VARCHAR(255),
        instructor VARCHAR(255),
        students_enrolled INT,
        price VARCHAR(50),
        rating FLOAT(2, 1)
    );
    """

    try:
        connection = connect_mysql()
        cursor = connection.cursor()
        cursor.execute(create_table_query)
    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        cursor.close()
        connection.close()
        print("MySQL connection closed after table creation.")

def generate_random_course():
    course_name = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 15)))
    instructor = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 10)))
    students_enrolled = random.randint(100,500)
    price = f"{round(random.uniform(10.0, 99.99), 2)} INR"
    rating = round(random.uniform(3.0, 5.0), 1)
    return course_name, instructor, students_enrolled, price, rating

def load_data_to_mysql(data):
    connection = connect_mysql()
    cursor = connection.cursor()

    for idx, course_data in enumerate(data):
        query = "INSERT INTO best_selling_courses (course_name, instructor, students_enrolled, price, rating) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, course_data)

    connection.commit()
    print(f"Loaded {len(data)} sample data into MySQL.")
    cursor.close()
    connection.close()
    print("MySQL connection closed after data load.")

if __name__ == "__main__":
    sample_data = [
        ("Maths", "Alice", 200, "49.99 INR", 4.5),
        ("Science", "Bob", 150, "59.99 INR", 4.2),
        ("Computer", "Charlie", 300, "79.99 INR", 4.8)
    ]
    # sample_data = [
    #     generate_random_course() for _ in range(100)
    # ]
    create_table_if_not_exists()
    load_data_to_mysql(sample_data)