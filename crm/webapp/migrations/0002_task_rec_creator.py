# Generated by Django 5.1.1 on 2024-11-11 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_rec',
            name='creator',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
