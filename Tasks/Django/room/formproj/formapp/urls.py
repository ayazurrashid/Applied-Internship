from django.urls import path
from . import views
app_name = 'formapp'
urlpatterns = [
    path('', views.get_name, name='index'),
    path('show', views.show, name='show'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('search', views.search, name='search'),
    
]