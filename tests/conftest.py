import allure
import pytest
from src.api.api_client import ApiClient
from src.data.student_data import random_student_data
from tenacity import retry, stop_after_delay, wait_fixed


@retry(stop=stop_after_delay(5), wait=wait_fixed(0.3), reraise=True)
def wait_for_student(client, student_id: int):
    response = client.get_student_data(student_id)
    return response


@pytest.fixture(scope="function")
def client():
    # Создаём чистый клиент для сессии
    client = ApiClient()
    yield client


@pytest.fixture(autouse=True)
def add_logs(caplog):
    yield
    allure.attach(caplog.text, name="logs", attachment_type=allure.attachment_type.TEXT)


@pytest.fixture()
def create_student(client):
    payload = random_student_data()
    student = client.create_new_student(payload)
    student_id = student.json()["student"]["id"]
    wait_for_student(client, student_id)

    yield student_id
    client.delete_students(student_id)
