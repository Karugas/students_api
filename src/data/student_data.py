import random
import string


def random_student_data():
    random_num = random.randint(1000, 9999)
    random_gender = random.choice(["male", "female"])
    random_status = random.choice([0, 1])
    random_name = "".join(random.choices(string.ascii_letters, k=8))

    return {
        "email": f"ivan{random_num}@example.com",
        "gender": f"{random_gender}",
        "name": f"{random_name}",
        "phone_no": f"+7999000{random_num}",
        "status": random_status
    }


def student_for_update():
    random_num = random.randint(1000, 9999)
    random_gender = random.choice(["male", "female"])
    random_status = random.choice([0, 1])
    random_name = "".join(random.choices(string.ascii_letters, k=8))
    return {
        "email": f"yaromir{random_num}@mail.com",
        "gender": f"{random_gender}",
        "name": f"{random_name}",
        "status": random_status
        }
