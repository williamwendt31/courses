# Generated by Django 2.1.1 on 2018-09-17 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20180917_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='course_desc',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='course', to='courses.Description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='description',
            name='desc',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
