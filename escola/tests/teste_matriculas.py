from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Matricula, Estudante, Curso


class MatriculasTestCase(APITestCase):
    fixtures = ["prototipo_banco.json"]
    def setUp(self):
        self.usuario = User.objects.create_superuser(username="admin", email="admin@admin.com", password="admin")
        self.url = reverse("Matriculas-list")
        self.client.force_authenticate(user=self.usuario) # type: ignore
        self.estudante = Estudante.objects.get(pk=1)
        self.curso = Curso.objects.get(pk=1)
        self.matricula = Matricula.objects.get(pk=1)

    def test_requisicao_get_para_listar_matriculas(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_matriculas(self):
        """Teste de requisição POST"""
        dados = {
            "estudante": self.estudante.pk,
            "curso": self.curso.pk,
            "periodo": "V"
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_uma_matricula(self):
        """Teste de requisição DELETE para um matricula"""
        response = self.client.delete(f"{self.url}1/") #/matriculas/2/
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_requisicao_put_matriculas(self):
        """Teste de requisição PUT"""
        dados = {
            "estudante": self.estudante.pk, # type: ignore
            "curso": self.curso.pk, # type: ignore
            "periodo": "M"
        }
        response = self.client.put(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)