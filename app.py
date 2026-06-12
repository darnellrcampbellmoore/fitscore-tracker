import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="FitScore Tracker", page_icon="🎯", layout="centered")

# 2. Main Dashboard Header
st.title("🎯 FitScore Tracker")
st.markdown("Upload your job details, resume, and interview notes to get an AI-powered confidence score.")
st.divider()

# 3. The Profile Switcher
st.header("1. Select Your Career Track")
st.markdown("Tune the AI's evaluation criteria based on the role you are applying for.")
career_track = st.selectbox(
    "Which profile are you applying with?",
    ["Select a track...", "Research Industry", "Pharma Industry", "Consultancy", "MSL", "School/Education"]
)

# 4. The Document Hub (Only shows up after a track is selected)
if career_track != "Select a track...":
    st.success(f"Profile loaded! The Scoring Engine is now tuned for {career_track} roles.")
    
    st.header("2. Document Hub")
    
    # Side-by-side file uploaders
    col1, col2 = st.columns(2)
    with col1:
        job_description = st.file_uploader("Upload Job Description", type=["pdf", "txt"])
    with col2:
        resume = st.file_uploader("Upload Your Resume", type=["pdf", "txt"])
        
    # Text area for interview transcripts
    st.subheader("Interview Notes")
    interview_notes = st.text_area("Paste your interview transcripts, thoughts, or prompt notes here:")
    
    # 5. The Scoring Engine Trigger
    st.divider()
    if st.button("Calculate FitScore (1-100)", type="primary"):
        st.info("Brain loading... We will connect the free Gemini AI Engine to this button next!")