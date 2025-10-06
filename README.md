# Agentic AI Research Assistant

A **fully-coded, agentic AI research assistant** built using **LangChain**, **Google Gemini AI**, and other powerful AI tools. Unlike no-code platforms, this project showcases **custom coding, tool integration, and structured AI outputs** for reliable, source-backed research.

---

## Features

- ✅ **Structured AI Research**  
  Generates research summaries in JSON format with `topic`, `summary`, `sources`, and `tools_used`.

- ✅ **Multi-Tool Integration**  
  Utilizes:  
  - **DuckDuckGo Search**: For real-time web information  
  - **Wikipedia API**: For structured and credible knowledge  
  - **Save-to-File Tool**: Logs research output with timestamps  

- ✅ **Agentic AI Capabilities**  
  The AI can autonomously decide which tool to use, collect data, and consolidate information into a structured output.  

- ✅ **High-Performance LLM**  
  Uses **Google Gemini 1.5 Flash** for accurate, up-to-date, and natural responses.  

- ✅ **Fully Coded**  
  No no-code tools — demonstrates proficiency in Python, LangChain, and API integration.

---

## Tech Stack

- Python 3.11+  
- [LangChain](https://www.langchain.com/)  
- [Google Gemini AI](https://developers.generativeai.google/)  
- DuckDuckGo Search  
- Wikipedia API  
- Pydantic for structured outputs  

---

## How It Works

1. User enters a research query.  
2. The agentic AI evaluates which tool(s) to use.  
3. Tools fetch information from the web and Wikipedia.  
4. AI consolidates the information into a **structured JSON format**.  
5. Optionally, outputs are saved to `research_output.txt` for logging.  

### Example Output

```json
{
  "topic": "Quantum Computing",
  "summary": "Quantum computing is a type of computation that utilizes quantum bits...",
  "sources": [
    "https://en.wikipedia.org/wiki/Quantum_computing",
    "https://www.example.com/article"
  ],
  "tools_used": ["WikipediaQueryRun", "DuckDuckGoSearchRun"]
}
```

## Clone Repo and run

```bash
1. git clone https://github.com/yourusername/agentic-ai-research.git
   cd agentic-ai-research

2. pip install -r requirements.txt

3. gemini=YOUR_GOOGLE_GEMINI_KEY

4. python main.py
```
