def categorizar(descricao: str) -> str:
    descricao = descricao.lower()

    categorias = {
        "Alimentação": [
            "ifood",
            "restaurante",
            "lanchonete",
            "pizza",
            "hamburguer",
            "burger",
        ],
        "Mercado": [
            "mercado",
            "supermercado",
            "assai",
            "atacadao",
            "guanabara",
        ],
        "Transporte": [
            "uber",
            "99",
            "posto",
            "shell",
            "ipiranga",
        ],
        "Saúde": [
            "farmacia",
            "drogaria",
            "raia",
            "pacheco",
        ],
        "Lazer": [
            "cinema",
            "netflix",
            "spotify",
            "steam",
        ],
    }

    for categoria, palavras in categorias.items():
        if any(palavra in descricao for palavra in palavras):
            return categoria

    return "Outros"
