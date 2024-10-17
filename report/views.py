# Customized to cater for report management functionality. This module
# defines the views for the Report model. It includes views for listing
# and creating reports, as well as retrieving, updating, and deleting
# individual report instances.

from rest_framework import generics, permissions
from .models import Report
from .serializers import ReportSerializer
from pixelpals_backend.permissions import IsOwnerOrReadOnly

class ReportList(generics.ListCreateAPIView):
    """
    List reports or create a report if logged in.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Saves the new report instance with the owner set to the current user.
        """
        serializer.save(owner=self.request.user)

class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a report.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsOwnerOrReadOnly]