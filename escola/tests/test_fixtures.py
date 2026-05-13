from django.test import TestCase
from escola.models import Estudante, Curso


class FixturesTestCase(TestCase):
    fixtures = ["prototipo_banco.json"]
    
    def test_carregamento_da_fixtures(self):
        """Teste que verifica o carregamento da Fixtures"""
        estudante = Estudante.objects.get(cpf="98822059174")
        curso = Curso.objects.get(pk=1)
        self.assertEqual(estudante.celular, "11 95907-6006")
        self.assertEqual(curso.codigo, "POO")