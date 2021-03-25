from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cats/', views.cats_index, name='cats'),
    path('cats/<int:cat_id>/', views.cats_show, name='cats_show'),
    path('cats/create/', views.cats_new, name='cats_create'),
    path('cats/<int:pk>/update/', views.cats_update, name='cats_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
    path('cats/<int:pk>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('accounts/signup', views.sign_up, name='sign_up'),

]
