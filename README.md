# Financial Data and News Agent

This repository hosts a Streamlit application that uses AI agents to fetch and analyze financial data and news about companies. It integrates tools like OpenAI, DuckDuckGo, and Yahoo Finance to provide a detailed overview of financial metrics and the latest news.

## Features

- **AI-Powered Agents**:
  - **Web Search Agent**: Searches for and summarizes the latest financial news, including source and date.
  - **Financial Analyst Agent**: Analyzes stock prices and financial data, presenting it in a table format.
  - **Multi-Agent System**: Combines the results from both agents for a unified analysis.

- **Interactive User Interface**:
  - Enter a company name or ticker symbol (e.g., `AAPL` for Apple Inc.) to fetch data.

- **Data Visualization**:
  - Displays financial data in a styled table with key metrics highlighted.
  - Presents news articles in a readable markdown format.

- **Error Handling**:
  - Handles scenarios where no data is found or when processing errors occur.
  - Provides detailed error messages for debugging.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Streamlit
- OpenAI API key
- Environment variables for sensitive data

### Installation

1. **Clone the Repository**:
   git clone https://github.com/your-username/financial-data-news-agent.git
   cd financial-data-news-agent
   
2. **Create and Activate a Virtual Environment**:
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install Dependencies**:
   pip install -r requirements.txt
   
4. **Set Up Environment Variables**:
  - Create a .env file in the project root:
      OPENAI_API_KEY=your_openai_api_key
  - Replace your_openai_api_key with your OpenAI API key.
    
5. **Run the Application**:
  streamlit run app.py


   


