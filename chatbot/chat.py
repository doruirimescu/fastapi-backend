from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_extraction_chain, create_extraction_chain_pydantic
from langchain.output_parsers import PydanticOutputParser

from chatbot.user_model import SCHEMA
from dotenv import load_dotenv
import asyncio

load_dotenv()


# Input
inp = """
My name is Jane Smith, and I'm actively seeking new opportunities. You can reach me at jane.smith@example.com or call me at (123) 456-7890.

Education:

Bachelor's Degree in Computer Science from University of Tech, graduated in 2019.
Master's Degree in Artificial Intelligence from AI Institute, graduated in 2021.
Work Experience:

Software Engineer at TechCorp from January 2020 to June 2021. Responsible for developing and maintaining web applications.
Data Scientist at DataWorld from July 2021 to present. Analyzing large datasets and creating predictive models.
Skills:

Programming: Python, Java, C++
Machine Learning
Data Analysis
Certifications:

Certified Python Programmer, issued by Python Institute in June 2018, expires in June 2023.
Machine Learning Specialist, issued by AI Association in January 2020.
Languages:

English: Native
Spanish: Fluent
French: Intermediate
I'm interested in Full-time positions in the Software Development industry, preferably in New York City.
My LinkedIn profile can be found at https://www.linkedin.com/in/janesmith,
and my online portfolio is at http://www.janesmithportfolio.com.
You can also download my resume from http://www.janesmithresume.com.
"""


# Run chain
async def gather_data(inp):
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    chain = create_extraction_chain(SCHEMA, llm)
    result = await chain.arun(inp)
    print(result)


asyncio.run(gather_data(inp))


# TODO: store the result in a database
# TODO: change schema into pydantic model
