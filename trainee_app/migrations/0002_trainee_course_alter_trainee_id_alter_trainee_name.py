# Generated by Django 5.1.7 on 2025-03-12 22:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0002_track_alter_course_id_course_track'),
        ('trainee_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainee',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course_app.course'),
        ),
        migrations.AlterField(
            model_name='trainee',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='trainee',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
