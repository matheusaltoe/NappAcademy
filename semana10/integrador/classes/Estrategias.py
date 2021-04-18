from abc import ABC, abstractmethod
from contextlib import closing
import sqlite3
import csv
import re


class Estrategia(ABC):
    """
    Classe Base para as estratégias (algoritmos)

    """
    @abstractmethod
    def execute(self, dados):
        """ Método em que o algoritmo é contido.
        Implementação do algoritmo na classe filha deve
        sobreescrever este método."""
        pass

    @abstractmethod
    def parametros_necessarios(self):
        """Sobreescrever este método para que retorne uma tupla
        com a lista de parâmetros necessários.
        Exemplo:
        ('algoritmo', 'dbname', 'host', 'user', 'password')
        """
        pass

    @abstractmethod
    def nome(self):
        """Sobreescrever este método para que
        retorne o nome do algoritmo utilizado."""
        pass


class Estrategia_SQLite(Estrategia):
    def execute(self, dados):
        lista_registros = []
        db = dados['db']
        with closing(sqlite3.connect(db)) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vendas;")
            for linha in cursor.fetchall():
                lista_registros.append(linha)
        return lista_registros

    def parametros_necessarios(self):
        return ('algoritmo', 'db')

    def nome(self):
        return 'Algoritmo SQLite'


class Estrategia_CSV(Estrategia):
    def execute(self, dados):
        lista_registros = []
        arquivo = dados['arquivo']
        with open(arquivo, newline='\n') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                lista_registros.append(line)
        return lista_registros

    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo CSV'


class Estrategia_Texto1(Estrategia):
    def execute(self, dados):
        lista_registros = []
        arquivo = dados['arquivo']
        with open(arquivo) as fp:
            reader = fp.readlines()
            for line in reader:
                if not line[0].isdigit():
                    continue
                data = line[:11].strip()
                produto = line[49:].strip()
                total = line[36:48].strip()
                lista_registros.append((produto, total, data))
        return lista_registros
    
    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo Texto1'


class Estrategia_Texto2(Estrategia):
    def execute(self, dados):
        lista_registros = []
        arquivo = dados['arquivo']
        with open(arquivo) as fp:
            reader = fp.readlines()
            for line in reader:
                pattern = '(?P<data>\d{4}-\d{2}-\d{2})|(?P<produto>[A-z]+\s\d+)|(?P<total>\d+[\.\,]+\d+)'
                result = re.findall(pattern, line)
                if result:
                    data = result[0][0]
                    produto = result[1][1]
                    total = result[2][2]
                    lista_registros.append((produto, total, data))
        return lista_registros
    
    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo Texto2'
