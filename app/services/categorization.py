from app.ai.classifier import chain


def categorize(description: str) -> str:
    response = chain.invoke({"description": description})

    return response.strip()
