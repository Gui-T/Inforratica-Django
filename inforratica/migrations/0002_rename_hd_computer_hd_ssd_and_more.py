# Generated by Django 4.2.1 on 2023-05-26 17:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("inforratica", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="computer",
            old_name="hd",
            new_name="hd_ssd",
        ),
        migrations.RenameField(
            model_name="computer",
            old_name="memoria",
            new_name="memoria_ram",
        ),
        migrations.RemoveField(
            model_name="computer",
            name="ssd",
        ),
    ]
