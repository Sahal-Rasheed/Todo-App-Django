# Generated by Django 4.1.4 on 2023-02-23 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0002_todolist_complete_alter_todolist_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=200)),
                ('status', models.CharField(choices=[('C', 'COMPLETED'), ('P', 'PENDING')], max_length=2)),
                ('complete', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]