# Generated by Django 5.0.1 on 2024-02-19 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_contact_map'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeCroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_group', models.CharField(choices=[('U6', 'U6'), ('U7', 'U7'), ('U8', 'U8'), ('U9', 'U9'), ('U10', 'U10'), ('U11', 'U11')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('week_day', models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], max_length=20)),
                ('hour', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos/')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='logo',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.agecroups')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.images')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.schedules')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.videos')),
            ],
        ),
    ]
