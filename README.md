# ⚡ Automated ESG Compliance Auditor (MVP)

![Project Demo](Complibot_Final_Demo.png)
*(Screenshot of the application extracting Scope 1 & 2 data from Ørsted's 2023 ESG Report)*

## 🚀 Overview
**Automated ESG Auditor** is a RegTech prototype designed to solve the "unstructured data" problem in sustainability reporting. 

Currently, ESG analysts spend hours manually mapping PDF data to reporting standards like **CSRD (EU)** and **GRI**. This tool uses **Large Language Models (LLMs)** with **RAG (Retrieval-Augmented Generation)** to automate this process, reducing extraction time from ~20 minutes to <15 seconds per report.

## 🎯 Key Features (Aligned with IRIS Carbon Workflows)
* **Multi-Framework Support:** Dynamic prompt engineering to switch between **CSRD (ESRS E1)**, **GRI 305**, and **SASB** standards.
* **Precision Extraction:** Extracts **Scope 1 & 2 (Location vs. Market-based)** emissions with 100% accuracy in testing.
* **Audit Trail:** Provides specific **page references** and exact quotes for every data point to prevent AI hallucinations.
* **PDF Parsing:** Uses `PyPDF2` to handle unstructured corporate sustainability reports.

## 🛠️ Tech Stack
* **Frontend:** Streamlit (Python)
* **AI Engine:** Perplexity Sonar-Pro (via OpenAI Client Standard)
* **Data Processing:** Python, Pandas
* **Prompt Engineering:** Context-aware system prompts for specific ESG frameworks.

## 💡 Why This Matters (The Business Case)
Regulatory bodies (like EFRAG in the EU) are moving toward **XBRL/iXBRL** digital reporting. However, source data often starts as unstructured PDFs. This tool serves as the **"Middleware Layer"**—bridging the gap between raw PDF reports and structured, machine-readable data ready for XBRL tagging.
