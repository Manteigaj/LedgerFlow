import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    model="gpt-5-mini",
    temperature=0,
)

parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a financial transaction classifier.

Choose EXACTLY ONE category.

Categories:

- Food & Dining
- Transportation
- Health
- Entertainment
- Groceries
- Education
- Housing
- Other

Respond only with the category name.
""",
        ),
        (
            "human",
            """Description: {description}""",
        ),
    ]
)

chain = prompt | model | parser
