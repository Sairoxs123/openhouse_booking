# Generated by Django 4.1.7 on 2023-11-05 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_students_grade_sec_alter_reservations_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='grade_sec',
            field=models.CharField(max_length=3),
        ),
    ]