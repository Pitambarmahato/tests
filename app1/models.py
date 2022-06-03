from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    std_class = models.PositiveIntegerField(null=True)
    roll = models.PositiveIntegerField(null=True)
    mark = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name
    
    @property
    def grade(self):
        if self.mark < 40:
            return "fail"
        else:
            return "pass"