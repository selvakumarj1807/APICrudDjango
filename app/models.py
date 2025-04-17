from django.db import models

class StudentEnquiry(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    dob = models.CharField(max_length=255, null=True, blank=True)  
    mobile = models.CharField(max_length=10, null=True, blank=True)  
    email = models.EmailField(null=True, blank=True)
    currently_working = models.CharField(max_length=3, null=True, blank=True, choices=[('yes', 'Yes'), ('no', 'No')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.enquiryId} - {self.name}"