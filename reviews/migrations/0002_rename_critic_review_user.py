# Generated by Django 4.1 on 2022-08-18 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="critic",
            new_name="user",
        ),
    ]
