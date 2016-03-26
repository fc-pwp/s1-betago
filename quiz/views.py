from django.shortcuts import render

from .models import Quiz


def quiz_list(request):
    object_list = Quiz.objects.order_by('?')
    ctx = {
        'object_list': object_list,
    }
    return render(request, 'quiz_list.html', ctx)

