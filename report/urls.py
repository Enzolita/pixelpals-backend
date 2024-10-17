# Customized to cater for report management functionality. This module
# defines the URL patterns for the Report app. It includes paths for
# listing, creating, retrieving, updating, and deleting reports.

from django.urls import path
from .views import ReportList, ReportDetail

urlpatterns = [
    path('', ReportList.as_view()),
    path('report/<int:pk>/', ReportDetail.as_view())
]