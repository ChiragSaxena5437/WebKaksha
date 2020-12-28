from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.http import Http404



from .models import Student,StudentInstance,Teacher, stu_class

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_stu = Student.objects.all().count()
    num_instances = StudentInstance.objects.all().count()
    num_Teacher=Teacher.objects.all().count()
    # Available books (status = 'a')
   
    # The 'all()' is implied by default.
    num_Teachers = Teacher.objects.all().count()

    context = {
        'num_stu': num_stu,
        'num_instances': num_instances,
        'num_Teacher': num_Teacher,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class StudentListView(generic.ListView):
    model = Student
    
    context_object_name = 'my_Student_list'   # your own name for the list as a template variable
    queryset = Student.objects.all()
    template_name = 'core/Student_list.html'  # Specify your own template name/location

def StudentDetailView(request, primary_key):
    try:
       Student_1 = Student.objects.get(pk=primary_key)
    except Student.DoesNotExist:
        raise Http404('Book does not exist')

    return render(request, 'core/Student_detail.html', context={'Student': Student_1})
