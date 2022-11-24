# Generated by Django 4.1.3 on 2022-11-24 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('rol', models.IntegerField(default=1)),
                ('password', models.CharField(max_length=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
