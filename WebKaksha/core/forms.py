from django import forms
from .models import Student
 
class MyForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ["first_name", "last_name","class_st","d_o_b","email","Bio","Pref_type",]
    