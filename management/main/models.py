from django.db import models
from django.core.exceptions import ValidationError
from accounts.models import Customer, Employee


class Task(models.Model):
    STATUS_CHOICES = (
        ("WAIT", "Ожидает исполнитея"),
        ("ONGOING", "В процессе"),
        ("DONE", "Выполнена"),
    )
    title = models.CharField("Заголовок",
                             max_length=200)
    status = models.CharField("Статус",
                              choices=STATUS_CHOICES,
                              max_length=20, blank=True, null=True)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.SET_NULL,
                                 related_name="tasks",
                                 verbose_name="Заказчик",
                                 null=True)
    executor = models.ForeignKey(Employee,
                                 on_delete=models.SET_NULL,
                                 related_name="employee",
                                 verbose_name="Исполнитель",
                                 null=True)
    date_of_creation = models.DateTimeField("Дата создания",
                                            auto_now_add=True)
    update_date = models.DateTimeField("Дата обновления",
                                       auto_now=True)

    closing_date = models.DateTimeField("Дата закрытия", blank=True, null=True)

    report = models.TextField("Отчет", blank=True, null=True)

    def __str__(self):
        return self.title

    def clean(self):
        if self.closing_date and not self.report:
            raise ValidationError({
                'EmptyReportError': 'При закрытии задачи отчет не может быть пустым'
            })

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return '/main/%s' % self.pk

    class Meta:
        verbose_name_plural = "Задачи"
        verbose_name = "Задача"
        ordering = ["-date_of_creation"]
        indexes = [
            models.Index(fields=['-date_of_creation'])
        ]

