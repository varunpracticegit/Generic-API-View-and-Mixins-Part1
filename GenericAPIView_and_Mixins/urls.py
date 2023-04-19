from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stulist/', views.StudentList.as_view()),
    path('stucreate/', views.StudentCreate.as_view()),
    path('stulist/<int:pk>/', views.StudentRetrieve.as_view()),
    path('stupdate/<int:pk>/', views.StudentUpdate.as_view()),
    path('studestroy/<int:pk>/', views.StudentDestroy.as_view()),
    # path('studentapi/<int:pk>', views.StudentAPI.as_view()), 
]
