from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView
)

from app import models
# Create your views here.

class Index(ListView):
    model = models.Question
    template_name = 'app/index.html'  # By default context_object_name in ListView is 'lowercase model name underscore list', here 'question_list'

class Question(DetailView):
    model = models.Question
    template_name = 'app/question.html'

