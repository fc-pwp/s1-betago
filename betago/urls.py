from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from quiz import views as quiz_views


urlpatterns = [
    url(
        r'^quiz/(?P<pk>[0-9]+)/q(?P<order>[1-5]{1})/$',
        quiz_views.question_view, name='question_view',
    ),
    url(
        r'^quiz/(?P<pk>[0-9]+)/result/$',
        quiz_views.quiz_result, name='quiz_result',
    ),
    url(
        r'^quiz/(?P<pk>[0-9]+)/start/$',
        quiz_views.quiz_start, name='quiz_start'
    ),
    url(r'^main/$', quiz_views.quiz_list, name='main'),
    url(r'^admin/', admin.site.urls),
    url(r'^ajax_test/$', quiz_views.ajax_test),
    url('', include('social.apps.django_app.urls', namespace='social')),
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

