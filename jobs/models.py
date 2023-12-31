from django.db import models

# Create your models here.
class Job(models.Model):
    LEVEL_CHOICES = (
        ('jr', 'Júnior'),
        ('pl', 'Pleno'),
        ('sr', 'Sênior'),
    )
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    requirements = models.TextField()
    responsibilities = models.TextField()
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    skills = models.ManyToManyField('jobs.Skill', related_name='jobs')


    def __str__(self):
        return self.title
    
    def requirements_list(self):
        return self.requirements.split('\n')
    
    def responsibilities_list(self):
        return self.responsibilities.split('\n')

class Skill(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
        return self.title
    
