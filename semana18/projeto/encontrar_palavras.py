import os
import re
import glob

class EncontrarPalavras:
    def __init__(self):
        self.tipos_arquivos = ['**/*.txt', '**/*.csv']

    def palavra_no_arquivo(self, palavra, arquivo, ignore_case):
        ignore_case =  re.IGNORECASE if ignore_case else 0
        with open(arquivo, 'r') as f:
            for line in f:
                match = re.search(palavra, line, flags=ignore_case)
                if match:
                    return palavra
        return False

    def todos_arquivos_txt(self):
        looking_for = '**/*.txt'
        matched = glob.glob(looking_for, recursive=True)
        return matched

    def todos_arquivos_definidos(self):
        matched = []
        for looking_for in self.tipos_arquivos:
            matched.extend(glob.glob(looking_for, recursive=True))
        return matched    

    def encontrar_palavra(self, palavra, ignore_case=False):
        encontrado_em = []
        arquivos = self.todos_arquivos_definidos()
        for arquivo in arquivos:
            if self.palavra_no_arquivo(palavra, arquivo, ignore_case):
                encontrado_em.append(arquivo)
        return encontrado_em

client = EncontrarPalavras()
busca_napp1 = client.encontrar_palavra('napp', ignore_case=False)
busca_napp2 = client.encontrar_palavra('NaPp', ignore_case=True)

print(busca_napp1)