from django.urls import path
from .views import JobPostListCreateView, JobPostSortedListView, ApplicantCreateView

urlpatterns = [
    path('jobs/', JobPostListCreateView.as_view(), name='jobs-list-create'),
    path('jobs/sorted/', JobPostSortedListView.as_view(), name='jobs-sorted-list'),
    path('jobs/apply/', ApplicantCreateView.as_view(), name='apply-job'),
]
