# Generated by Django 5.1.6 on 2025-02-11 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_question_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_word', models.CharField(max_length=100)),
                ('russian_translation', models.CharField(max_length=100)),
            ],
        ),
    ]
