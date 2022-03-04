from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('facerec/', views.facerec, name='face'),
    path('lion/',views.lion, name='lion')
]