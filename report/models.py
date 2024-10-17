# Customized to cater for report management functionality.
# This module defines the Report model used to store information about 
# reports submitted by users. It includes fields for the report submitter, 
# reason, content and timestamps for creation and updates.

from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    """
    Represents a report entry submitted by a user. 
    Each report has a submitter, reason, content, status,
    and timestamps for creation and last update.
    """
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        """
        Returns a string representation of the report, combining 
        the submitter's username, reason, and status.
        """
        return f'{self.submitter} : {self.reason}'