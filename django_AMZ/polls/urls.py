from django.urls import path, include

from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('best_seller/', views.StockRecordsListView.as_view(), name='best_seller'),
    #path('best_seller/', views.simple_view, name='simple_url_view'),
    path('table/', views.table_server_side, name="table_server_side"),
    path('data/', views.Data.as_view()), 
]

