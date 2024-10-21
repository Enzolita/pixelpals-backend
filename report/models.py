from django.db import models
from django.contrib.auth.models import User


class Report(models.Model):
    """
    Represents a report entry submitted by a user.
    Each report has a submitter, reason, content, status,
    and timestamps for creation and last update.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
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
        return f'{self.owner} : {self.reason}'
