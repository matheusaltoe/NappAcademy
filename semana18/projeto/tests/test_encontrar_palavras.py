from projeto.encontrar_palavras import EncontrarPalavras
import pytest
import unittest

class TestEncontrarPalavras(unittest.TestCase):
    def test_instanciar_objeto_ok(self):
        objeto = EncontrarPalavras()
        assert isinstance(objeto, EncontrarPalavras)

    def test_todos_arquivos_txt(self):
        client = EncontrarPalavras()
        assert type(client.todos_arquivos_txt()) == list

    def test_todos_arquivos_txt_case(self):
        client = EncontrarPalavras()
        diretorio = 'diretorio10/arquivo22.txt'
        assert diretorio in client.encontrar_palavra('nAPp', ignore_case=True)

    def test_todos_arquivos_definidos(self):
        client = EncontrarPalavras()
        assert 'csv' in str(client.encontrar_palavra('napp', ignore_case=False))