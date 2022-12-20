
from django.urls import path,include
from . import views

app_name='todo_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('cancel',views.cancel,name='cancel'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:f_id>/',views.update,name='update'),
    path('cancel',views.cancel1,name='cancel'),
    path('generic_list/',views.generic_list.as_view(),name='generic_list'),
    path('generic_detial/<int:pk>/',views.generic_detial.as_view(),name='generic_detial'),
    # path('classupdate/<int:pk>/',views.generic_update.as_view(),name='classupdate')

]
