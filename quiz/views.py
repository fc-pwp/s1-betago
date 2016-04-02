from django.http import Http404
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Answer
from .models import QuizResult
from .models import Quiz
from .models import UserResult
from .forms import UserResultForm
from .forms import AnswerForm


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
            new_user_result.save()
            request.session['user_result_pk'] = new_user_result.pk
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

    question = qs[0]  # or `qs.first()`

    session_key_name = 'quiz{}_question'.format(quiz.pk)

    if session_key_name not in request.session:
        request.session[session_key_name] = 0
        return redirect('quiz_start', pk=quiz.pk)
    else:
        if request.session[session_key_name] + 1 > question.order:
            return redirect(
                'question_view',
                pk=quiz.pk,
                order=question.order+1
            )

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            if request.session[session_key_name] == question.order:
                return redirect(
                    'question_view',
                    pk=quiz.pk,
                    order=question.order+1
                )
            user_result_pk = request.session['user_result_pk']
            user_result = get_object_or_404(UserResult, pk=user_result_pk)
            answer = get_object_or_404(
                Answer,
                question=question,
                order=form.cleaned_data['order']
            )
            user_result.scores += answer.score
            user_result.save()
            request.session[session_key_name] = question.order

            last_question = quiz.question_set.order_by('-order').first()
            if question.order < last_question.order:
                return redirect(
                    'question_view',
                    pk=quiz.pk,
                    order=question.order+1
                )
            else:
                return redirect('quiz_result', pk=quiz.pk)

    elif request.method == 'GET':
        form = AnswerForm()

    ctx = {
        'form': form,
        'question': question,
    }

    return render(request, 'question_view.html', ctx)


def quiz_result(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    user_result_pk = request.session['user_result_pk']
    user_result = get_object_or_404(UserResult, pk=user_result_pk)

    scores = user_result.scores

    qr_qs = QuizResult.objects.filter(
        quiz=quiz,
        min_scores__gte=scores,
        max_scores__lte=scores,
    )
    if qr_qs.exists():
        raise Exception('으앙 없는 결과...')

    ctx = {
        'quiz_result': qr_qs.first(),
    }
    return render(request, 'quiz_result.html', ctx)

