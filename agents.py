# agents.py

import os
from crewai import Agent, LLM

# Configure the LLM to use the Groq API
# The model name 'groq/...' tells litellm to use the Groq provider.
llm = LLM(
    model='groq/moonshotai/kimi-k2-instruct-0905',
    api_key=os.environ.get("GROQ_API_KEY")
)


class ResumeAgents:
    def data_extractor(self):
        return Agent(
            role="Resume Information Parser",
            goal="Extract structured information from the resume text into a clean markdown format.",
            backstory="You are a highly accurate, machine-learning-powered resume parser.",
            llm=llm,
            allow_delegation=False,
            verbose=True,
        )

    def ats_analyst(self):
        return Agent(
            role="Advanced ATS Simulator",
            goal="Calculate a precise match percentage between the resume and job description.",
            backstory="You are an advanced Applicant Tracking System (ATS) simulator.",
            llm=llm,
            allow_delegation=False,
            verbose=True,
        )

    def resume_screener(self):
        return Agent(
            role="Resume Evaluation Expert",
            goal="Conduct a comprehensive analysis of the candidate's resume against the job description.",
            backstory="As a world-class resume evaluation expert, you have a keen eye for identifying top talent.",
            llm=llm,
            allow_delegation=False,
            verbose=True,
        )

    def final_report_compiler(self):
        return Agent(
            role="Final Report Compiler",
            goal="Compile all individual analyses into a single, cohesive, and professionally formatted markdown report.",
            backstory="You are a meticulous editor who synthesizes raw outputs into a single, easy-to-read document.",
            llm=llm,
            allow_delegation=False,
            verbose=True,
        )