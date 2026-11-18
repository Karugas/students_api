import random


def random_student_data():
    random_num = random.randint(1000, 9999)
    return {
        "email": f"ivan{random_num}@example.com",
        "gender": "male",
        "name": "Ivan Ivano",
        "phone_no": f"+7999000{random_num}",
        "status": 1
    }


def student_for_update():
    return {
        "email": "petrov@exampdle.com",
        "gender": "male",
        "name": "Yaromir",
        "status": 1
        }
