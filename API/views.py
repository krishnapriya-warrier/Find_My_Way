from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet,ModelViewSet
from django.contrib.auth.models import User
from API.serializers import JobsSerializer,ApplicationsSerializer,SaveMyJobSerializer,UserSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from API.models import Jobs,Applications,Save_My_Job
from rest_framework.decorators import action

class JobsView(ModelViewSet):
    serializer_class = JobsSerializer
    queryset = Jobs.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(Created_by=self.request.user) 

class ApplicationsView(ModelViewSet):
    serializer_class = ApplicationsSerializer
    queryset = Applications.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(Applicant=self.request.user)

class SaveMyJobView(ModelViewSet):
    serializer_class = SaveMyJobSerializer
    queryset = Save_My_Job.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(Applicant=self.request.user)

    @action(methods=["POST"],detail=True)
    def add_to_saved_jobs(self,request,*args,**kw):
        id = kw.get('pk')
        applicant = request.User
        job = Jobs.objects.get(id=id)
        Save_My_Job.objects.create(Job=job,Applicant=applicant)
        return Response(data="Job successfully added to Saved Jobs")

class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]




