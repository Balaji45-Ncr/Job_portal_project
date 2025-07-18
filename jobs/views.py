from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import JobPost, Applicant
from .throttles import EmailPerDayThrottle
from .serializer import JobPostSerializer, ApplicantSerializer
from django.db.models import Count
from rest_framework.exceptions import Throttled

class JobPostListCreateView(generics.ListCreateAPIView):
    serializer_class =  JobPostSerializer

    def get_queryset(self):
        return JobPost.objects.annotate(applicant_count=Count('applicants'))

class JobPostSortedListView(generics.ListAPIView):
    serializer_class = JobPostSerializer

    def get_queryset(self):
        return JobPost.objects.annotate(
            applicant_count=Count('applicants')
        ).order_by('-applicant_count')

class ApplicantCreateView(generics.CreateAPIView):
    serializer_class = ApplicantSerializer
    throttle_classes = [EmailPerDayThrottle]

    def throttled(self, request, wait):
        raise Throttled(detail={
            "error": "Rate limit exceeded. Max 3 applications per day for this email."
        })
