# Amazon Advertising & Sales Intelligence Agent

## Overview

The **Amazon Advertising & Sales Intelligence Agent** is an agentic AI system designed to help Amazon sellers analyze advertising performance and product sales using natural language queries.

Sellers often run advertising campaigns across hundreds of keywords and multiple products. Analyzing performance manually using spreadsheets or dashboards is time-consuming and reactive.

This project builds an **AI-powered analytics assistant** that can:

- Understand natural language questions about sales and advertising
- Analyze advertising performance and sales trends
- Identify wasted ad spend and high-performing keywords
- Connect advertising data with product sales
- Provide actionable recommendations for campaign optimization

The system integrates **LLM reasoning with structured data analysis tools**, enabling users to ask business questions and receive structured insights.

## Problem Statement

Amazon sellers must constantly analyze:

- Which keywords are wasting advertising budget
- Which products are performing best
- Whether sales drops are caused by ads or organic demand
- How advertising spend impacts product revenue

However, this analysis typically requires manual data exploration.

This project solves that problem by creating an **agentic AI system** that can:

1. Understand natural language queries
2. Decide which data to analyze
3. Execute analytical tools
4. Connect insights across multiple datasets
5. Provide structured recommendations

## Key Features

### Natural Language Query Interface

Users can ask questions such as:

- "Which keywords are wasting my advertising budget?"
- "What are my top performing products?"
- "Which products rely most on advertising?"
- "Give recommendations to improve my ad campaigns"

### Agentic AI System

The system uses an **LLM-powered agent** that:

- Understands user intent
- Selects appropriate analytical tools
- Executes data analysis
- Generates insights based on tool outputs

### Dataset Integration

The system analyzes two datasets:

**1. Sales Dataset**

Contains product-level sales information.

Fields include:
* ASIN
* Product Title
* Category
* Date
* Units Sold
* Revenue
* Profit Margin
* BSR Rank
* Stock Level

**2. Advertising Dataset**

Contains keyword-level advertising performance.

Fields include:
* ASIN
* Keyword
* Match Type
* Date
* Impressions
* Clicks
* CPC
* Ad Spend
* Attributed Sales
* ACoS

## System Architecture

```
User Query
   ↓
Streamlit Frontend
   ↓
FastAPI Backend
   ↓
LangChain Agent
   ↓
Analytical Tools
   ↓
Filtered Dataset Processing
   ↓
Structured Results
   ↓
LLM Explanation
```

## Technology Stack

| Component         | Technology   |
| ----------------- | ------------ |
| Frontend          | Streamlit    |
| Backend           | FastAPI      |
| AI Model          | Groq Llama 3 |
| Agent Framework   | LangChain    |
| Data Processing   | Pandas       |
| API Communication | HTTP         |

## Intelligent Data Filtering

Instead of analyzing the entire dataset for every query, the system performs **query-driven filtering**.

Example workflow:

```
User Question
↓
Extract context (time, product, keyword)
↓
Filter relevant subset of dataset
↓
Perform analysis
↓
Return summarized results
↓
LLM generates explanation
```

This ensures scalability and improves performance.

## Analytical Tools

The agent uses four analytical tools.

### 1. Sales Trend Analyzer

Analyzes product sales performance.

Capabilities:

- Identify top-performing products
- Calculate revenue trends
- Analyze units sold

Example question:

```
What are my top performing products by revenue?
```

### 2. Keyword Performance Evaluator

Analyzes advertising keyword performance.

Capabilities:

- Identify high ACoS keywords
- Detect wasted advertising spend
- Evaluate keyword profitability

Example question:

```
Which keywords are wasting my advertising budget?
```

### 3. Spend vs Revenue Analyzer

Connects advertising data with product sales.

Capabilities:

- Calculate advertising contribution to revenue
- Identify products heavily dependent on ads
- Compare organic vs paid performance

Example question:

```
Which products rely most on advertising?
```

### 4. Action Recommender

Provides advertising optimization recommendations.

Capabilities:

- Suggest pausing high ACoS keywords
- Recommend increasing bids for profitable keywords
- Provide campaign improvement strategies

Example question:

```
How can I improve my advertising campaigns?
```

## Project Structure

```
amazon_agent_ai
│
├── api
│   └── main.py
│
├── agent
│   └── advertising_agent.py
│
├── tools
│   ├── sales_trend_analyzer.py
│   ├── keyword_performance_evaluator.py
│   ├── spend_revenue_analyzer.py
│   ├── action_recommender.py
│   ├── data_loader.py
│   └── date_filter.py
│
├── data
│   ├── sales_cleaned.csv
│   └── ads_cleaned.csv
│
├── frontend
│   └── app.py
│
└── README.md
```

## Key Concepts Demonstrated

This project demonstrates several important data and AI engineering concepts:

- Agentic AI systems
- Natural language query interfaces
- Tool-based LLM reasoning
- Cross-dataset analytics
- Query-driven data filtering
- Scalable AI data pipelines
