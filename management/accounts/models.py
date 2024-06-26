from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Person(models.Model):

    phone_number_regex = RegexValidator(regex=r"^\+?375\(?(29|33|44|25)\)?\d{7}$")

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                verbose_name="Пользователь")
    name = models.CharField(max_length=30,
                            verbose_name="Имя")
    surname = models.CharField(verbose_name="Фамилия",
                               max_length=50)
    patronymic = models.CharField(verbose_name="Отчество",
                                  max_length=50)
    phone = models.CharField(
        validators=[phone_number_regex], max_length=16, unique=True, blank=False, null=False
    )

    class Meta:
        abstract = True


class Employee(Person):
    company = models.CharField(verbose_name="Компания",
                               max_length=200)
    job_title = models.CharField(verbose_name="Должность",
                                 max_length=100)
    image = models.ImageField(verbose_name="Фотография")

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    @receiver(post_save, sender=User)  # add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Employee.objects.create(user=instance)

    @receiver(post_save, sender=User)  # add this
    def save_user_profile(sender, instance, **kwargs):
        instance.employee.save()

    class Meta:
        verbose_name_plural = "Сотрудник"
        verbose_name = "Сотрудники"
        ordering = ["surname"]
        indexes = [
            models.Index(fields=['surname', "phone"])
        ]


class Customer(Person):
    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    @receiver(post_save, sender=User)  # add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)

    @receiver(post_save, sender=User)  # add this
    def save_user_profile(sender, instance, **kwargs):
        instance.customer.save()

    class Meta:
        verbose_name_plural = "Заказчик"
        verbose_name = "Заказчики"
        ordering = ["surname"]
        indexes = [
            models.Index(fields=['surname', "phone"])
        ]
