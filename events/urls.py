from django.urls import path
from . import views

app_name = 'events'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new', views.CreateView.as_view(), name='create'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
    path('descending/', views.DescendingView.as_view(), name='descending'),
    path('search_results/', views.DescriptionSearchView.as_view(), name='search_results'),
    path('chart', views. ChartView, name='chart'),
]