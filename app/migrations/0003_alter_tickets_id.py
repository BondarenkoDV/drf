# Generated by Django 3.2.16 on 2022-12-09 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_tickets_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
