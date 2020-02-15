from django.shortcuts import render
from django.db.models import Sum
from datetime import date, datetime

from objective.models import AnualObjective
from activity.models import Activity


def statistic(request):
    anual_objective = AnualObjective.objects.get(slug='1') #Pegar objetivo anual
    anual_objective_int = AnualObjective.objects.aggregate(Sum('objective'))['objective__sum'] #Objetivo anual em float
    total_activities =  Activity.objects.count() #Conta quantas atividades
    total_distance = Activity.objects.aggregate(Sum('distance'))['distance__sum'] #Distância percorrida
    total_distance_decimal = float(total_distance) #Distância percorrida em float
    now = datetime.now() #Data atual
    year = date.today().year #Ano atual
    totalweekyear = date(year, 12, 31).isocalendar()[1] #Total de semanas do ano
    weeknumbernow = datetime.date(now).isocalendar()[1] #Semana atual
    initialweekgoal = anual_objective_int/totalweekyear #Objetivo semanal inicial
    debt = anual_objective_int - total_distance #Quanto falta pra alcançar o objetivo
    actualweekgoal = debt/(totalweekyear-weeknumbernow) #Objetivo semanal atual
    deficit = total_distance_decimal - (weeknumbernow * initialweekgoal) #Quanto está abaixo do que já deveria ter percorrido
    q = Activity.objects.filter(date__week=weeknumbernow) #Pega todas as atividades da semana atual
    number_week_activity = q.count() #Conta quantas atividades na semana atual
    actual_weekly_distance = q.aggregate(Sum('distance'))['distance__sum'] #Distância percorrida na semana atual
    weekly_balance = actualweekgoal - actual_weekly_distance #Comparação do quanto andou com o objetivo da semana
    excess = total_distance_decimal - anual_objective_int

    context = {
        'anual_objective_int': anual_objective_int,
        'initialweekgoal': initialweekgoal,
        'total_distance': total_distance,
        'deficit': deficit,
        'excess': excess,
        'debt': debt,
        'actualweekgoal': actualweekgoal,
        'actual_weekly_distance': actual_weekly_distance,
        'weekly_balance': weekly_balance,
        'year': year,
    }
    return render(request, 'statistic/index.html', context)


#def jan(request):
#    month = "Janeiro"
#    activities = Activity.objects.filter(date__month=1)
#    return render(request, 'statistic/detail.html', {'activities':activities, 'month':month})
