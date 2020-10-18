from django.db import models
from datetime import datetime


# Create your models here.
class Experience(models.Model):
    title = models.CharField(max_length=200)
    employment_type = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return self.title


class Education(models.Model):
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_year = models.DateField()
    end_year = models.DateField()
    final_gpa = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Education'

    def __str__(self):
        return self.school


class LicensesAndCertifications(models.Model):
    name = models.CharField(max_length=200)
    issuing_org = models.CharField(max_length=200)
    expire = models.BooleanField()
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=200)
    Credential_url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Licenses & Certifications'

    def __str__(self):
        return self.name
