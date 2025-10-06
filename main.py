import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool

# Load API key
load_dotenv()

# Define structured output model
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# Setup Gemini LLM via LangChain wrapper
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("gemini"),
)

# Setup output parser
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# Tools list
tools = [search_tool, wiki_tool, save_tool]

# Create prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", 
    """You are a research assistant that uses tools and responds in structured JSON format.
Use this format:\n{format_instructions}"""),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}")
]).partial(format_instructions=parser.get_format_instructions())


# Create agent
agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
)

# Create executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Run query
query = input("What can I help you research? ")
response = agent_executor.invoke({"query": query})

try:
    structured_response = parser.parse(response.get("output")[0]["text"])
    print(structured_response)
except Exception as e:
    print("Error parsing response", e, "Raw Response - ", response)
