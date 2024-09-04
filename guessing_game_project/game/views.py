# game/views.py
import random
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def guess_number(request):
    if request.method == 'POST':
        user_guess = int(request.POST.get('guess', '0'))
        random_number = random.randint(1, 10)
        if user_guess == random_number:
            return render(request, 'result.html', {'result': '正解！', 'number': random_number})
        else:
            return render(request, 'result.html', {'result': '不正解。', 'number': random_number})
    return render(request, 'home.html')
