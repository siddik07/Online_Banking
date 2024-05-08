# Generated by Django 4.2.6 on 2024-05-06 06:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_details_acc_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction_history',
            old_name='from_account',
            new_name='from_account_user',
        ),
        migrations.RenameField(
            model_name='transaction_history',
            old_name='to_account',
            new_name='to_account_user',
        ),
        migrations.AddField(
            model_name='transaction_history',
            name='from_account_no',
            field=models.BigIntegerField(db_index=True, default=0, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999999)]),
        ),
        migrations.AddField(
            model_name='transaction_history',
            name='to_account_no',
            field=models.BigIntegerField(db_index=True, default=0, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999999)]),
        ),
    ]
