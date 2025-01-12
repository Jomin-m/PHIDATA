
### Financial Data and News Agent
This project is a Streamlit application that leverages AI agents to fetch and analyze financial data and news about companies. The app integrates multiple tools and APIs, including OpenAI, DuckDuckGo, and Yahoo Finance, to provide a comprehensive overview of company-specific financial metrics and related news articles.

#### Features
AI-Powered Agents:

Web Search Agent: Searches the web for the latest financial news and summarizes it with source and date.
Financial Analyst Agent: Analyzes stock prices and financial data, presenting it in table format.
Multi-Agent System: Combines the outputs of the two agents to provide a unified analysis.
Interactive User Input:

Enter a company name or ticker symbol (e.g., AAPL for Apple Inc.) to fetch relevant data.
Data Display:

Financial data is presented in a styled table with key metrics highlighted.
News articles are displayed in markdown format for better readability.
Error Handling:

Handles cases where no data is found or errors occur during processing.
Provides detailed error messages for debugging.
Setup Instructions
Prerequisites
Python 3.8 or higher
Streamlit
OpenAI API key
Environment variables for sensitive data
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/financial-data-news-agent.git
cd financial-data-news-agent
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up environment variables:

Create a .env file in the project root:
env
Copy code
OPENAI_API_KEY=your_openai_api_key
Replace your_openai_api_key with your actual OpenAI API key.
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Usage
Start the app by running the Streamlit command above.
Enter a company name or ticker symbol into the input field.
Wait for the app to fetch and display the financial data and news.
Code Highlights
AI Agents
Web Search Agent: Uses DuckDuckGo to fetch and summarize the latest financial news.
Financial Analyst Agent: Leverages YFinanceTools to analyze stock price and fundamental metrics.
Multi-Agent System: Coordinates the outputs of both agents for a comprehensive analysis.
Data Extraction and Display
Functions to extract financial data and news from agent responses.
Styled dataframes and markdown displays for enhanced readability.
Error Handling
Graceful handling of missing data or API errors.
Debugging support via traceback display.
Example Screenshots
Input Section
A simple text box where users can enter a company name or ticker symbol.

Financial Data Table
Highlights key metrics like Market Cap, PE Ratio, and more.

Latest News
Summarized news articles with source and date.

Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request for bug fixes, feature suggestions, or improvements.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgements
Streamlit
OpenAI
Yahoo Finance
DuckDuckGo
Enjoy exploring financial insights with AI-powered agents! 🚀
