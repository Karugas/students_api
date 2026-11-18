import pytest
from students_api.src.api.api_client import ApiClient
from students_api.src.data.student_data import random_student_data


@pytest.fixture(scope="function")
def client():
    # Создаём чистый клиент для сессии
    client = ApiClient()
    yield client


@pytest.fixture()
def create_student(client):
    payload = random_student_data()
    student = client.create_new_student(payload)
    student_id = student.json()["student"]["id"]

    yield student_id
    client.delete_students(student_id)
