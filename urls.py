from django.urls import include, path
from . import views

app_name = 'betpolls'

urlpatterns = [
    path('accounts/login/', views.loginPage,name="login"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerPage,name="register"),
    path('', views.index, name = 'index'),
    path('<int:match_id>/', views.detail, name='detail'),
    path('<int:match_id>/results/', views.results, name='results'),
    path('<int:match_id>/vote/', views.vote, name='vote'),
    path('get-matches/<int:league_id>/', views.get_matches, name='get_matches'),
]