from rest_framework import serializers
from .models import JobPost, Applicant

class JobPostSerializer(serializers.ModelSerializer):
    applicant_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = JobPost
        fields = [
            'id',
            'title',
            'description',
            'location',
            'created_at',
            'posted_by',
            'applicant_count'
        ]

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = [
            'id',
            'name',
            'email',
            'resume_link',
            'applied_job',
            'applied_at'
        ]
