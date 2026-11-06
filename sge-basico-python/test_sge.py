"""Pruebas unitarias básicas para las funciones del SGE."""
import unittest
from main import buscar_estudiante_por_id


class PruebasSGE(unittest.TestCase):
    def setUp(self):
        self.estudiantes = [
            {"id": 1001, "nombre": "Ana Gómez", "edad": 20,
             "programa": "Ingeniería de Sistemas", "promedio": 4.5},
            {"id": 1002, "nombre": "Carlos Ruiz", "edad": 22,
             "programa": "Administración", "promedio": 3.8},
        ]

    def test_busqueda_exitosa(self):
        resultado = buscar_estudiante_por_id(self.estudiantes, 1001)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado["nombre"], "Ana Gómez")

    def test_busqueda_fallida(self):
        resultado = buscar_estudiante_por_id(self.estudiantes, 9999)
        self.assertIsNone(resultado)

    def test_lista_vacia(self):
        resultado = buscar_estudiante_por_id([], 1001)
        self.assertIsNone(resultado)


if __name__ == "__main__":
    unittest.main(verbosity=2)
