# Generated by Django 5.0.4 on 2024-05-06 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_bookinstance_imprint'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['first_name']},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['author']},
        ),
    ]
