from . import *



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['classroom__school', 'classroom', 'first_name', 'last_name', 'gender']
    search_fields = ['first_name', 'last_name']
    http_method_names = ['get', 'post', 'put', 'delete']
