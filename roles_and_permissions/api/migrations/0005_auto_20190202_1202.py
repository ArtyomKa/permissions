# Generated by Django 2.1.5 on 2019-02-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190127_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrole',
            name='change_date',
            field=models.DateField(),
        ),
    ]