from reporter import views as reporter_views
from django.urls import path,include
urlpatterns = [ 
    path('rainbow',reporter_views.Rainbow_handler,name='Rainbow'),
]
