from django.urls import path

from . import views
from django.conf.urls import url, include
urlpatterns = [

    path(r'', views.QuizIndexView.as_view(), name='index'),
    path('quiz/<int:pk>/', views.QuizDetailView.as_view(), name='detail'),]