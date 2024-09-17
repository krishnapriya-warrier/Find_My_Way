from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Jobs(models.Model):
    
    Role=models.CharField(max_length=255)
    Company_Name = models.CharField(max_length=255)
    Job_Location = models.CharField(max_length=255)
    Salary = models.PositiveIntegerField()
    Experience = models.PositiveIntegerField()
    Is_Active = models.BooleanField(default=True)
    Created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True) 
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Role
    
class Applications(models.Model):
    Job = models.ForeignKey(Jobs,on_delete=models.CASCADE)
    Applicant = models.ForeignKey(User,on_delete=models.CASCADE)
    Resume = models.FileField(upload_to='Resumes',null=True)
    Applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.Applicant.username}" applied for {self.Job.Role}'
    
class Save_My_Job(models.Model):
    Job = models.ForeignKey(Jobs,on_delete=models.CASCADE)
    Applicant = models.ForeignKey(User,on_delete=models.CASCADE)
    Date = models.DateTimeField(auto_now_add=True)
