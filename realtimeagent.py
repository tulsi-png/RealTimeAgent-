import streamlit as st
from langchain.agents import initialize_agent, AgentType
from langchain.tools import DuckDuckGoSearchRun
from langchain_google_genai import ChatGoogleGenerativeAI

# 🔐 HARDCODED Gemini API key (NOT recommended for production!)
GOOGLE_API_KEY = "AIzaSyDtgwOZNPWmJ3cU-RV09cOnnAJAuj8JTxE"  # Replace with your actual key

# 🔌 Set up Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.7
)

# 🔍 Search Tool (DuckDuckGo)
search_tool = DuckDuckGoSearchRun()

# 🤖 Agent Setup with ZERO_SHOT_REACT_DESCRIPTION
agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

# 🎨 Streamlit UI Setup
st.set_page_config(page_title="🧠 Ask Anything – Real-Time AI", page_icon="🌐")
st.title("🧠 Ask Anything – Real-Time AI Assistant")
st.write("Ask questions about **current events**, facts, or anything else! The AI uses Gemini + DuckDuckGo for fresh and accurate info. 🌍")

user_query = st.text_input("🔎 Enter your question below:", placeholder="e.g., What’s the latest update on the Mars mission?")

if st.button("🪄 Get Answer"):
    if not user_query.strip():
        st.warning("❗ Please enter a question.")
    else:
        with st.spinner("Thinking... 🤔"):
            try:
                response = agent.run(user_query)
                st.success("✅ Answer:")
                st.write(response)
            except Exception as e:
                st.error("⚠️ Oops! Something went wrong while fetching the answer.")
                st.exception(e)
