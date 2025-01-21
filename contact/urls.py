from django.urls import path

from .views import ContactView, ContactThanksView

app_name = 'jobs'
urlpatterns = [
    path('job-app/', ContactView.as_view(), name='app'),
    path('job-app/thanks/', ContactThanksView.as_view(), name='thanks'),
]