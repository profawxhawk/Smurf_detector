from predictor import views as predictor_views
from django.urls import path,include
urlpatterns = [ 
    # path('rainbow',predictor_views.Rainbow_handler,name='Rainbow'),
    # path('codeforces',predictor_views.codeforces_handler,name='Codeforces'),
    path('',predictor_views.selector, name='selector'),
    path('/',predictor_views.selector, name='selector'),
    path('/R6',predictor_views.r6_result,name='r6result')
]
