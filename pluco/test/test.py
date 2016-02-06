from django.test import TestCase
from foros.models import Forum

class ForumTest(TestCase):
    def setUp(self):
	Forum.objects.create(theme="Test de Prueba",title="Test de Prueba",asignature="PRUEBA")

    def testing(self):
	prueba = Forum.objects.get(title="Test de Prueba")
