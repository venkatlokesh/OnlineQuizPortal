from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Quiz,Question,Option
# Create your views here.

class QuizIndexView(generic.ListView):
    template_name = 'Quiz/home.html'
    context_object_name = 'quiz_list'

    def get_queryset(self):
        print( Quiz.objects.all())
        return Quiz.objects.all()


class QuizDetailView(generic.DetailView):
    model = Quiz
    template_name = 'Quiz/quiz.html'
