# Generated by Django 5.0 on 2024-02-08 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_alter_admin_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('phno', models.IntegerField(max_length=10)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=12)),
                ('cpwd', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'registration_table',
            },
        ),
    ]