# Generated by Django 4.1.7 on 2023-04-16 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_accounts_options_accounts_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='updated_at',
        ),
    ]