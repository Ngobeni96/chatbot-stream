# Install Streamlit first: pip install streamlit
import streamlit as st

st.title("🎓 Career Guidance Chatbot")

interests = st.text_input("🔍 What are your interests?")
skills = st.text_input("🛠️ What are your strongest skills?")
subjects = st.text_input("📚 What are your favorite subjects?")

if st.button("Get Career Suggestion"):
    result = ""
    if "technology" in interests or "coding" in skills or "math" in subjects:
        result = "💡 Suggested Career: Software Developer, Data Analyst, or AI Engineer."
    elif "helping" in interests or "communication" in skills or "life science" in subjects:
        result = "💡 Suggested Career: Nurse, Psychologist, or Social Worker."
    elif "business" in interests or "leadership" in skills or "economics" in subjects:
        result = "💡 Suggested Career: Entrepreneur, Marketing Manager, or Financial Analyst."
    elif "creativity" in interests or "design" in skills or "art" in subjects:
        result = "💡 Suggested Career: Graphic Designer, Content Creator, or Architect."
    else:
        result = "💡 Suggested Career: Teacher, Consultant, or Project Manager."
    
    st.success(result)

