from app.ai.classifier import chain


def categorizar(descricao: str) -> str:
    resposta = chain.invoke({"descricao": descricao})

    return resposta.strip()
