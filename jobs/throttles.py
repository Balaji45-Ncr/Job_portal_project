from rest_framework.throttling import BaseThrottle
from django.utils import timezone
from .models import Applicant

class EmailPerDayThrottle(BaseThrottle):
    """
    Allows max 3 applications per email per day.
    """

    def allow_request(self, request, view):

        if request.method != 'POST':
            return True

        email = request.data.get('email')
        if not email:
            return False

        today = timezone.now().date()

        count = Applicant.objects.filter(
            email=email,
            applied_at__date=today
        ).count()

        return count < 3
