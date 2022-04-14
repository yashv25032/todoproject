from django.urls import path
from .import views
urlpatterns = [
    path('',views.loginpage,name='login'),
    path('sign/',views.signuppage,name='sign'),
    path('logout/',views.loginpage,name='logout'),
    path('index/',views.home,name='home'),
    path('showtodo/',views.showtodo,name='show'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('change-status/<int:id>/<str:status>',views.changestatus,name='changestatus'),
]