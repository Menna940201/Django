from django.db import models
from django.shortcuts import get_object_or_404
# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    technologies = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null = True, blank=True)
    def __str__(self):
        return self.title
    @classmethod
    def get_all_projects(cls):
        return cls.objects.all()
    @classmethod
    def get_specific_project(cls, id):
        return get_object_or_404(cls, pk = id)

