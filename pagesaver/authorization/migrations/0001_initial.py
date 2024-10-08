# Generated by Django 5.0.7 on 2024-08-12 05:28

from django.db import migrations, models

import pagesaver.authorization.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('expired', models.DateTimeField(default=pagesaver.authorization.models._default_expire_time, verbose_name='token expire time')),
                ('token', models.TextField(blank=True, verbose_name='token')),
            ],
            options={
                'verbose_name': 'api token',
                'verbose_name_plural': 'api token',
                'db_table': 'api_token',
            },
        ),
    ]
