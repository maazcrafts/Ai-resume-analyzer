import streamlit as st
from swarm import Swarm
from openai import OpenAI
from agents import resume_agent, skills_agent, career_agent

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>
.block-container {
    max-width: 1180px;
    padding-top: 2rem;
}

.hero {
    background: linear-gradient(135deg, #312e81, #7c3aed);
    padding: 34px;
    border-radius: 18px;
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 42px;
    margin: 0;
}

.hero p {
    font-size: 17px;
    margin-top: 8px;
}

.info-card {
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
    min-height: 150px;
}

.result-card {
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
    margin-bottom: 16px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:
    st.markdown("## 📄 AI Resume Analyzer")
    st.caption("AI-Powered Resume Analysis System")

    st.divider()

    st.markdown("### AI Model")
    st.write("Llama 3.2")

    st.markdown("### AI Framework")
    st.write("Swarm")

    st.markdown("### Agents")
    st.write("3 AI Agents")

    st.divider()
    st.success("System Status: Ready")

# =========================================================
# HERO
# =========================================================
st.markdown("""
<div class="hero">
    <h1>📄 AI Resume Analyzer</h1>
    <p>Analyze your resume using multiple AI agents powered by Llama 3.2 and Swarm.</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# METRICS
# =========================================================
c1, c2, c3, c4 = st.columns(4)

c1.metric("AI Agents", "3")
c2.metric("AI Model", "Llama 3.2")
c3.metric("Framework", "Swarm")
c4.metric("Input", "TXT Resume")

st.write("")

# =========================================================
# UPLOAD
# =========================================================
st.markdown("### 📤 Upload Your Resume")

uploaded_file = st.file_uploader(
    "Choose your resume",
    type=["txt"],
    help="Upload your resume as a .txt file."
)

if uploaded_file is not None:
    st.success(f"Resume loaded: {uploaded_file.name}")

st.caption("Supported format: .txt")

# =========================================================
# ANALYSIS
# =========================================================
if st.button(
    "🚀 Analyze Resume",
    type="primary",
    use_container_width=True
):
    if uploaded_file is None:
        st.warning("Please upload a resume first.")
    else:
        try:
            resume_text = uploaded_file.read().decode("utf-8")

            if not resume_text.strip():
                st.warning("The uploaded resume is empty.")
                st.stop()

            # Local Ollama OpenAI-compatible endpoint
            client = OpenAI(
                base_url="http://localhost:11434/v1",
                api_key="ollama"
            )

            swarm_client = Swarm(client=client)

            # Resume analysis
            with st.spinner("🔎 Resume Analysis Agent is working..."):
                response = swarm_client.run(
                    agent=resume_agent,
                    messages=[
                        {
                            "role": "user",
                            "content": resume_text
                        }
                    ],
                    model_override="llama3.2"
                )
                resume_analysis = response.messages[-1]["content"]

            # Skills analysis
            with st.spinner("🛠️ Skills Analysis Agent is working..."):
                response = swarm_client.run(
                    agent=skills_agent,
                    messages=[
                        {
                            "role": "user",
                            "content": resume_text
                        }
                    ],
                    model_override="llama3.2"
                )
                skills_analysis = response.messages[-1]["content"]

            # Career recommendations
            with st.spinner("💼 Career Recommendation Agent is working..."):
                response = swarm_client.run(
                    agent=career_agent,
                    messages=[
                        {
                            "role": "user",
                            "content": resume_text
                        }
                    ],
                    model_override="llama3.2"
                )
                career_recommendations = response.messages[-1]["content"]

            st.success("Resume analysis completed successfully!")

            # =================================================
            # RESULTS
            # =================================================
            st.markdown("### 📋 Resume Analysis")
            st.markdown(
                f'<div class="result-card">{resume_analysis}</div>',
                unsafe_allow_html=True
            )

            st.markdown("### 🛠️ Skills Analysis")
            st.markdown(
                f'<div class="result-card">{skills_analysis}</div>',
                unsafe_allow_html=True
            )

            st.markdown("### 💼 Career Recommendations")
            st.markdown(
                f'<div class="result-card">{career_recommendations}</div>',
                unsafe_allow_html=True
            )

            # =================================================
            # RESUME PREVIEW
            # =================================================
            with st.expander("📄 View Uploaded Resume"):
                st.text(resume_text)

        except Exception as e:
            st.error("An error occurred while analyzing the resume.")
            st.code(str(e))
            st.info(
                "Make sure Ollama is running and the llama3.2 model is available."
            )

# =========================================================
# HOW IT WORKS
# =========================================================
st.write("")
st.markdown("### ⚙️ How It Works")

a, b, c = st.columns(3)

with a:
    st.markdown("""
    <div class="info-card">
    <h4>📋 Resume Agent</h4>
    Analyzes education, experience, projects, and one strength and weakness.
    </div>
    """, unsafe_allow_html=True)

with b:
    st.markdown("""
    <div class="info-card">
    <h4>🛠️ Skills Agent</h4>
    Identifies technical and soft skills and recommends two skills to learn.
    </div>
    """, unsafe_allow_html=True)

with c:
    st.markdown("""
    <div class="info-card">
    <h4>💼 Career Agent</h4>
    Suggests suitable entry-level roles and resume improvements.
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.caption(
    "AI Resume Analyzer • Python • Streamlit • Swarm • Ollama • Llama 3.2"
)