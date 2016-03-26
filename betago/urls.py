from django.conf.urls import url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from quiz import views as quiz_views


urlpatterns = [
    url(r'^main/$', quiz_views.quiz_list, name='main'),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

