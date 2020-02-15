from django.shortcuts import render

from django.db.models import Sum
from datetime import date, datetime

from objective.models import AnualObjective
from activity.models import Activity


def index(request):
    anual_objective_int = AnualObjective.objects.aggregate(Sum('objective'))['objective__sum'] #Objetivo anual em float
    total_distance = Activity.objects.aggregate(Sum('distance'))['distance__sum'] #Distância percorrida
    total_distance_decimal = float(total_distance) #Distância percorrida em float
    now = datetime.now() #Data atual
    year = date.today().year #Ano atual
    totalweekyear = date(year, 12, 31).isocalendar()[1] #Total de semanas do ano
    weeknumbernow = datetime.date(now).isocalendar()[1] #Semana atual
    debt = anual_objective_int - total_distance #Quanto falta pra alcançar o objetivo
    actualweekgoal = debt/(totalweekyear-weeknumbernow) #Objetivo semanal atual
    q = Activity.objects.filter(date__week=weeknumbernow) #Pega todas as atividades da semana atual
    actual_weekly_distance = q.aggregate(Sum('distance'))['distance__sum'] #Distância percorrida na semana atual
    weekly_balance = actualweekgoal - actual_weekly_distance #Comparação do quanto andou com o objetivo da semana

    context = {
        'anual_objective_int': anual_objective_int,
        'total_distance_decimal': total_distance_decimal,
        'debt': debt,
        'actualweekgoal': actualweekgoal,
        'actual_weekly_distance': actual_weekly_distance,
        'weekly_balance': weekly_balance,
        'weeknumbernow': weeknumbernow,
        'totalweekyear': totalweekyear
    }

    if AnualObjective.objects.filter(slug='1').exists():
        return render(request, 'home.html', context)
    else:
        return render(request, 'index.html', {})
