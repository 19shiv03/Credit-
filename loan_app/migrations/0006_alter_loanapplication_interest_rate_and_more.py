# Generated by Django 4.2.6 on 2023-11-18 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_app', '0005_alter_loanapplication_interest_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='interest_rate',
            field=models.IntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='loan_amount',
            field=models.IntegerField(),
        ),
    ]
