from django.db import models

# Create your models here.

JOB_TYPE = (
    ('Full Time' , 'Full Time'),
    ('Part Time' , 'Part Time'),
)
# Create your models here.
class job (models.Model) :
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE , blank=True , null=True)
    description = models.TextField(max_length=1000)
    puplished_at = models.DateField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)


    def __str__(self):
        return self.title
