from django_filters import FilterSet, filters, CharFilter
from .models import *

# class TeacherFilter(FilterSet):
#     first_name = CharFilter(field_name='first_name', lookup_expr='icontains')
#     last_name = CharFilter(field_name='last_name', lookup_expr='icontains')
#     gender = CharFilter(field_name='gender', lookup_expr='iexact')
#     school = CharFilter(field_name='classrooms__school__name', lookup_expr='icontains')
#     classroom = CharFilter(field_name='classrooms__grade', lookup_expr='icontains')

#     class Meta:
#         model = Teacher
#         fields = ['first_name', 'last_name', 'gender', 'classrooms__school', 'classrooms']
