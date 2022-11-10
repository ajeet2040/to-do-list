# Generated by Django 4.1.3 on 2022-11-10 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
