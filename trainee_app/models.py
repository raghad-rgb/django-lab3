from django.db import models
from course_app.models import Track, Course

class Trainee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    track = models.ForeignKey(Track, on_delete=models.CASCADE, null=True, blank=True) 

    def __str__(self):
        return self.name