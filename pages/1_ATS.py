# pages/1_ATS.py

import streamlit as st
import os
import tempfile
from dotenv import load_dotenv
from crewai import Crew, Process

# Load environment variables from .env file
load_dotenv()

# Import your agent and task classes
from agents import ResumeAgents
from tasks import ResumeTasks

# --- Streamlit Page Setup ---
st.set_page_config(page_title="ATS Resume Expert", layout="wide")
st.title("ATS Resume Analyzer")
st.markdown("Get instant, AI-powered feedback on your resume. Upload your resume and paste a job description to see how you stack up.")

# --- Main App Logic ---
uploaded_file = st.file_uploader(
    "Upload your resume (PDF)...",
    type=["pdf"],
    help="The entire document will be analyzed by a team of AI agents."
)
job_description = st.text_area(
    "Paste the full job description here...",
    height=300,
    help="For the best results, provide the complete job description."
)

if st.button("Analyze Resume", type="primary", use_container_width=True):
    if uploaded_file is not None and job_description:
        # Create a temporary file to store the uploaded PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
            tmpfile.write(uploaded_file.getvalue())
            temp_file_path = tmpfile.name

        with st.spinner("Your team of AI agents is analyzing the resume... This may take a moment."):
            try:
                # --- CrewAI Logic ---
                agents = ResumeAgents()
                tasks = ResumeTasks()

                # Agent Instances
                data_extractor_agent = agents.data_extractor()
                ats_analyst_agent = agents.ats_analyst()
                resume_screener_agent = agents.resume_screener()
                final_compiler_agent = agents.final_report_compiler()

                # Task Instances
                parser_task = tasks.resume_parser_task(data_extractor_agent, temp_file_path)
                match_task = tasks.percentage_match_task(ats_analyst_agent, temp_file_path, job_description, context=[parser_task])
                summary_task = tasks.fit_summary_task(resume_screener_agent, temp_file_path, job_description, context=[match_task])
                report_task = tasks.final_report_task(final_compiler_agent, context=[parser_task, match_task, summary_task])
                
                # Assemble the crew
                crew = Crew(
                    agents=[data_extractor_agent, ats_analyst_agent, resume_screener_agent, final_compiler_agent],
                    tasks=[parser_task, match_task, summary_task, report_task],
                    process=Process.sequential,
                    verbose=True,
                )

                # Kick off the analysis
                final_result = crew.kickoff()
                
                st.success("Analysis Complete!")
                st.markdown("---")
                st.header("Comprehensive Resume Analysis Report")
                st.markdown(final_result)

            except Exception as e:
                st.error(f"An unexpected error occurred during analysis: {e}")
            finally:
                # Clean up the temporary file
                os.remove(temp_file_path)

    elif uploaded_file is None:
        st.warning("Please upload your resume to begin analysis.")
    else:
        st.warning("Please paste the job description to begin analysis.")