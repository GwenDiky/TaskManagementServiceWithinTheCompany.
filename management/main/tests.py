# tasks/tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task
from accounts.models import Customer, Employee
from django.urls import reverse


class TaskPermissionsTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.customer_user = User.objects.create(username='customer', password='password')
        self.customer = Customer.objects.create(user=self.customer_user, name='Олег', surname='Герасимович',
                                                patronymic='Сергеевич', phone='+375292184567')

        self.employee_user = User.objects.create(username='employee', password='password')
        self.employee = Employee.objects.create(user=self.employee_user, name='Анастасия', surname='Назарова',
                                                patronymic='Владимировна', phone='+3753345678766', company='Company',
                                                job_title='Веб-разработчик', image='')

    def test_customer_can_create_task(self):
        self.client.force_authenticate(user=self.customer_user)

        url = reverse('main:task-create')
        data = {
            'title': 'Новая задача',
            'status': 'WAIT',
            'customer': self.customer.id,
            'executor': None,
            'closing_date': None,
            'report': ''
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_employee_cannot_create_task(self):
        self.client.force_authenticate(user=self.employee_user)

        url = reverse('main:task-create')
        data = {
            'title': 'Новая задача',
            'status': 'WAIT',
            'customer': self.customer.id,
            'executor': None,
            'closing_date': None,
            'report': ''
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
