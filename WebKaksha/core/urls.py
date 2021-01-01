from django.urls import path
from . import views

urlpatterns = [
      path('', views.index, name='index'),
      path('Students/', views.StudentListView.as_view(), name='Students'),
     path('Students/form/', views.my_form, name='form'),
     #path('Students/<int:pk>', views.StudentDetailView.as_view(),name='Student Detail'),
      # path('url/', views.my_reused_view, {'my_template_name': 'some_path'}, name='aurl'),
      #path('anotherurl/', views.my_reused_view, {'my_template_name': 'another_path'}, name='anotherurl'),

]