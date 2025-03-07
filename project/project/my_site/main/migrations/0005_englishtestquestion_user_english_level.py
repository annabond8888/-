# Generated by Django 5.1.6 on 2025-02-13 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_word'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnglishTestQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
                ('difficulty', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='english_level',
            field=models.CharField(choices=[('A1', 'Beginner'), ('A2', 'Elementary'), ('B1', 'Intermediate'), ('B2', 'Upper Intermediate'), ('C1', 'Advanced'), ('C2', 'Proficiency')], default='A1', max_length=2),
        ),
    ]
