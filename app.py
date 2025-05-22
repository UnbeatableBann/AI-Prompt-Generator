import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
BACKEND_URL = os.getenv("BACKEND_URL")

USER_ID = "user123"

st.set_page_config(page_title="AI Prompt Generator", layout="wide")
st.title("🤖 AI Prompt Generator")


style = st.selectbox("Select tone/style:",
    ["Both (Default)", "Casual", "Formal"],
    index=0)

query = st.text_input("Enter your query:")
col1, col2 = st.columns([2, 1])

with col1:
    if st.button("Generate"):
        if not query:
            st.warning("Please enter a query.")
        else:
            
            with st.spinner("Generating responses..."):   #async feature
                payload = {
                    "user_id": USER_ID,
                    "query": query,
                    "tone": style.lower()
                }

                try:
                    response = requests.post(f"{BACKEND_URL}/generate", json=payload)
                    response.raise_for_status()
                    data = response.json()

                    if style in ["Both (Default)", "Casual"]:
                        st.markdown("### Casual Response")
                        st.info(data.get("casual_response", "No casual response."))

                    if style in ["Both (Default)", "Formal"]:
                        st.markdown("### Formal Response")
                        st.success(data.get("formal_response", "No formal response."))

                    st.success("Responses generated successfully.")

                except requests.exceptions.RequestException as e:
                    st.error(f"Failed to connect to backend. {e}")
                except Exception as e:
                    st.error(f"Error occurred: {e}")

with col2:
    with st.expander("History", expanded=True):
        try:
            history_response = requests.get(f"{BACKEND_URL}/history", params={"user_id": USER_ID})
            history_response.raise_for_status()
            history = history_response.json()

            if not history:
                st.write("No history yet.")
            else:
                for item in reversed(history):
                    st.markdown(f"**Query:** {item['query']}")
                    st.markdown(f"- *{item['created_at']}*")
                    st.markdown(f"**Casual:** {item.get('casual_response', 'N/A')}")
                    st.markdown(f"**Formal:** {item.get('formal_response', 'N/A')}")
                    st.markdown("---")

        except requests.exceptions.RequestException:
            st.warning("⚠️ Could not fetch history. Backend might be offline.")
