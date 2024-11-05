from django.urls import path
from movie.api.views import (AdminReportListView, AdminReportApprove, AdminReportReject, AdminReportStatusView) 

urlpatterns = [
    # Admin Report View URL/ Endpoints
    path('admin-report/', AdminReportListView.as_view(), name='admin-report'),
    path('report-approve/<int:pk>/', AdminReportApprove.as_view(), name='admin-report-approve'),
    path('report-reject/<int:pk>/', AdminReportReject.as_view(), name='admin-report-reject'),
    path('report-status/', AdminReportStatusView.as_view(), name='admin-report-status'),
]
