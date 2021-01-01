from django.contrib import admin

# Register your models here.
from .models import Student,StudentInstance,Teacher, stu_class

#admin.site.register(Student)
#admin.site.register(StudentInstance)
admin.site.register(Teacher)
admin.site.register(stu_class)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'class_st', 'd_o_b', 'email', 'Bio')


#admin.site.register(Student,TeacherAdmin)

class StudentAdmin(admin.ModelAdmin):
       list_display = ('last_name', 'first_name', 'class_st', 'd_o_b', 'email', 'Bio', 'Pref_type')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(StudentInstance)
class StudentInstanceAdmin(admin.ModelAdmin):
    list_filter = ('id', 'student')

  