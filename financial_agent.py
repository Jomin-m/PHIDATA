from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat


from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


web_search_agent = Agent(
    name='Web Search Agent',
    role='search web for financial data',
    model=Groq(id="lllama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions =["Always include source"],
    show_tool_calls=True,
    markdown=True,

)

## FINANCIAL AGENT
financial_agent = Agent(
    name='Financial Agent',
    role='search financial data',
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, stock_fundamentals=True, company_news=True)],
    instructions =["Use Tables to display data"],
    show_tool_calls=True,
    markdown=True,

)

multi_agent = Agent(    
    team=[web_search_agent, financial_agent],
    instructions=["Use the agents to search for financial data","Use the tables to display data","always include source"],
    show_tool_calls=True,
    markdown=True,
)

multi_agent.print_response("Summarize analyst recommendations and share the latest news on Apple Inc. (AAPL).",stream=True)


