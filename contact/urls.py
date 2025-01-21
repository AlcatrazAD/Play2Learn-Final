from django.urls import path

from .views import ContactView, ContactThanksView

app_name = 'contact'
urlpatterns = [
    path('contact-app/', ContactView.as_view(), name='app'),
    path('contact-app/thanks/', ContactThanksView.as_view(), name='thanks'),
]