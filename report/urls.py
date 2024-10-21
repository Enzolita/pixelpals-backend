from django.urls import path
from .views import ReportList, ReportDetail

urlpatterns = [
    path('report/', ReportList.as_view()),
    path('report/<int:pk>/', ReportDetail.as_view())
]
