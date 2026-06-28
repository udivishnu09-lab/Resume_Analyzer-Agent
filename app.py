import streamlit as st
from pdf_parser import extract_text_from_pdf
from agent import analyze_resume

# ── Page Config ─────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Resume Analyzer Agent",
    page_icon="📄",
    layout="wide"
)

# ── Custom CSS ───────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .stButton > button {
        background-color: #4f46e5;
        color: white;
        border-radius: 8px;
        padding: 12px 30px;
        font-size: 16px;
        font-weight: bold;
        border: none;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #4338ca;
    }
    .result-box {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        border-left: 4px solid #4f46e5;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }
    .step-header {
        color: #4f46e5;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .hero {
        text-align: center;
        padding: 30px 0 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# ── Header ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>📄 AI Resume Analyzer Agent</h1>
    <p style="color:#6b7280; font-size:18px;">
        Upload your resume → AI analyzes, scores, and improves it in 5 steps
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── Input Section ────────────────────────────────────────────────────────
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 📤 Upload Your Resume")
    uploaded_file = st.file_uploader(
        "Upload Resume (PDF only)",
        type=["pdf"],
        label_visibility="collapsed"
    )
    if uploaded_file:
        st.success(f"✅ Uploaded: {uploaded_file.name}")

with col2:
    st.markdown("### 🎯 Target Job Role")
    job_role = st.text_input(
        "Enter the job role you are applying for",
        placeholder="e.g. Software Developer, Data Scientist, UI/UX Designer",
        label_visibility="collapsed"
    )

st.markdown("")

# ── Analyze Button ───────────────────────────────────────────────────────
col_btn = st.columns([1, 2, 1])[1]
with col_btn:
    analyze_clicked = st.button("🚀 Analyze My Resume")

# ── Results ─────────────────────────────────────────────────────────────
if analyze_clicked:

    # Validation
    if not uploaded_file:
        st.error("❌ Please upload your resume PDF first.")
        st.stop()

    if not job_role.strip():
        st.error("❌ Please enter a target job role.")
        st.stop()

    # Extract PDF text
    with st.spinner("📖 Reading your resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)

    if resume_text.startswith("ERROR"):
        st.error(resume_text)
        st.stop()

    st.info(f"✅ Resume read successfully — {len(resume_text)} characters extracted")

    # Run Agentic Analysis
    st.markdown("---")
    st.markdown("## 🤖 Agent Analysis Results")
    st.markdown(f"*Analyzing for role: **{job_role}***")
    st.markdown("")

    with st.spinner("🤖 AI Agent working... (may take 20-30 seconds)"):
        results = analyze_resume(resume_text, job_role)

    # ── Display Results ──────────────────────────────────────────────────

    # Step 1 - Skills
    st.markdown("""
    <div class="result-box">
        <div class="step-header">🔍 Step 1 — Skills Extracted from Your Resume</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(results.get("skills", "No data"))

    st.markdown("")

    # Step 2 - Match Analysis
    st.markdown("""
    <div class="result-box">
        <div class="step-header">📊 Step 2 — Job Role Match Analysis</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(results.get("match_analysis", "No data"))

    st.markdown("")

    # Step 3 - ATS Score
    st.markdown("""
    <div class="result-box">
        <div class="step-header">🎯 Step 3 — ATS Score & Feedback</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(results.get("ats_score", "No data"))

    st.markdown("")

    # Step 4 - Improved Summary
    st.markdown("""
    <div class="result-box">
        <div class="step-header">✍️ Step 4 — AI-Rewritten Professional Summary</div>
    </div>
    """, unsafe_allow_html=True)
    st.info(results.get("improved_summary", "No data"))

    st.markdown("")

    # Step 5 - Recommendations
    st.markdown("""
    <div class="result-box">
        <div class="step-header">💡 Step 5 — Top Recommendations to Improve Your Resume</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(results.get("recommendations", "No data"))

    st.markdown("")
    st.success("✅ Analysis complete! Use the recommendations above to improve your resume.")

# ── Footer ───────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#9ca3af; font-size:13px;'>"
    "AI Resume Analyzer Agent • Powered by Google Gemini 1.5 Flash"
    "</p>",
    unsafe_allow_html=True
)
