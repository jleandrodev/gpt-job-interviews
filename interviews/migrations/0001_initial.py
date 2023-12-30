# Generated by Django 5.0 on 2023-12-30 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobs', '0002_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('uuid', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(editable=False, max_length=100)),
                ('completed', models.BooleanField(default=False)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats', to='jobs.job')),
            ],
        ),
    ]