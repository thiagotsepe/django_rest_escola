from django.test import TestCase
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer


class SerializerEstudanteTestCase(TestCase):
    def setUp(self) -> None:
        self.estudante = Estudante(
            nome = "Thiago",
            email = "thiago@thiago.com",
            cpf = "91653411040",
            data_nascimento = "2001-02-08",
            celular = "45 99999-9999"
        )
        self.serializer_estudante = EstudanteSerializer(instance=self.estudante)

    def test_verifica_campos_serializados_estudante(self):
        """Teste que verifica os campos que estão sendo serializados de estudante"""
        dados = self.serializer_estudante.data
        self.assertEqual(set(dados.keys()),                 # type: ignore
                         set(["id", "nome", "email", "cpf",
                               "data_nascimento", "celular"]))
        
    def test_verifica_conteudo_campos_serializados_estudante(self):
        """Teste que verifica o conteudo dos campos que estão sendo serializados de estudante"""
        dados: dict = self.serializer_estudante.data # type: ignore
        self.assertEqual(dados["nome"], self.estudante.nome)
        self.assertEqual(dados["email"], self.estudante.email)
        self.assertEqual(dados["cpf"], self.estudante.cpf)
        self.assertEqual(dados["data_nascimento"], self.estudante.data_nascimento)
        self.assertEqual(dados["celular"], self.estudante.celular)


class SerializerCursoTestCase(TestCase):
    def setUp(self) -> None:
        self.curso = Curso(
            codigo = "0231032331",
            descricao = "Curso especifico de POO",
            nivel = "A"
        )
        self.serializer_curso = CursoSerializer(instance = self.curso)

    def test_verifica_campos_serializados_curso(self):
        """Teste que verifica os campos que estão sendo serializado de curso"""
        dados: dict = self.serializer_curso.data # type: ignore
        self.assertEqual(set(dados.keys()), set(["id", "codigo", "descricao", "nivel"]))

    def test_verifica_conteudo_campos_serializados_estudante(self):
        """Teste que verifica o conteudo dos campos que estão sendo serializados de curso"""
        dados: dict = self.serializer_curso.data # type: ignore
        self.assertEqual(dados["codigo"], self.curso.codigo)
        self.assertEqual(dados["descricao"], self.curso.descricao)
        self.assertEqual(dados["nivel"], self.curso.nivel)


class SerializerMatriculaTestCase(TestCase):
    def setUp(self) -> None:
        self.estudante = Estudante.objects.create(
            nome = "Thiago",
            email = "thiago@thiago.com",
            cpf = "91653411040",
            data_nascimento = "2001-02-08",
            celular = "45 99999-9999"
        )
        self.curso = Curso.objects.create(
            codigo = "0231032331",
            descricao = "Curso especifico de POO",
            nivel = "A"
        )
        self.matricula = Matricula.objects.create(
            estudante = self.estudante,
            curso = self.curso,
            periodo = "V"
        )
        self.serializer_matricula = MatriculaSerializer(instance = self.matricula)

    def test_verifica_campos_serializados_matricula(self):
        """Teste que verifica os campos que estão sendo serializados de matricula"""
        dados: dict = self.serializer_matricula.data # type: ignore
        self.assertEqual(set(dados.keys()), set(["id", "estudante", "curso", "periodo"]))

    def test_verifica_conteudo_campos_serializados_matricula(self):
        """Teste que verifica o conteudo dos campos que estão sendo serializados de matricula"""
        dados: dict = self.serializer_matricula.data # type: ignore
        self.assertEqual(dados["estudante"], self.matricula.estudante.id) # type: ignore
        self.assertEqual(dados["curso"], self.matricula.curso.id) # type: ignore
        self.assertEqual(dados["periodo"], self.matricula.periodo)