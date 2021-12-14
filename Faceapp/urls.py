from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from Faceapp import views
from django.conf.urls.static import static
from django.conf import settings

appname = 'Faceapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('predictImage', views.predictImage, name='predictImage'),
    path('mood_calendar/', views.mood_calendar, name='mood_calendar'),
    # path('chart/', views.chart, name='chart'),
    # path('mood_notes/', views.mood_notes, name='mood_notes'),
    path('note/', views.note, name='note'),
    path('mypage/', views.mypage, name='mypage'),



    # path('viewDataBase', views.viewDataBase, name='viewDataBase'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)