from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='request_list'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='request_edit'),  # new
    path('<int:pk>/', views.PostDetailView.as_view(), name='request_detail'),  # new
    path('<int:pk>/delete/',
         views.PostDeleteView.as_view(), name='request_delete'),
    path('new/', views.PostCreateView.as_view(), name='request_new'),
]
