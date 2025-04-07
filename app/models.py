from django.db import models

class StudentEnquiry(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    dob = models.CharField(max_length=255, null=False, blank=False)  
    mobile = models.CharField(unique=True, max_length=10, null=False, blank=False)  
    email = models.EmailField(unique=True, null=False, blank=False)
    currently_working = models.CharField(max_length=3, null=False, blank=False, choices=[('yes', 'Yes'), ('no', 'No')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.enquiryId} - {self.name}"