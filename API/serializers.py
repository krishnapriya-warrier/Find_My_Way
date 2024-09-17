from rest_framework import serializers
from API.models import Jobs,Applications,Save_My_Job
from django.contrib.auth.models import User

class JobsSerializer(serializers.ModelSerializer):
    Created_by = serializers.PrimaryKeyRelatedField(read_only=True) 
    Created_at = serializers.DateTimeField(read_only=True)
    Updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Jobs
        fields = "__all__"

class ApplicationsSerializer(serializers.ModelSerializer):
    Applicant = serializers.PrimaryKeyRelatedField(read_only=True)
    Applied_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Applications
        fields = "__all__"

class SaveMyJobSerializer(serializers.ModelSerializer):
    Job = serializers.PrimaryKeyRelatedField(read_only = True)
    Applicant = serializers.PrimaryKeyRelatedField(read_only = True)
    Date = serializers.DateTimeField(read_only = True)
   
    class Meta:
        model = Save_My_Job
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = ["first_name","last_name","email","username","password"]

    def create(self,validated_data):
        return User.objects.create_user(**self.validated_data)
