# Generated by Django 3.1.7 on 2021-04-06 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionaryapp', '0002_auto_20210406_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dictionary',
            name='id',
        ),
        migrations.RemoveField(
            model_name='superuser',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='dictionary',
            name='dictId',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='superuser',
            name='superUserId',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='user',
            name='userId',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
