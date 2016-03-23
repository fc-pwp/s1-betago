from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=200)


class Question(models.Model):
    content = models.TextField(max_length=500)
    quiz = models.ForeignKey(Quiz)
    order = models.SmallIntegerField(default=1)


class Answer(models.Model):
    content = models.CharField(max_length=200)
    score = models.SmallIntegerField(default=0)
    order = models.SmallIntegerField(default=1)
    question = models.ForeignKey(Question)


class UserResult(models.Model):
    _genders = (
        ['M', 'Male',],
        ['F', 'Female',],
    )
    name = models.CharField(max_length=200)
    scores = models.IntegerField(default=0)
    quiz = models.ForeignKey(Quiz)
    gender = models.CharField(max_length=1, choices=_genders)
    age = models.SmallIntegerField(default=20)
    created_at = models.DateTimeField(auto_now_add=True)


class QuizResult(models.Model):
    quiz = models.ForeignKey(Quiz)
    min_scores = models.IntegerField()
    max_scores = models.IntegerField()
    image = models.ImageField()
    text = models.TextField()

