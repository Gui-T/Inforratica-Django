# Generated by Django 4.2.4 on 2023-08-09 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inforratica', '0017_ordemservico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemservico',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True),
        ),
    ]