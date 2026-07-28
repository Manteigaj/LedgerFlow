import csv


def ler_csv(conteudo: str):
    leitor = csv.DictReader(conteudo.splitlines())

    return list(leitor)
