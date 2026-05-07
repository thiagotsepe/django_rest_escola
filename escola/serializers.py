from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ["id", "nome", "email", "cpf", "data_nascimento", "celular"]


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = "__all__"


class MatriculaPorEstudante(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = ["Curso.descricao", "periodo"] 


class MatriculaPorCurso(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        