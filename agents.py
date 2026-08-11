from swarm import Agent


# ==========================================================
# RESUME ANALYSIS AGENT
# ==========================================================

resume_agent = Agent(
    name="Resume Analysis Agent",
    instructions="""
    Analyze the resume.

    Give ONLY these 4 items:
    1. Education
    2. Experience
    3. Main Projects
    4. One Strength and One Weakness

    Use short bullet points.
    Maximum 6 bullet points total.
    Do not rewrite the resume.
    Do not add explanations.
    Do not invent information.
    """
)


# ==========================================================
# SKILLS ANALYSIS AGENT
# ==========================================================

skills_agent = Agent(
    name="Skills Analysis Agent",
    instructions="""
    Analyze the resume.

    Give ONLY:
    1. Technical Skills
    2. Soft Skills
    3. Two Recommended Skills to Learn

    Use short bullet points.
    Maximum 6 bullet points total.
    Do not explain each skill.
    Do not rewrite the resume.
    Do not invent information.
    """
)


# ==========================================================
# CAREER RECOMMENDATION AGENT
# ==========================================================

career_agent = Agent(
    name="Career Recommendation Agent",
    instructions="""
    Analyze the resume.

    Give ONLY:
    1. Three suitable entry-level job roles
    2. Two resume improvement suggestions

    Use short bullet points.
    Maximum 5 bullet points total.
    Keep the recommendations realistic for a beginner.
    Do not rewrite the resume.
    Do not add a sample resume.
    Do not invent qualifications.
    """
)