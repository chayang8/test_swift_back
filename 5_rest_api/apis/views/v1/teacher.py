from . import *

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_class = TeacherFilter
    filterset_fields = ['classrooms__school', 'classrooms', 'first_name', 'last_name', 'gender']
    search_fields = ['first_name', 'last_name']
    http_method_names = ['get', 'post', 'put', 'delete']