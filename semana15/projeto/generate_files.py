import csv
from collections import defaultdict


class ProjetoLargeCSV:
    def __init__(self):
        self.anos = list()
        self.header = self.get_header_years()

    def __repr__(self):
        return 'Projeto para dividir um csv em arquivos menores'

    def get_header_years(self):
        with open('candidatura.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            header = list(next(reader).keys())
            for row in reader:
                if row.get('ano_eleicao') not in self.anos:
                    self.anos.append(row.get('ano_eleicao'))
            return header


    def process_data(self, ano):
        with open('candidatura.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == ano:
                    anos_agrupados[ano].append(row)
                yield row


client = ProjetoLargeCSV()
for ano in client.anos:
    anos_agrupados = defaultdict(list)
    for i, row in enumerate(client.process_data(ano)):
        pass

    for ano, value in anos_agrupados.items():
        valores = list()
        print(ano)
        for elen in value:
            valores.append(elen)
        with open(f'eleicao_{ano}.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(client.header)
            for l in valores:
                writer.writerow(l)
