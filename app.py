import streamlit as st
from resume_parser import extract_resume_text

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
st.markdown("<h1 style='text-align: center;'>📄 AI Resume Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Get ATS score, feedback, and suggestions instantly</p>", unsafe_allow_html=True)
st.markdown("---")

st.title("🧠 AI Resume Analyzer")
st.markdown("Upload your resume in PDF format to get feedback and ATS score.")

uploaded_file = st.file_uploader("Upload Resume (PDF only)", type="pdf")

if uploaded_file is not None:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    text = extract_resume_text("temp_resume.pdf")

    st.subheader("📄 Extracted Resume Text")
    st.text_area("Resume Content", text, height=400)
from ats_score import generate_feedback_with_gpt

if uploaded_file is not None:
    st.subheader("🧠 AI Feedback on Resume")

    if st.button("Analyze Resume"):
        with st.spinner("Analyzing..."):
            feedback = generate_feedback_with_gpt(text)
            st.markdown("### 🔍 ATS Feedback")
            st.markdown(feedback)

    from pdf_generator import create_pdf_report

    if st.button("📥 Download PDF Report"):
        pdf_path = create_pdf_report(text=generate_feedback_with_gpt(text))
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="Download Feedback as PDF",
                data=f,
                file_name="Resume_Feedback.pdf",
                mime="application/pdf"
            )
