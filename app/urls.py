from django.urls import path
from app import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('question/<slug>', views.Question.as_view(), name='question')
]