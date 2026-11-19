import allure
import logging
import requests
from pydantic import BaseModel


class StudentSchema(BaseModel):
    email: str
    gender: str
    id: int
    name: str
    phone_no: str
    status: int


UPDATE_STUDENT_SCHEMA = {
    "type": "object",
    "required": ["message", "status", "student"],
    "properties": {
        "message": {"type": "string"},
        "status": {"type": "integer"},
        "student": {
            "type": "object",
            "required": ["email", "gender", "id", "name", "phone_no", "status"],
            "properties": {
                "email": {"type": "string"},
                "gender": {"type": "string"},
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "phone_no": {"type": "string"},
                "status": {"type": "integer"}
            }
        }
    }
}


class ApiClient:
    def __init__(self):
        self.base_url = "http://194.87.126.16"
        self.session = requests.Session()

    @allure.step("Получаем список всех студентов")
    def get_all_students(self):
        url = f"{self.base_url}/student"
        response = self.session.get(url)
        logging.info(response.text)
        return response

    @allure.step("Создаём нового студента")
    def create_new_student(self, payload: dict):
        url = f"{self.base_url}/student"
        response = self.session.post(url, json=payload)
        logging.info(response.text)
        return response

    @allure.step("Удаляем студента c ID")
    def delete_students(self, student_id: int):
        url = f"{self.base_url}/student/{student_id}"
        response = self.session.delete(url)
        logging.info(response.text)
        return response

    @allure.step("Получаем данные студента")
    def get_student_data(self, student_id: int):
        url = f"{self.base_url}/student/{student_id}"
        response = self.session.get(url)
        logging.info(response.text)
        return response

    @allure.step("Обновляем данные студента")
    def update_student(self, student_id: int, payload: dict):
        url = f"{self.base_url}/student/{student_id}"
        response = self.session.put(url, json=payload)
        logging.info(response.text)
        return response
