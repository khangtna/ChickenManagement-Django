# Generated by Django 4.1.2 on 2022-11-12 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0012_alter_emps_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emps',
            name='email',
            field=models.EmailField(default='abc@gmail.com', max_length=50, unique=True),
        ),
    ]