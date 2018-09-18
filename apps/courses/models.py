from django.db import models
from django.contrib import messages

class CourseManager(models.Manager):
    def basic_validations(self, postData):
        errors = {}
        if len(postData['course_name']) < 5:
            errors['name'] = "Course name must be more than 5 characters"
        return errors

class DescriptionManager(models.Manager):
    def basic_validations(self, postData):
        errors = {}
        if len(postData['desc']) < 15:
            errors['desc'] = "Description must be more than 15 characters"
        return errors

class CommentManager(models.Manager):
    def basic_validations(self, postData):
        errors = {}
        if len(postData['comment']) < 15:
            errors['length'] = "Comment must be more than 15 characters"
        return errors

class Description(models.Model):
    desc = models.CharField(max_length=255, unique=True)
    objects = DescriptionManager()

class Course(models.Model):
    name = models.CharField(max_length=255)
    course_desc = models.OneToOneField(Description, on_delete=models.CASCADE, to_field="desc", related_name="course")
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CourseManager()
    
class Comment(models.Model):
    comment = models.CharField(max_length=60)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CommentManager()
