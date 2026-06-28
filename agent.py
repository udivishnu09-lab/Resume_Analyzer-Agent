import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ✅ Correct model name
model = genai.GenerativeModel("gemini-2.0-flash")

def analyze_resume(resume_text: str, job_role: str) -> dict:
    """
    Agentic AI: Runs multiple steps to analyze and improve the resume.
    Returns a dict with all analysis results.
    """

    results = {}

    # ── STEP 1: Extract Skills ──────────────────────────────────────────
    step1_prompt = f"""
You are a professional resume analyst.

Extract and list the key skills from this resume clearly.
Categorize them as:
- Technical Skills
- Soft Skills
- Tools & Technologies

Resume:
{resume_text}

Respond in clean bullet points.
"""
    try:
        response = model.generate_content(step1_prompt)
        results["skills"] = response.text
    except Exception as e:
        results["skills"] = f"Error extracting skills: {str(e)}"

    # ── STEP 2: Match Against Job Role ──────────────────────────────────
    step2_prompt = f"""
You are a hiring expert for the role: {job_role}

Based on this resume, tell me:
1. What skills MATCH the job role (list them)
2. What skills are MISSING for this role (list them)
3. Overall match percentage (e.g. 65%)

Resume:
{resume_text}

Be specific and actionable.
"""
    try:
        response = model.generate_content(step2_prompt)
        results["match_analysis"] = response.text
    except Exception as e:
        results["match_analysis"] = f"Error in match analysis: {str(e)}"

    # ── STEP 3: ATS Score ───────────────────────────────────────────────
    step3_prompt = f"""
You are an ATS (Applicant Tracking System) expert.

Score this resume out of 100 for the role: {job_role}

Evaluate based on:
- Keyword relevance
- Formatting clarity
- Experience alignment
- Education fit

Resume:
{resume_text}

Give:
- ATS Score: XX/100
- Reason for score
- Top 3 improvements to increase ATS score
"""
    try:
        response = model.generate_content(step3_prompt)
        results["ats_score"] = response.text
    except Exception as e:
        results["ats_score"] = f"Error calculating ATS score: {str(e)}"

    # ── STEP 4: Rewrite Resume Summary ──────────────────────────────────
    step4_prompt = f"""
You are a professional resume writer.

Rewrite the professional summary/objective section of this resume
to perfectly target the role: {job_role}

Make it:
- Strong and impactful (3-4 sentences)
- Keyword-rich for ATS
- Action-oriented

Resume:
{resume_text}

Write ONLY the improved summary. Nothing else.
"""
    try:
        response = model.generate_content(step4_prompt)
        results["improved_summary"] = response.text
    except Exception as e:
        results["improved_summary"] = f"Error rewriting summary: {str(e)}"

    # ── STEP 5: Final Recommendations ───────────────────────────────────
    step5_prompt = f"""
You are a career coach.

Give 5 specific, actionable recommendations to improve this resume
for the role: {job_role}

Number them 1 to 5. Be direct and practical.

Resume:
{resume_text}
"""
    try:
        response = model.generate_content(step5_prompt)
        results["recommendations"] = response.text
    except Exception as e:
        results["recommendations"] = f"Error generating recommendations: {str(e)}"

    return results
