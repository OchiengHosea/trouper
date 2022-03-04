# Generated by Django 4.0.3 on 2022-03-03 00:47

import base.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.UUIDField(default=base.utils.get_uuid, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('full_name', models.CharField(max_length=225)),
                ('stage_name', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=13)),
                ('work_phone', models.CharField(max_length=13)),
                ('physical_address', models.CharField(max_length=125)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
