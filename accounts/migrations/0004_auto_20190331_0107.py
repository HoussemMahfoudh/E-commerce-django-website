# Generated by Django 2.2b1 on 2019-03-31 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_myuser_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.DecimalField(decimal_places=0, max_digits=8),
        ),
    ]