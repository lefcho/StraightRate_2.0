# Generated by Django 5.1.3 on 2024-12-10 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creators', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='developer',
            options={'ordering': ['developer_name']},
        ),
        migrations.AlterModelOptions(
            name='director',
            options={'ordering': ['first_name', 'last_name']},
        ),
    ]
