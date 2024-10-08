# Generated by Django 5.1 on 2024-09-10 20:56

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_image', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('name', models.CharField(max_length=200)),
                ('fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('about', django_ckeditor_5.fields.CKEditor5Field(default='Add about course', max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
