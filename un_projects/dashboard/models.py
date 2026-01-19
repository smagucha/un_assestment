from django.db import models

class RemoteStatus(models.TextChoices):
        Yes = 'Yes', 'yes'
        NO = 'NO', 'NO'

class Softwareepertiseleve(models.TextChoices):
    beginner = 'beginner', 'beginner'
    intermediate = 'intermediate', 'intermediate'
    advanced = 'advance', 'advance'

class LevelOfresponsibility(models.TextChoices):
    admin= 'admin', 'admin'
    staffmember = 'staffmember', 'staffmember'
    management = 'management', 'management'

class HighestLevelofeducation(models.TextChoices):
    certificate= 'certificate', 'certificate'
    diploma = 'diploma', 'diploma'
    degree = 'degree', 'degree'
    master = 'master', 'master'
    phd = 'phd', 'phd'

class Staff_Member(models.Model):
    INdexNumber = models.CharField(max_length=250, null=False)
    FullNames = models.CharField(max_length=250, null=False)
    email = models.EmailField(unique=True, max_length=254)
    CurrentLocation = models.CharField(max_length=250, null= False)
    HighestLevelofEducation = models.CharField(max_length=11,choices=HighestLevelofeducation.choices,default=HighestLevelofeducation.degree)
    DutyOfStation = models.CharField(max_length=250, null=False)
    AvailabiltiyForRemotework = models.CharField(max_length=3,choices=RemoteStatus.choices,default=RemoteStatus.Yes)
    Software_Expertise = models.CharField(max_length=250, null=False)
    Software_Expertise_Level = models.CharField(max_length=12,choices=Softwareepertiseleve.choices,default=Softwareepertiseleve.beginner)
    Language = models.CharField(max_length=250, null=False)
    Level_Of_responsibility = models.CharField(max_length=11,choices=LevelOfresponsibility.choices,default=LevelOfresponsibility.staffmember)

