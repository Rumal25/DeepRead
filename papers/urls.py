from django.urls import path
from papers import views

app_name = 'papers'

urlpatterns = [
    # Papers
    path('', views.paper_list, name='paper_list'),
    path('<int:pk>/', views.paper_detail, name='paper_detail'),
    path('new/', views.paper_form, name='paper_form'),
    path('<int:pk>/edit/', views.paper_form, name='paper_edit'),
    path('<int:pk>/delete/', views.paper_delete, name='paper_delete'),

    # Notes
    path('<int:paper_pk>/notes/add/', views.note_add, name='note_add'),
    path('notes/<int:pk>/delete/', views.note_delete, name='note_delete'),

    # Experiments
    path('<int:paper_pk>/experiments/add/', views.experiment_add, name='experiment_add'),
    path('experiments/<int:pk>/delete/', views.experiment_delete, name='experiment_delete'),

    # Authors
    path('authors/', views.author_list, name='author_list'),
    path('authors/new/', views.author_form, name='author_form'),
    path('authors/<int:pk>/edit/', views.author_form, name='author_edit'),

    # Topics
    path('topics/', views.topic_list, name='topic_list'),
    path('topics/new/', views.topic_form, name='topic_form'),
    path('topics/<int:pk>/edit/', views.topic_form, name='topic_edit'),
]