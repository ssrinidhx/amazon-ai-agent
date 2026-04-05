import os
from dotenv import load_dotenv

from langchain.agents import initialize_agent
from langchain.agents import Tool
from langchain_groq import ChatGroq

from tools.sales_trend_analyzer import sales_trend_analyzer
from tools.keyword_performance_evaluator import keyword_performance_evaluator
from tools.spend_revenue_analyzer import spend_revenue_analyzer
from tools.action_recommender import action_recommender

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.1-8b-instant",
    temperature=0
)

tools = [

    Tool(
        name="Sales Trend Analyzer",
        func=sales_trend_analyzer,
        description="Use this tool when the user asks about product sales performance, top products, revenue, or units sold."
    ),

    Tool(
        name="Keyword Performance Evaluator",
        func=keyword_performance_evaluator,
        description="Use this tool when the user asks about advertising keyword performance, high ACoS, or wasted advertising spend."
    ),

    Tool(
        name="Spend Revenue Analyzer",
        func=spend_revenue_analyzer,
        description="Use this tool when the user asks how advertising contributes to product revenue."
    ),

    Tool(
        name="Action Recommender",
        func=action_recommender,
        description="Use this tool when the user asks for recommendations to improve advertising performance."
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True,
    max_iterations=4,
    early_stopping_method="generate"
)

def run_agent(query):

    response = agent.invoke({
        "input": query
    })

    return response["output"]