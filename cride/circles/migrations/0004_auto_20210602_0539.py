# Generated by Django 3.1.1 on 2021-06-02 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circles', '0003_invitation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='used',
            field=models.BooleanField(default=False),
        ),
    ]
