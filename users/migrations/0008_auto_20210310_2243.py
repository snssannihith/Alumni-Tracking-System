# Generated by Django 2.2 on 2021-03-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_college_workexp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexp',
            name='address',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='workexp',
            name='end_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
