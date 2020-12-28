from django.db import models
from django.urls import reverse
import uuid
# Create your models here.



class Student(models.Model):
    """AModel representing a particular student"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    class_st=models.IntegerField()
    d_o_b =models.DateField(null=True, blank=True)
    email=models.EmailField()
    Bio=models.TextField(max_length=1000, help_text='Tell others something about you')
    Pref_type=models.CharField(max_length=200, help_text="Left for now")
    def __str__(self):
        """String for representing the Model objects"""
        return (self.first_name)
    
    def get_absolute_url(self):
        """Returns the url to access a detail representing the model"""
        return reverse('Students')

    



class StudentInstance(models.Model):
    """Model representing a specific copy of a book """
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular student across whole staff')
    student=models.ForeignKey('Student',on_delete=models.SET_NULL, null=True)
    
    
      

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.student.first_name})'


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    class_st=models.IntegerField()
    d_o_b =models.DateField(null=True, blank=True)
    email=models.EmailField()
    Bio=models.TextField(max_length=1000, help_text='Tell others something about you')
    
    class Meta:
        ordering=['last_name' , 'first_name']    

    def get_absolute_url(self):
        
        return reverse('Teacher_detail')

    def __str__(self):
         return f'{self.last_name}, {self.first_name}'




class stu_class(models.Model):
    """Model reperesenting student class"""
    name=models.IntegerField(help_text='Enter your class(ex 10) ')

    def __str(self):
        """String for representing Model class"""