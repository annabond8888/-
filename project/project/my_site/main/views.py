import random
import json


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from main.forms import RegistrationForm, LoginForm
from main.models import Exercise, Question, Choice, Word, Answer, TQuestion


def logout_view(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'main/registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'main/login.html', {'form': form, 'error': 'Неверное имя пользователя или пароль.'})
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def index(request):
    return render(request, "main/index.html")

def home(request):
    return render(request, "main/home.html")

def help(request):
    return render(request, "main/help.html")

def abo(request):
    return render(request, "main/about.html")

def map(request):
    return render(request, "main/map.html")
def games(request):
    return render(request, "main/games.html")
def login1(request):
    return render(request, "main/login.html")


def fill_the_gaps(request):
    exercises = Exercise.objects.all()
    context = {
        'exercises': exercises,
    }
    return render(request, 'main/fill_the_gaps.html', context)


def check_answer(request):
    if request.method == 'POST':
        user_answer = request.POST.get('answer')
        correct_answer = request.POST.get('correct_answer')

        if user_answer.lower().strip() == correct_answer.lower():
            message = "Верно!"
        else:
            message = f"Неверно!"

        return HttpResponseRedirect(reverse('result_page', args=[message]))
    else:
        return HttpResponseRedirect(reverse('home'))




def questions(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'main/questions.html', context)


def check_choice(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            selected_choice_id = int(data.get('choice'))
        except (json.JSONDecodeError, TypeError, ValueError):
            return JsonResponse({'error': 'Incorrect data format'}, status=400)

        try:
            selected_choice = Choice.objects.get(id=selected_choice_id)
        except Choice.DoesNotExist:
            return JsonResponse({'error': 'No response'}, status=400)

        if selected_choice.is_correct:
            message = "Верно!"
        else:
            correct_choice = selected_choice.question.choice_set.filter(is_correct=True).first()
            if correct_choice:
                message = f"Неверно!"
            else:
                message = "Неверно!"

        return JsonResponse({'message': message})
    else:
        return HttpResponseRedirect('/questions/')


def flashcards(request):
    words = Word.objects.all()
    context = {'words': words}
    return render(request, 'main/flashcards.html', context)


@login_required
def test_view(request):
    questions = TQuestion.objects.all().order_by('?')[:15]
    context = {'questions': questions}
    return render(request, 'main/test.html', context)


@login_required
def submit_answers(request):
    if request.method == 'POST':
        score = 0
        total_questions = len(request.POST.keys()) - 1

        for key, value in request.POST.items():
            if key.startswith('q_'):
                question_id = int(key.split('_')[1])
                correct_answer = Answer.objects.filter(question_id=question_id, is_correct=True).first()

                if str(correct_answer.id) == value:
                    score += 1

        result = f'You scored {score} out of {total_questions}'
        return HttpResponseRedirect(f'/result/{result}')

    return redirect('/entertest')


def result_view(request, result):
    context = {'result': result}
    return render(request, 'main/result.html', context)