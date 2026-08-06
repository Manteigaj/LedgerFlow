from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
chave_api = os.getenv("OPENAI_API_KEY")

modelo = ChatOpenAI(model="gpt-5-mini", temperature=0)

parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """Você é um classificador financeiro.

Escolha APENAS UMA categoria.

Categorias:

- Alimentação
- Transporte
- Saúde
- Lazer
- Mercado
- Educação
- Moradia
- Outros

Responda somente com o nome da categoria.
""",
        ),
        (
            "human",
            """ Descrição:{descricao} """,
        ),
    ]
)

chain = prompt | modelo | parser
