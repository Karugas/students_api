def test_get_all_students(client):
    response = client.get_all_students()
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"


def test_create_new_student(client):
    response = client.create_new_student()
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    print(response.json())


def test_delete_student(client):
    response = client.delete_students(1)
    print(response.json())


def test_get_student_dat(client):
    response = client.get_student_data(2)
    print(response.json())

