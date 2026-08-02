import csv


def ler_csv(conteudo: str):
    leitor = csv.DictReader(conteudo.splitlines())

    dados = []

    for linha in leitor:
        dados.append(
            {
                "data": linha["date"],
                "descricao": linha["title"],
                "valor": linha["amount"],
            }
        )

    return dados


def converter_valor(valor):
    valor = valor.strip()

    valor = valor.replace(" ", "")

    if "," in valor:
        valor = valor.replace(".", "")
        valor = valor.replace(",", ".")

    return float(valor)
