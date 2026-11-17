import requests
from pydantic import BaseModel


class StudentSchema(BaseModel):
    email: str
    gender: str
    id: int
    name: str
    phone_no: str
    status: int


class ApiClient:
    def __init__(self):
        self.base_url = "http://194.87.126.16"
        self.session = requests.Session()

    def get_all_students(self):
        url = f"{self.base_url}/student"
        response = self.session.get(url)
        return response
