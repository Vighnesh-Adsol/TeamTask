# Generated by Django 5.1.1 on 2024-11-10 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task_rec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('task_name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=700)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
