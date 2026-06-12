import streamlit as st
from google import genai

# 1. Page Configuration
st.set_page_config(page_title="FitScore Tracker", page_icon="🎯", layout="centered")

# 2. Main Dashboard Header
st.title("🎯 FitScore Tracker")
st.markdown("Upload your job details, resume, and interview notes to get an AI-powered confidence score.")
st.divider()

# 3. The Profile Switcher
st.header("1. Select Your Career Track")
career_track = st.selectbox(
    "Which profile are you applying with?",
    ["Select a track...", "Research Industry", "Pharma Industry", "Consultancy", "MSL", "School/Education"]
)

# 4. The Document Hub 
if career_track != "Select a track...":
    st.success(f"Profile loaded! The Scoring Engine is now tuned for {career_track} roles.")
    
    st.header("2. Document Hub")
    
    col1, col2 = st.columns(2)
    with col1:
        job_description = st.file_uploader("Upload Job Description (.txt)", type=["txt"])
    with col2:
        resume = st.file_uploader("Upload Your Resume (.txt)", type=["txt"])
        
    st.subheader("Interview Notes")
    interview_notes = st.text_area("Paste your interview transcripts, thoughts, or prompt notes here:")
    
    # 5. The Scoring Engine Trigger
    st.divider()
    if st.button("Calculate FitScore (1-100)", type="primary"):
        if job_description is None or resume is None:
            st.error("Please upload both a Job Description and a Resume (.txt files) to run the engine!")
        else:
            with st.spinner("Brain is processing..."):
                try:
                    # Extract the text from the uploaded .txt files
                    job_text = job_description.getvalue().decode("utf-8")
                    resume_text = resume.getvalue().decode("utf-8")
                    
                    # Wake up the Gemini Client using our Secret Vault
                    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
                    
                    # The Prompt for the AI
                    prompt_instructions = f"""
                    You are an expert career coach evaluating a candidate for a {career_track} role.
                    
                    Here is the Job Description:
                    {job_text}
                    
                    Here is the Candidate's Resume:
                    {resume_text}
                    
                    Here are their Interview Notes:
                    {interview_notes}
                    
                    Based on these documents, provide:
                    1. A 'FitScore' from 1 to 100 on how likely they are to get the job.
                    2. Three brief, actionable tips on what to improve or emphasize.
                    """
                    
                    # Send it to Gemini
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt_instructions
                    )
                    
                    # Show the results!
                    st.subheader("🎯 Your FitScore Results")
                    st.write(response.text)
                    
                except Exception as e:
                    st.error(f"Something went wrong: {e}")
