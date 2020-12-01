# Generated by Django 3.1.3 on 2020-12-01 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndustriesModel',
            fields=[
                ('ino', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationModel',
            fields=[
                ('rno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('contact', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('otp', models.IntegerField()),
                ('doj', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('pno', models.AutoField(primary_key=True, serialize=False)),
                ('education', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='user_images/')),
                ('resume', models.FileField(upload_to='user_resumes/')),
                ('itype', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='process.industriesmodel')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='process.registrationmodel')),
            ],
        ),
    ]
