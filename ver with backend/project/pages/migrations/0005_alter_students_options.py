# Generated by Django 4.0.4 on 2022-05-14 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_students_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='students',
            options={'ordering': ['id']},
        ),
    ]
