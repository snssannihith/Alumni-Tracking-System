# Generated by Django 2.2 on 2021-03-09 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminmodel',
            name='department',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='adminmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='StudentModel',
        ),
    ]
