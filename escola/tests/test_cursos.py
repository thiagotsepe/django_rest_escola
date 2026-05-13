from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from escola.models import Curso
from escola.serializers import CursoSerializer


class CursosTestCase(APITestCase):
    fixtures = ["prototipo_banco.json"]
    def setUp(self):
        self.usuario = User.objects.get(username = "sepe")
        self.url = reverse("Cursos-list")
        self.client.force_authenticate(user=self.usuario) # type: ignore
        self.curso_01 = Curso.objects.get(pk=1)

    def test_requisicao_get_para_listar_cursos(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_lista_um_curso(self):
        """Teste de requisição GET para um curso"""
        response = self.client.get(self.url+"1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_curso = Curso.objects.get(pk=1)
        dados_curso_serializados = CursoSerializer(instance = dados_curso).data
        self.assertEqual(response.data, dados_curso_serializados) # type: ignore
    
    def test_requsicao_post_para_criar_um_curso(self):
        """Teste de requisição POST"""
        dados = {
            "codigo": "0312013",
            "descricao": "Curso de teste TDD",
            "nivel": "B"
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_um_curso(self):
        """Teste de requisição DELETE para um curso"""
        response = self.client.delete(f"{self.url}1/") #/cursos/1/
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_um_curso(self):
        """Teste de requisição PUT para um curso"""
        dados = {
            "codigo": "11111",
            "descricao": 'Teste put teste put curso',
            "nivel": "B"
        }
        response = self.client.put(f"{self.url}1/", data = dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)