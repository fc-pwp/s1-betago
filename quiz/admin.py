from django.contrib import admin

from .models import Quiz
from .models import Question
from .models import Answer
from .models import UserResult
from .models import QuizResult


admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserResult)
admin.site.register(QuizResult)

