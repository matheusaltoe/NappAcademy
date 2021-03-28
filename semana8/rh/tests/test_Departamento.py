from rh.classes.Departamento import Departamento
from datetime import date, timedelta


class TestDepartamento:
    def test_class_declared(self):
        objeto = Departamento('Departamento XYZ', 'Responsável')
        assert isinstance(objeto, Departamento)

    def test_instanciar(self):
        objeto = Departamento('Departamento XYZ', 'Responsável')
        assert objeto.nome == 'Departamento XYZ'
        assert objeto.responsavel is None

    def test_str_repr(self):
        objeto = Departamento('Departamento XYZ', 'Responsável')
        assert str(objeto) == 'Departamento XYZ'
        assert repr(objeto) == 'Departamento = Departamento XYZ'

    def test_setters(self):
        objeto = Departamento('Curadoria', 'Geraldo')
        assert objeto.nome == 'Curadoria'
        objeto.nome = 'ETL'
        assert objeto.nome == 'ETL'

    def test_properties(self):
        objeto = Departamento('Departamento XYZ', 'Responsável')
        assert objeto.nome == 'Departamento XYZ'

    def test_responsavel(self):
        departamento = Departamento('Departamento XYZ', 'Responsável')
        assert departamento.responsavel is None
        departamento.informar_responsavel('José da Silva', 1, 1, 1990)
        assert departamento.responsavel.nome == 'José da Silva'

    def test_responsavel_substituido(self):
        departamento = Departamento('Departamento XYZ', 'Responsável')
        assert departamento.responsavel is None
        departamento.informar_responsavel('José da Silva', 1, 1, 1990)
        assert departamento.responsavel.nome == 'José da Silva'
        departamento.informar_responsavel('João Oliveira', 1, 1, 1990)
        assert departamento.responsavel.nome == 'João Oliveira'

    def test_add_colaborador(self):
        departamento = Departamento('Departamento XYZ', 'Responsável')
        departamento.informar_responsavel('José da Silva', 1, 1, 1990)
        departamento.add_colaborador('João Oliveira', 18, 3, 1992)
        departamento.add_colaborador('Pedro Mendonça', 18, 4, 1993)
        assert len(departamento.colaboradores) == 2

    def test_verificar_aniversariantes(self):
        hoje = date.today()
        retorno = [('João Oliveira', f'1992-03-{hoje.day}', 'Departamento XYZ'),
                   ('Luis Fernando', f'2000-03-{hoje.day}', 'Departamento XYZ')]
        dt1 = date.today() - timedelta(days=4)
        depto = Departamento('Departamento XYZ', 'Responsável')
        depto.informar_responsavel('José da Silva', dt1.day, dt1.month, 1990)
        depto.add_colaborador('João Oliveira', hoje.day, hoje.month, 1992)
        depto.add_colaborador('Pedro Mendonça', dt1.day, dt1.month, 1993)
        depto.add_colaborador('Luis Fernando', hoje.day, hoje.month, 2000)
        depto.add_colaborador('Maurício Souza', dt1.day, dt1.month, 1085)
        aniversariantes = depto.verificar_aniversariantes()
        assert aniversariantes == retorno
        assert len(aniversariantes) == 2
        assert len(aniversariantes[0]) == 3
        assert type(aniversariantes[0]) == tuple
        assert type(aniversariantes) == list
    
    def test_verificar_aniversariantes_2(self):
        hoje = date.today()
        retorno = [('José da Silva', f'1992-03-{hoje.day}', 'Departamento XYZ')]
        depto = Departamento('Departamento XYZ', 'Responsável')
        depto.informar_responsavel('José da Silva', hoje.day, hoje.month, 1992)
        aniversariantes = depto.verificar_aniversariantes()
        assert aniversariantes == retorno


