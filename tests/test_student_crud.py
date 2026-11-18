import allure

from students_api.src.data.student_data import random_student_data, student_for_update
from students_api.src.api.api_client import StudentSchema


@allure.title("Выводим список всех студентов")
def test_get_all_students(client, create_student):
    student_id = create_student
    response = client.get_all_students()
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    data_id = response.json()["students"]
    all_ids = []
    # Проверяем соответствие Schema
    for student in data_id:
        StudentSchema(**student)
    #Проверяем созданного студента в списке всех студентов
    for student in data_id:
        all_ids.append(student["id"])
    assert student_id in all_ids, "Созданного студента нет в списке всех студентов"
    client.delete_students(student_id)


@allure.title("Создаём нового студента")
def test_create_new_student(client):
    response = client.create_new_student(random_student_data())
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    data = response.json()
    StudentSchema(**data["student"])
    student_id = data["student"]["id"]
    # Проверяем что студент был создан через GET
    student_id_get = client.get_student_data(student_id).json()
    assert student_id == student_id_get, "Пользователь не был создан"


@allure.title("Удаление студента")
def test_delete_student(client, create_student):
    response = client.delete_students(student_id=create_student)
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    assert response.json() == {'message': 'Student deleted successfully', 'status': 1}
    assert client.get_student_data(create_student) == 404, "Студент не был удалён"


@allure.title("Получаем данные о студенте")
def test_get_student_data(client, create_student):
    response = client.get_student_data(student_id=create_student)
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    data = response.json()
    # Проверяем соответствие Schema
    StudentSchema(**data["student"])
    assert data["student"]["id"] == create_student, f"Ожидали получить данные пользователя, но пришло {data}"


@allure.title("Изменяем данные о студенте")
def test_update_student_data(client, create_student):
    response = client.update_student(student_id=create_student, payload=student_for_update())
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    assert response.json()["message"] == "Student updated successfully", "Студент не был изменён"
    response = client.get_student_data(student_id=create_student)
    data = response.json()
    # Проверяем соответствие Schema
    StudentSchema(**data["student"])
    assert data["student"]["name"] == "Yaromir", "Студент не был изменён"
