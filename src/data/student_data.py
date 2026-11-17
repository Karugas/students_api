import random


def random_student_data():
    random_num = random.randint(1000, 9999)
    payload = {
        "email": f"ivan{random_num}@example.com",
        "gender": "male",
        "name": "Ivan Ivanov",
        "phone_no": f"+7999000{random_num}",
        "status": 1
    }
