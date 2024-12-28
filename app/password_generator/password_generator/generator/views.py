from django.shortcuts import render
import random
import string

def generate_password(length):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def index(request):
    password = ''
    if request.method == 'POST':
        pass_len = int(request.POST['pass_len'])
        password = generate_password(pass_len)
    return render(request, 'index.html', {'password': password})