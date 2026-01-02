import streamlit as st
import PyPDF2
from openai import OpenAI

# --- PAGE SETUP ---
st.set_page_config(page_title="CompliBot Pro", page_icon="⚡", layout="wide")
st.title("⚡ CompliBot: ESG Compliance Auditor")
st.markdown("### Powered by Perplexity (Sonar-Pro)")

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Audit Settings")
    
    # 1. API Key Input
    api_key = st.text_input("Enter Perplexity API Key", type="password")
    
    # 2. THE NEW FRAMEWORK SELECTOR (The "Killer Feature")
    st.divider()
    framework = st.selectbox(
        "Select Reporting Framework",
        ["Generic (Scope 1 & 2)", "CSRD (EU Standard)", "GRI 305 (Global)", "SASB (Industry Specific)"]
    )
    
    # 3. Contextual Help (Shows you know what the standards are)
    if framework == "CSRD (EU Standard)":
        st.info("ℹ️ **CSRD Mode:** Focuses on European Sustainability Reporting Standards (ESRS E1) requirements.")
    elif framework == "GRI 305 (Global)":
        st.info("ℹ️ **GRI Mode:** Focuses on GRI 305-1 (Direct) and 305-2 (Energy Indirect) protocols.")

# --- MAIN APP ---
col1, col2 = st.columns([1, 1])

with col1:
    uploaded_file = st.file_uploader("Upload Report Page (PDF)", type="pdf")

if uploaded_file and api_key:
    try:
        # 1. READ PDF
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text_content = ""
        # Limit to first 2 pages to save credits/speed
        for page in range(min(len(pdf_reader.pages), 2)):
            text_content += pdf_reader.pages[page].extract_text()
            
        with col1:
            st.success(f"✅ Document Loaded: {len(text_content)} characters extracted.")

        if st.button("Run Compliance Audit", type="primary"):
            with col2:
                with st.spinner(f"Analyzing against {framework} protocols..."):
                    
                    # 2. DYNAMIC PROMPT ENGINEERING (The Logic)
                    if framework == "CSRD (EU Standard)":
                        system_prompt = """
                        You are an expert EU ESG Auditor. Analyze the text for CSRD 'ESRS E1' compliance.
                        Extract 'Gross Scope 1' and 'Gross Scope 2' (Market-based) emissions.
                        If data is missing, explicitly state: 'Non-Compliant with ESRS E1'.
                        Output a markdown table with columns: Metric | Value | Unit | Page Ref.
                        """
                    elif framework == "GRI 305 (Global)":
                        system_prompt = """
                        You are a GRI Specialist. Extract data for 'GRI 305-1 (Direct GHG)' and 'GRI 305-2 (Energy Indirect GHG)'.
                        Ensure you distinguish between Location-based and Market-based Scope 2.
                        Output a markdown table with columns: GRI Indicator | Value | Unit | Evidence.
                        """
                    elif framework == "SASB (Industry Specific)":
                        system_prompt = """
                        You are a SASB Analyst. Extract Scope 1 and Scope 2 emissions.
                        Look for 'Activity Metrics' or 'Accounting Metrics' specific to the industry.
                        Output a markdown table.
                        """
                    else: # Generic
                        system_prompt = """
                        You are an expert ESG Auditor. Analyze this text for 'Scope 1' and 'Scope 2' emissions.
                        Output a simple table: Metric | Status | Value | Evidence (Quote).
                        """

                    # 3. CONNECT TO PERPLEXITY
                    client = OpenAI(
                        api_key=api_key,
                        base_url="https://api.perplexity.ai"
                    )

                    # 4. SEND REQUEST
                    response = client.chat.completions.create(
                        model="sonar-pro",
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": f"Here is the report text: \n\n{text_content}"}
                        ]
                    )

                    # 5. DISPLAY RESULT
                    result = response.choices[0].message.content
                    st.markdown(f"### 📊 Audit Results: {framework}")
                    st.markdown(result)
                    
                    # 6. ADD DOWNLOAD BUTTON (Bonus Feature)
                    st.download_button("Download Report", result, file_name="audit_report.md")

    except Exception as e:
        st.error(f"Error: {e}")


















# import streamlit as st
# import PyPDF2
# from openai import OpenAI

# # --- PAGE SETUP ---
# st.set_page_config(page_title="CompliBot Pro", page_icon="⚡")
# st.title("⚡ CompliBot: Powered by Perplexity")

# # --- SIDEBAR ---
# with st.sidebar:
#     st.header("Settings")
#     # You can hardcode your key here for testing if you want, or paste it in the UI
#     api_key = st.text_input("Enter Perplexity API Key", type="password")
#     st.info("Uses 'sonar-pro' model (Smart & Fast)")

# # --- MAIN APP ---
# uploaded_file = st.file_uploader("Upload Any PDF Page", type="pdf")

# if uploaded_file and api_key:
#     try:
#         # 1. READ THE PDF (Text Extraction)
#         pdf_reader = PyPDF2.PdfReader(uploaded_file)
#         text_content = ""
#         # We only read the first 2 pages to save your credits
#         for page in range(min(len(pdf_reader.pages), 2)):
#             text_content += pdf_reader.pages[page].extract_text()
            
#         st.success(f"✅ PDF Loaded. Extracted {len(text_content)} characters.")

#         if st.button("Run Audit"):
#             with st.spinner("Perplexity is analyzing..."):
                
#                 # 2. CONNECT TO PERPLEXITY
#                 client = OpenAI(
#                     api_key=api_key,
#                     base_url="https://api.perplexity.ai"
#                 )

#                 # 3. SEND TO AI
#                 response = client.chat.completions.create(
#                     model="sonar-pro", # This is their best model
#                     messages=[
#                         {
#                             "role": "system",
#                             "content": "You are an expert ESG Auditor. Analyze the text provided. Extract 'Scope 1' and 'Scope 2' emissions. If exact numbers are missing, state 'Not Found'. Output a table."
#                         },
#                         {
#                             "role": "user",
#                             "content": f"Here is the report text: \n\n{text_content}"
#                         }
#                     ]
#                 )

#                 # 4. SHOW RESULT
#                 result = response.choices[0].message.content
#                 st.markdown("### 📊 Audit Results")
#                 st.markdown(result)

#     except Exception as e:
#         st.error(f"Error: {e}")