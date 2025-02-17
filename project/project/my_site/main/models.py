from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='группы',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="main_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='specific permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="main_user_set",
        related_query_name="user",
    )

    ENGLISH_LEVEL_CHOICES = (
        ('A1', 'Beginner'),
        ('A2', 'Elementary'),
        ('B1', 'Intermediate'),
        ('B2', 'Upper Intermediate'),
        ('C1', 'Advanced'),
        ('C2', 'Proficiency'),
    )

    english_level = models.CharField(max_length=2, choices=ENGLISH_LEVEL_CHOICES, default='A1')

class Exercise(models.Model):
    title = models.CharField(max_length=100)
    sentence = models.TextField()
    answer = models.TextField()


class TQuestion(models.Model):
    question_text = models.CharField(max_length=255)
    level = models.IntegerField(default=1)  # Уровень сложности вопроса от 1 до 5

class Answer(models.Model):
    question = models.ForeignKey(TQuestion, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)
    is_correct = models.BooleanField()

class Question(models.Model):
    question_text = models.CharField(max_length=200)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)


class Word(models.Model):
    english_word = models.CharField(max_length=100)
    russian_translation = models.CharField(max_length=100)

    def __str__(self):
        return self.english_word