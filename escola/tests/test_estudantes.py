from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from escola.models import Estudante
from rest_framework import status
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    fixtures = ["prototipo_banco.json"]
    def setUp(self):
        self.usuario = User.objects.get(username="sepe")
        self.url = reverse("Estudantes-list")
        self.client.force_authenticate(user=self.usuario) # type: ignore
        self.estudante_01 = Estudante.objects.get(pk=1)
        self.estudante_02 = Estudante.objects.get(pk=2)

    def test_requisicao_get_para_listar_estudantes(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url) #/estudantes/
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_um_estudantes(self):
        """Teste de requisição GET para um estudante"""
        response = self.client.get(self.url + "1/") #/estudantes/1/
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializados = EstudanteSerializer(instance = dados_estudante).data
        self.assertEqual(response.data, dados_estudante_serializados) # type: ignore

    def test_requisicao_post_para_criar_um_estudante(self):
        """Teste de requisição POST para um estudante"""
        dados = {
            "nome": "teste",
            "email": "teste@gmail.com",
            "cpf": "95637267073",
            "data_nascimento": "2003-06-05",
            "celular": "45 99999-9999"
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_um_estudante(self):
        """Teste de requisição DELETE para um estudante"""
        response = self.client.delete(f"{self.url}2/") #/estudantes/2/
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_um_estudante(self):
        """Teste de requisição PUT para um estudante"""
        dados = {
            "nome" : "teste",
            "email": "testeput@put.com",
            "cpf": "27254912075",
            "data_nascimento": "2032-04-05",
            "celular": "11 30303-3232"
        }
        response = self.client.put(f"{self.url}1/", data = dados) #/estudantes/2/
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    