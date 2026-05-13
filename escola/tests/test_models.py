from django.test import TestCase
from escola.models import Estudante, Curso, Matricula


class ModelEstudanteTestCase(TestCase):
    """ def teste_falha(self):
        self.fail("Teste falhou") """
    
    def setUp(self) -> None:
        self.estudante = Estudante.objects.create(
            nome = "Thiago",
            email = "thiago@thiago.com",
            cpf = "91653411040",
            data_nascimento = "2001-02-08",
            celular = "45 99999-9999"
        )

    def test_verifica_atributos_estudante(self):
        """Teste que verifica os atributos do modelo de Estudante"""
        self.assertEqual(self.estudante.nome, "Thiago")
        self.assertEqual(self.estudante.email, "thiago@thiago.com")
        self.assertEqual(self.estudante.cpf, "91653411040")
        self.assertEqual(self.estudante.data_nascimento, "2001-02-08")
        self.assertEqual(self.estudante.celular, "45 99999-9999")

    
class ModelCursoTestCase(TestCase):
    def setUp(self) -> None:
        self.curso = Curso.objects.create(
            codigo = "0231032331",
            descricao = "Curso especifico de POO",
            nivel = "A"
        )
    
    def test_verifica_atributos_curso(self):
        """Teste que verifica os atributos do modelo de Curso"""
        self.assertEqual(self.curso.codigo, "0231032331")
        self.assertEqual(self.curso.descricao, "Curso especifico de POO")
        self.assertEqual(self.curso.nivel, "A")


class ModelMatriculaTestCase(TestCase):
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

    def test_verifica_atributos_matricula(self):
        """Teste que verifica os atributos do modelo de Matricula"""
        self.assertEqual(self.matricula.estudante, self.estudante)
        self.assertEqual(self.matricula.curso, self.curso)
        self.assertEqual(self.matricula.periodo, "V")