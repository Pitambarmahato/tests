import pytest
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Student

# Create your tests here.
class TestStudent(TestCase):
    def setUp(self):
        self.apiClinet = APIClient()
        self.std = Student.objects.create(name="pitambar", std_class=5, roll=12, mark=50)
    # @pytest.mark.django_db
    def test_product(self):
        assert self.std.name == "pitambar"
    
    def test_grade(self):
        assert self.std.grade == "pass"
    
    def test_str_return(self):
        result = Student.objects.get(name="pitambar")
        assert str(result) == "pitambar"

    def test_student_get(self):
        response = self.apiClinet.get('/api/student/')
        print("Hello World")
        print(response.json())
        assert response.status_code == 200
    
    def test_student_post(self):
        response = self.apiClinet.post('/api/student/', 
                        {"name": "Raj", "std_class":12, "roll": 22, "mark": 43}, format="json")
        assert response.status_code == 201
    
    def test_student_put(self):
        response = self.apiClinet.put('/api/student/1/', {"name": "Shyam"}, format="json")
        assert response.status_code == 200
    
    def test_student_delete(self):
        response = self.apiClinet.delete('/api/student/1/')
        assert response.status_code == 204

