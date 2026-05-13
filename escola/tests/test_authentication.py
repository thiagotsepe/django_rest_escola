from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse


class AuthenticationUserTestCase(APITestCase):
    def setUp(self) -> None:
        self.usuario = User.objects.create_superuser(username="admin", 
                                                     email= "admin@admin.com", 
                                                     password="admin")
        self.url = reverse("Estudantes-list")

    def test_autenticacao_user_com_credenciais_corretas(self):
        """Teste que verifica a autenticação de um user com as credenciais corretas"""
        usuario = authenticate(username="admin", password="admin")
        self.assertTrue((usuario is not None) and usuario.is_authenticated)
    
    def test_autenticacao_user_com_username_incorreto(self):
        """Teste que verifica a autenticação de um user com username incorreto"""
        usuario = authenticate(username="admn", password="admin")
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_autenticacao_user_com_password_incorreto(self):
        """Teste que verifica a autenticação de um user com password incorreto"""
        usuario = authenticate(username="admin", password="admi")
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_requisicao_get_autorizada(self):
        """Teste que verifica uma requisição GET autorizada"""
        self.client.force_authenticate(self.usuario) # type: ignore
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_nao_autorizada(self):
        """Teste que verifica uma requisição GET não autorizada"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
