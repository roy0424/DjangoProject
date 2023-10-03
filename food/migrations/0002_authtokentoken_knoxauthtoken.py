# Generated by Django 4.2.4 on 2023-08-29 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthtokenToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'authtoken_token',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KnoxAuthtoken',
            fields=[
                ('digest', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('created', models.DateTimeField()),
                ('expiry', models.DateTimeField(blank=True, null=True)),
                ('token_key', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'knox_authtoken',
                'managed': False,
            },
        ),
    ]
