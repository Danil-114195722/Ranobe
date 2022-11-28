from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponseRedirect

from .models import Persons


# Create your views here.

def input_data_about_user(request):
    # словарь с ключом о существовании почты в БД (exist_email) и ключом верных данных (correct_add)
    data_keys = {
        'exist_email': False,
        'correct_add': False,
    }

    if request.method == 'POST':
        # переменные с данными из словаря POST
        email_post = request.POST.get('email')
        name_post = request.POST.get('name')
        # проверка на уникальность данных
        try:
            # создание экземпляра класса по введённым данным и его запись в БД
            Persons.objects.create(email=email_post, name=name_post)
            data_keys['correct_add'] = True
            request.method = None
        except IntegrityError:
            # если в БД уже существует введённая почта или логин
            data_keys['exist_email'] = True
            request.method = None
            return render(request, 'authorization/authorization.html', data_keys)

    return HttpResponseRedirect
# I see you
# check
# я тута был
# ⣇⢸⢸⣿⡿⢸⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⢂⡇⡟⢼⠟⠁⠄⠄⠄⠄⠄⠄
# ⠄⠻⣌⢼⢻⣷⡧⣣⣝⢿⣿⣿⡙⠛⣿⣿⡿⢋⡼⣱⡇⠳⡄⠄⠄⠄⠄⠄⠄⠄
# ⠄⠄⠈⠻⡉⣿⣿⡨⠙⠳⠭⣛⡿⠿⠿⣋⡴⢏⢁⡿⣱⣶⣱⣶⣷⣶⣄⠄⠄⠄
# ⠄⠄⠄⣀⣑⡫⡻⢇⢤⣶⣿⣿⡹⣷⣿⣮⡶⡫⢼⣱⣿⣿⣿⣿⣿⣿⣿⡄⠄⠄
# ⠄⣴⣿⣿⣿⣇⢮⣬⣊⡻⣿⣿⣿⡿⠷⢿⣊⣪⣿⣿⣿⣿⣇⠘⣸⣿⣿⣷⠄⠄
# ⠄⣿⣿⣿⣿⣿⣎⡻⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⣿⣿⣿⣿⠄⠄
# ⠄⣿⣿⣿⣿⡿⣿⣿⠿⣿⣿⣿⣿⡛⣿⣿⠟⣿⣿⣿⣿⣿⣿⣿⣦⡙⢿⡏⠄⠄
# ⠄⣿⣿⣿⣿⣿⡄⢃⣾⣿⣿⣿⣿⣿⣦⣌⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡁⠄⠄
# ⠄⠸⣿⣿⣿⣿⡟⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⡌⣿⣿⣿⣿⣿⡿⢛⣛⣛⢿⣷⠄
# ⠄⠄⢻⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⢻⣿⣿⣿⢸⣿⠛⣿⡇⣿⡇
# ⠄⠄⠈⣿⣿⣿⡇⣿⣿⣿⣿⢋⣶⣶⣦⡙⣿⣿⣿⣦⡹⣿⣿⣌⠻⠿⠿⢃⣿⡇
# ⠄⠄⠄⢻⣿⣿⡇⢿⣿⣿⣿⠸⣿⣤⣿⠇⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⠁
# ⠄⠄⠄⠈⢿⣿⣷⡸⣿⣿⣿⣷⣭⣭⣵⣾⣿⣿⣿⣿⡇⢿⣿⣿⣿⣿⠿⣋⣵⠁
# ⠄⠄⠄⠄⠘⣿⣿⣧⣝⢻⣿⣿⣿⣿⣿⣿⣿⣿⠿⢛⣼⣶⣬⣭⣭⡤⠖⣛⡉⣿
#   ⠄⠄⢀⢻⣿⢟⣥⣶⣬⣭⣛⣛⣛⣛⣭⣥⣾⣿⡿⠿⢛⣯⡅⢰⡆⣿⣷
