from django.db import models

# Create your models here.
class Resume_model(models.Model):
    role = models.CharField(max_length=200, null=False)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=50, default='India')
    pincode = models.CharField(max_length=10, null=True, blank=True)
    
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField()
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    other_links = models.TextField(max_length=500, null=True, blank=True)
    skills = models.TextField(null=False)
    
    # 10th education details
    edu_10 = models.CharField(max_length=4, null=True, blank=True)             # 'edu' stands for education
    edu_10_year = models.CharField(max_length=10, null=True, blank=True)
    edu_10_institute = models.CharField(max_length=150, null=True, blank=True)

    # 12th education details
    edu_12 = models.CharField(max_length=4, null=True, blank=True)             
    edu_12_year = models.CharField(max_length=10, null=True, blank=True)
    edu_12_institute = models.CharField(max_length=150, null=True, blank=True)

    # Graduation Detials
    edu_grad_name = models.CharField(max_length=100, null=True, blank=True)
    edu_grad_spz = models.CharField(max_length=100, null=True, blank=True)
    edu_grad_start = models.CharField(max_length=10, null=True, blank=True)
    edu_grad_end = models.CharField(max_length=10, null=True, blank=True)
    edu_grad_institute = models.CharField(max_length=150, null=True, blank=True)

    # Project Details
    project_title = models.CharField(max_length=150, null=True, blank=True)
    project_link = models.TextField(null=True, blank=True)
    project_disc = models.TextField(null=True, blank=True)

    
    '''
    "role": ""
    "phone": ""
    "email": ""
    "linkedin": ""
    "github": ""
    "other_links": ""
    "skills": ""
    
    
    "edu_10": ""
    "edu_10_year": ""
    "edu_10_institute": ""

    "edu_12": ""
    "edu_12_year": ""
    "edu_12_institute": ""

    "edu_grad_name": ""
    "edu_grad_spz": ""
    "edu_grad_start": ""
    "edu_grad_end": ""
    "edu_grad_institute": ""

    "project_title": ""
    "project_link": ""
    "project_disc": ""
    '''