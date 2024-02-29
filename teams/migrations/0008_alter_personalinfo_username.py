# Generated by Django 5.0.1 on 2024-02-29 18:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_personalinfo_username_alter_schedules_hour'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='username_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
