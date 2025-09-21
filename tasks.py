# tasks.py

from crewai import Task
from textwrap import dedent
from tools.file_read_tool import read_pdf_content

class ResumeTasks:
    def resume_parser_task(self, agent, resume_file_path: str):
        resume_content = read_pdf_content(resume_file_path)
        return Task(
            description=dedent(f"""
                Parse the resume content below and extract all key information into a structured markdown format.
                This is the first step, so focus solely on accurate extraction.

                **Resume Content:**
                ---
                {resume_content}
                ---
            """),
            expected_output=dedent("""
                A clean, well-organized markdown output with the following sections extracted from the resume (if present):
                - **Contact Information**
                - **Professional Summary/Objective**
                - **Work Experience**
                - **Education**
                - **Technical Skills**
                - **Projects**
                - **Certifications & Awards**
            """),
            agent=agent,
        )

    def percentage_match_task(self, agent, resume_file_path: str, job_description: str, context: list):
        resume_content = read_pdf_content(resume_file_path)
        return Task(
            description=dedent(f"""
                Using the parsed resume data and the job description below, calculate a precise ATS match percentage.
                Provide a brief rationale for the score based on keyword overlap, skills, and experience.

                **Job Description:**
                ---
                {job_description}
                ---

                **Resume Content:**
                ---
                {resume_content}
                ---
            """),
            expected_output=dedent("""
                A concise report with only two sections:
                1.  **Match Percentage (0–100%):** The calculated score.
                2.  **Rationale:** 3-4 bullet points explaining the factors influencing the score.
            """),
            agent=agent,
            context=context,
        )

    def fit_summary_task(self, agent, resume_file_path: str, job_description: str, context: list):
        resume_content = read_pdf_content(resume_file_path)
        return Task(
            description=dedent(f"""
                Based on the parsed resume, the ATS score, and the job description, create a comprehensive 'Fit Summary & Analysis'.
                Highlight strengths, weaknesses, and alignment with the role.

                **Job Description:**
                ---
                {job_description}
                ---
                
                **Resume Content:**
                ---
                {resume_content}
                ---
            """),
            expected_output=dedent("""
                A detailed, professional markdown report containing:
                1.  **Overall Fit Summary:** A concise paragraph on the candidate's suitability.
                2.  **Skill Match Analysis:** A list of required skills marked with ✔️ or ❌.
                3.  **Experience Relevance:** A brief analysis of work history alignment.
                4.  **Actionable Improvement Suggestions:** Specific advice for tailoring the resume.
            """),
            agent=agent,
            context=context,
        )
    
    def final_report_task(self, agent, context: list):
        return Task(
            description=dedent("""
                Compile all the preceding analyses into a single, cohesive, and professionally formatted final report.
                The report should be well-structured with clear headings for each section.
                The sections should be:
                1. Parsed Resume Information
                2. ATS Match Score & Rationale
                3. Overall Fit Summary & Analysis
                
                Combine the outputs from the previous tasks into this final document.
            """),
            expected_output=dedent("""
                A single, comprehensive markdown document that includes all analysis sections,
                formatted cleanly for final presentation. Use headings, bullet points, and bold text
                to make the report easy to read.
            """),
            agent=agent,
            context=context,
        )