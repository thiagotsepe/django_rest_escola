from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer
from escola.serializers import ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ["nome", "cpf"]
    ordering_fields = ["nome"]


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculasEstudante(generics.ListAPIView):
    def get_queryset(self):
        self.queryset = Matricula.objects.filter(estudante_id=self.kwargs["pk"])
        return self.queryset
    serializer_class = ListaMatriculasEstudanteSerializer


class ListaMatriculasCurso(generics.ListAPIView):
    def get_queryset(self):
        self.queryset = Matricula.objects.filter(curso_id=self.kwargs["pk"])
        return self.queryset
    serializer_class = ListaMatriculasCursoSerializer

