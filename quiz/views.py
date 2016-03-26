from django.http import Http404
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Quiz
from .forms import UserResultForm


def quiz_list(request):
    object_list = Quiz.objects.order_by('?')
    ctx = {
        'object_list': object_list,
    }
    return render(request, 'quiz_list.html', ctx)


def quiz_start(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)

    if request.method == 'GET':
        form = UserResultForm()
    elif request.method == 'POST':
        form = UserResultForm(request.POST)
        if form.is_valid():
            new_user_result = form.save(commit=False)
            new_user_result.quiz = quiz
            return redirect('question_view', pk=quiz.pk, order=1)

    ctx = {
        'form': form,
        'quiz': quiz,
    }
    return render(request, 'quiz_start.html', ctx)


def question_view(request, pk, order):
    quiz = get_object_or_404(Quiz, pk=pk)

    qs = quiz.question_set.filter(order=order)
    if not qs.exists():
        raise Http404

    ctx = {
        'question': qs[0],  # or `qs.first()`
    }

    return render(request, 'question_view.html', ctx)

