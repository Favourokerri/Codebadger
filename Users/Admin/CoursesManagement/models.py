from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Course(models.Model):
    """ course """
    course_image = models.ImageField(upload_to='media/course_image/', null=True, blank=True)
    name = models.CharField(max_length=200, unique=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    about = CKEditor5Field(default="Add about course")
    registered_student = models.IntegerField(default=0)
    number_of_modules = models.IntegerField(default=0)
    status = models.CharField(max_length=50, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name