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

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title is required.")
        if len(value) > 255:
            raise serializers.ValidationError("Title is too long (max 255).")
        return value

    def validate_description(self, value):
        if not value:
            raise serializers.ValidationError("Description is required.")
        if len(value) < 10:
            raise serializers.ValidationError("Description too short (min 10 characters).")
        return value

    def validate_location(self, value):
        if not value:
            raise serializers.ValidationError("Location is required.")
        return value

    def validate_posted_by(self, value):
        if not value:
            raise serializers.ValidationError("Posted by is required.")
        return value

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

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name is required.")
        if len(value) > 255:
            raise serializers.ValidationError("Name is too long (max 255).")
        return value

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required.")
        return value

    def validate_resume_link(self, value):
        if not value:
            raise serializers.ValidationError("Resume link is required.")
        if not value.startswith("http"):
            raise serializers.ValidationError("Resume link must be a valid URL.")
        return value

    def validate(self, data):
        if not data.get('applied_job'):
            raise serializers.ValidationError({"applied_job": "Applied job is required."})
        return data