# Generated by Django 4.1.3 on 2022-12-05 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
