from django.urls import path
from . import views

app_name = "crud"
urlpatterns = [
    path("", views.create_view, name="create_view"),
    path("list/",views.ListView.as_view(),name="listar"),
    path('<pk>/', views.DetailView.as_view()),
    path('delete/<pk>',views.DeleteView.as_view(), name="delete_view")
]
