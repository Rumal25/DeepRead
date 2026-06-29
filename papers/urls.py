from django.urls import path
from papers import views

app_name = 'papers'

urlpatterns = [
    path('', views.paper_list, name='paper_list'),
    path('<int:pk>/', views.paper_detail, name='paper_detail'),
    path('new/', views.paper_form, name='paper_form'),
]