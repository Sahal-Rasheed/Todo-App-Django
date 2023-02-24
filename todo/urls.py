from django.urls import path
from . import views

urlpatterns = [
    path('',views.todo_details ,name='todo_details'),
    path('add_todo/',views.add_todo ,name='add_todo'),
    path('delete_todo/<str:id>/',views.delete_todo ,name='delete_todo'),
    path('update_todo/<str:id>/',views.update_todo ,name='update_todo'),
    path('login/',views.userlogin ,name='login'),
    path('signup/',views.signup ,name='signup'),
    path('logout/',views.userlogout ,name='logout'),
    

]
