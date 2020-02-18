from . import views
from django.contrib import admin
from django.urls import path,include
app_name = 'portfolio'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about, name="about" ),
    path('experience/',views.experience, name="experience" ),
    path('education/',views.education, name="education" ),
    path('skills/',views.skills, name="skills" ),
    path('languages/',views.languages, name="languages" ),
    path('certification',views.certification, name="certification" ),
    ]

