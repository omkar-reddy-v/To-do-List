# Generated by Django 5.0.3 on 2024-03-28 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addtask', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phoneno', models.BigIntegerField()),
                ('gender', models.CharField(max_length=50)),
            ],
        ),
    ]
