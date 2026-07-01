from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import TemplateView


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('sentry-debug/', trigger_error),
    path(
        'lettings/',
        include(('lettings.urls', 'lettings'), namespace='lettings')
    ),
    path(
        'profiles/',
        include(('profiles.urls', 'profiles'), namespace='profiles')
    ),
    path('admin/', admin.site.urls),
]