# Generated by Django 3.1.4 on 2020-12-19 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0003_auto_20201219_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='option_id',
            field=models.IntegerField(default=None, max_length=4, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_id',
            field=models.IntegerField(default=None, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='quiz_id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False, unique=True),
        ),
    ]