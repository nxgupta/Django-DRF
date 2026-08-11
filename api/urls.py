from django.urls import path, include
from . import views
from blogs.views import BlogsView, CommentsView, BlogDetailView, CommentDetailView
from rest_framework import routers

router= routers.SimpleRouter()

router.register('employees', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('students/', views.studentView ),
    path('students/<int:id>/', views.studentDetailView),
    # path('employees/', views.Employees.as_view()),
    # path('employee/<int:id>', views.EmployeeDetail.as_view()),
    path('blogs/', BlogsView.as_view()),
    path('blogs/<int:id>', BlogDetailView.as_view() ),
    path('comments/', CommentsView.as_view()),
    path('comments/<int:id>', CommentDetailView.as_view()),
    path('', include(router.urls))
]
