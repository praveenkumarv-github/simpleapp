from django.http import JsonResponse
import random
import string
from django.shortcuts import render
from datetime import datetime
import pytz


def generate_password(request):
    pass_len = int(request.GET.get('length', 8))  # Default length is 8 if not provided
    count = 0
    passw1 = []

    while True:
        count += 1
        if count > pass_len:
            break
        small_alfa = random.choice(string.ascii_lowercase)
        caps_alfa = random.choice(string.ascii_uppercase)
        numeric = random.choice(string.digits)
        spl_char = random.choice(string.punctuation)
        var = (small_alfa, caps_alfa, numeric, spl_char)
        var01 = random.choice(var)
        passw1.append(var01)

    psswd = ''.join(passw1)
    return JsonResponse({'password': psswd})

def index(request):
    return render(request, 'password_generator_app/index.html')

def health_check(request):
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
    return JsonResponse({'status': 'ok', 'current_time': current_time})