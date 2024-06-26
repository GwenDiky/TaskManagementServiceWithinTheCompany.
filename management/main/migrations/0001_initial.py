# Generated by Django 5.0.6 on 2024-06-26 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('status', models.CharField(blank=True, choices=[('WAIT', 'Ожидает исполнитея'), ('ONGOING', 'В процессе'), ('DONE', 'Выполнена')], max_length=20, null=True, verbose_name='Статус')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('closing_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия')),
                ('report', models.TextField(blank=True, null=True, verbose_name='Отчет')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='accounts.customer', verbose_name='Заказчик')),
                ('executor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee', to='accounts.employee', verbose_name='Исполнитель')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'ordering': ['-date_of_creation'],
                'indexes': [models.Index(fields=['-date_of_creation'], name='main_task_date_of_d3a99b_idx')],
            },
        ),
    ]
