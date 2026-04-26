import streamlit as st

# ── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Jakuan Ahmed · Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Syne:wght@400;600;700;800&display=swap');

/* ─── Reset & Base ─── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    background: #0a0a0f !important;
    color: #e8e8f0 !important;
    font-family: 'Syne', sans-serif !important;
}

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(ellipse 80% 50% at 20% 0%, rgba(0,255,136,0.07) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 100%, rgba(0,180,255,0.06) 0%, transparent 60%),
        #0a0a0f !important;
}

[data-testid="stHeader"] { background: transparent !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none !important; }

/* ─── Hide Streamlit chrome ─── */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }

/* ─── Scrollbar ─── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #0a0a0f; }
::-webkit-scrollbar-thumb { background: #00ff88; border-radius: 2px; }

/* ─── Typography ─── */
h1, h2, h3, h4 { font-family: 'Syne', sans-serif !important; }
code, pre { font-family: 'Space Mono', monospace !important; }

/* ─── Wrapper ─── */
.port-wrap {
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 32px 80px;
}

/* ════════════════════════════════════════════
   HERO
════════════════════════════════════════════ */
.hero {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 80px 0 60px;
    position: relative;
    overflow: hidden;
}

.hero::before {
    content: '';
    position: absolute;
    top: -60px; right: -120px;
    width: 520px; height: 520px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(0,255,136,0.12) 0%, transparent 70%);
    pointer-events: none;
}

.hero-tag {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #00ff88;
    background: rgba(0,255,136,0.08);
    border: 1px solid rgba(0,255,136,0.25);
    padding: 6px 14px;
    border-radius: 2px;
    margin-bottom: 28px;
    display: inline-block;
}

.hero-name {
    font-family: 'Syne', sans-serif;
    font-size: clamp(52px, 8vw, 96px);
    font-weight: 800;
    line-height: 0.95;
    letter-spacing: -3px;
    color: #e8e8f0;
    margin-bottom: 20px;
}

.hero-name span {
    color: transparent;
    -webkit-text-stroke: 1.5px rgba(232,232,240,0.4);
}

.hero-role {
    font-family: 'Space Mono', monospace;
    font-size: 15px;
    color: #7878a0;
    margin-bottom: 28px;
    letter-spacing: 1px;
}

.hero-role b { color: #00ff88; }

.hero-summary {
    font-size: 17px;
    line-height: 1.7;
    color: #a0a0c0;
    max-width: 560px;
    margin-bottom: 40px;
}

.hero-links {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
}

.hero-link {
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: #e8e8f0;
    text-decoration: none;
    border: 1px solid rgba(232,232,240,0.2);
    padding: 10px 20px;
    border-radius: 2px;
    transition: all 0.2s;
    background: rgba(255,255,255,0.03);
}

.hero-link:hover, .hero-link.primary {
    background: #00ff88;
    color: #0a0a0f;
    border-color: #00ff88;
}

.hero-meta {
    margin-top: 40px;
    display: flex;
    gap: 32px;
    flex-wrap: wrap;
}

.hero-stat {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.hero-stat-num {
    font-family: 'Syne', sans-serif;
    font-size: 32px;
    font-weight: 800;
    color: #00ff88;
    line-height: 1;
}

.hero-stat-label {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    color: #5555777;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #606080;
}

/* ════════════════════════════════════════════
   SECTION HEADER
════════════════════════════════════════════ */
.section-header {
    display: flex;
    align-items: center;
    gap: 16px;
    margin: 60px 0 32px;
}

.section-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(to right, rgba(0,255,136,0.3), transparent);
}

.section-title {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #00ff88;
    white-space: nowrap;
}

/* ════════════════════════════════════════════
   SKILLS
════════════════════════════════════════════ */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 16px;
}

.skill-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 8px;
    padding: 20px;
    transition: all 0.25s;
    cursor: default;
}

.skill-card:hover {
    border-color: rgba(0,255,136,0.3);
    background: rgba(0,255,136,0.04);
    transform: translateY(-2px);
}

.skill-card-label {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #00ff88;
    margin-bottom: 12px;
    display: block;
}

.skill-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
}

.skill-tag {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: #a0a0c0;
    background: rgba(255,255,255,0.05);
    padding: 3px 8px;
    border-radius: 2px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* ════════════════════════════════════════════
   EXPERIENCE
════════════════════════════════════════════ */
.exp-card {
    border-left: 2px solid #00ff88;
    padding: 24px 28px;
    background: rgba(0,255,136,0.03);
    border-radius: 0 8px 8px 0;
    margin-bottom: 20px;
    transition: all 0.25s;
}

.exp-card:hover {
    background: rgba(0,255,136,0.06);
    transform: translateX(4px);
}

.exp-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 6px;
}

.exp-role {
    font-family: 'Syne', sans-serif;
    font-size: 20px;
    font-weight: 700;
    color: #e8e8f0;
}

.exp-company {
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    color: #00ff88;
    font-weight: 700;
}

.exp-period {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: #606080;
    letter-spacing: 1px;
}

.exp-bullets {
    list-style: none;
    margin-top: 14px;
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.exp-bullets li {
    font-size: 14px;
    color: #8888a8;
    line-height: 1.6;
    padding-left: 18px;
    position: relative;
}

.exp-bullets li::before {
    content: '▸';
    position: absolute;
    left: 0;
    color: #00ff88;
    font-size: 12px;
}

/* ════════════════════════════════════════════
   PROJECTS
════════════════════════════════════════════ */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 20px;
}

.project-card {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    padding: 28px;
    transition: all 0.25s;
    position: relative;
    overflow: hidden;
}

.project-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(to right, #00ff88, #00b4ff);
    opacity: 0;
    transition: opacity 0.25s;
}

.project-card:hover {
    border-color: rgba(0,255,136,0.25);
    background: rgba(0,255,136,0.03);
    transform: translateY(-4px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.3);
}

.project-card:hover::before { opacity: 1; }

.project-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 14px;
}

.project-name {
    font-family: 'Syne', sans-serif;
    font-size: 20px;
    font-weight: 700;
    color: #e8e8f0;
}

.project-star {
    font-size: 14px;
    color: #ffd700;
}

.project-link-btn {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: #00ff88;
    text-decoration: none;
    border: 1px solid rgba(0,255,136,0.3);
    padding: 5px 12px;
    border-radius: 2px;
    transition: all 0.2s;
}

.project-link-btn:hover {
    background: #00ff88;
    color: #0a0a0f;
}

.project-desc {
    font-size: 14px;
    line-height: 1.65;
    color: #7878a0;
    margin-bottom: 16px;
}

.project-stack {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
}

.stack-tag {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    color: #00b4ff;
    background: rgba(0,180,255,0.08);
    border: 1px solid rgba(0,180,255,0.2);
    padding: 3px 8px;
    border-radius: 2px;
}

/* ════════════════════════════════════════════
   EDUCATION
════════════════════════════════════════════ */
.edu-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 16px;
}

.edu-card {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    padding: 24px;
    transition: all 0.25s;
}

.edu-card:hover {
    border-color: rgba(0,180,255,0.3);
    background: rgba(0,180,255,0.04);
    transform: translateY(-2px);
}

.edu-degree {
    font-family: 'Syne', sans-serif;
    font-size: 17px;
    font-weight: 700;
    color: #e8e8f0;
    margin-bottom: 8px;
    line-height: 1.3;
}

.edu-school {
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    color: #00b4ff;
    margin-bottom: 6px;
}

.edu-period {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: #505070;
    letter-spacing: 1px;
    margin-bottom: 10px;
}

.edu-note {
    font-size: 13px;
    color: #7878a0;
    line-height: 1.5;
}

/* ════════════════════════════════════════════
   ACHIEVEMENTS
════════════════════════════════════════════ */
.ach-list {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.ach-item {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    padding: 18px 22px;
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 8px;
    transition: all 0.2s;
}

.ach-item:hover {
    border-color: rgba(0,255,136,0.2);
    background: rgba(0,255,136,0.03);
}

.ach-icon { font-size: 22px; flex-shrink: 0; }

.ach-text {
    font-size: 15px;
    color: #a0a0c0;
    line-height: 1.5;
}

/* ════════════════════════════════════════════
   CONTACT
════════════════════════════════════════════ */
.contact-bar {
    margin-top: 60px;
    padding: 36px;
    border: 1px solid rgba(0,255,136,0.15);
    border-radius: 12px;
    background: rgba(0,255,136,0.03);
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
}

.contact-left h3 {
    font-family: 'Syne', sans-serif;
    font-size: 24px;
    font-weight: 800;
    color: #e8e8f0;
    margin-bottom: 6px;
}

.contact-left p {
    font-size: 14px;
    color: #7878a0;
}

.contact-links {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.contact-link {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: #e8e8f0;
    text-decoration: none;
    border: 1px solid rgba(232,232,240,0.15);
    padding: 10px 18px;
    border-radius: 4px;
    transition: all 0.2s;
    background: rgba(255,255,255,0.03);
}

.contact-link:hover {
    background: #00ff88;
    color: #0a0a0f;
    border-color: #00ff88;
}

/* ─── Footer ─── */
.footer {
    text-align: center;
    margin-top: 60px;
    padding: 24px 0;
    border-top: 1px solid rgba(255,255,255,0.05);
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: #404060;
    letter-spacing: 1px;
}
</style>
""", unsafe_allow_html=True)

# ── Data ──────────────────────────────────────────────────────────────────────
SKILLS = {
    "Languages": ["TypeScript", "JavaScript", "Python", "C", "C++"],
    "Frontend": ["React.js", "Next.js", "Tailwind CSS", "Shadcn/UI", "Zustand"],
    "Backend": ["Node.js", "Express.js", "REST API", "JWT", "Prisma"],
    "Databases": ["MongoDB", "Mongoose", "MySQL"],
    "Cloud & DevOps": ["AWS EC2", "AWS S3", "Nginx", "VPS", "SSH", "Git", "Vercel"],
    "AI/ML (Learning)": ["Python", "NumPy", "Pandas", "scikit-learn", "ML Fundamentals"],
}

PROJECTS = [
    {
        "name": "Admission Mirror",
        "star": True,
        "url": "https://admission-mirror.vercel.app",
        "desc": "Full-featured university admission prep platform covering 11+ universities — exam simulation engine with timer, review & analytics, 8-week study plans, and practice games (flashcards, quiz, formula sprint).",
        "stack": ["Next.js", "TypeScript", "MongoDB", "Tailwind", "Zustand", "JWT", "Python (Scraper)"],
    },
    {
        "name": "DubaiPulse",
        "star": False,
        "url": "https://arteventsdubai.com",
        "desc": "Dubai event & e-commerce platform with role-based admin panel, online shop, courses, and gallery — deployed on AWS EC2 with Nginx and Prisma ORM for type-safe queries.",
        "stack": ["Next.js", "TypeScript", "Prisma", "MongoDB", "AWS EC2", "Nginx"],
    },
]

# ── Render ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="port-wrap">', unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <span class="hero-tag">⚡ Available for opportunities</span>
    <h1 class="hero-name">JAKUAN<br><span>AHMED</span></h1>
    <p class="hero-role"><b>Software Engineer</b> &nbsp;·&nbsp; AI/ML Enthusiast &nbsp;·&nbsp; Sylhet, Bangladesh</p>
    <p class="hero-summary">
        Full-stack engineer delivering production-grade systems using TypeScript, React, Next.js, and Node.js.
        Skilled in scalable REST APIs, cloud deployment on AWS, and modular architecture.
        Currently expanding into AI/ML to build intelligent, data-driven products.
    </p>
    <div class="hero-links">
        <a class="hero-link primary" href="mailto:jakuanultimate777@gmail.com">✉ Email Me</a>
        <a class="hero-link" href="https://github.com/JAKUAN-AHMED" target="_blank">GitHub</a>
        <a class="hero-link" href="https://linkedin.com/in/jakuan-ahmed-0514932a3" target="_blank">LinkedIn</a>
        <a class="hero-link" href="http://jakuan-ahmed.vercel.app" target="_blank">Portfolio</a>
    </div>
    <div class="hero-meta">
        <div class="hero-stat">
            <span class="hero-stat-num">12+</span>
            <span class="hero-stat-label">Production Projects</span>
        </div>
        <div class="hero-stat">
            <span class="hero-stat-num">1+</span>
            <span class="hero-stat-label">Year Experience</span>
        </div>
        <div class="hero-stat">
            <span class="hero-stat-num">11+</span>
            <span class="hero-stat-label">Universities Covered</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SKILLS ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <span class="section-title">Technical Skills</span>
    <div class="section-line"></div>
</div>
<div class="skills-grid">
""", unsafe_allow_html=True)

for category, tags in SKILLS.items():
    tags_html = "".join(f'<span class="skill-tag">{t}</span>' for t in tags)
    st.markdown(f"""
    <div class="skill-card">
        <span class="skill-card-label">{category}</span>
        <div class="skill-tags">{tags_html}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── EXPERIENCE ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <span class="section-title">Work Experience</span>
    <div class="section-line"></div>
</div>
<div class="exp-card">
    <div class="exp-top">
        <div>
            <div class="exp-role">Software Developer</div>
            <div class="exp-company">Betopia Group</div>
        </div>
        <div class="exp-period">APR 2025 – PRESENT &nbsp;·&nbsp; REMOTE</div>
    </div>
    <ul class="exp-bullets">
        <li>Built optimized RESTful APIs with modular architecture using Node.js, Express.js, and MongoDB; deployed on VPS via SSH with Nginx as reverse proxy.</li>
        <li>Delivered 12+ full-stack client projects on schedule; implemented JWT authentication, role-based access control, and AWS S3 for file/media storage.</li>
        <li>Collaborated with design and product teams using agile workflows to ship features with high client satisfaction.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ── PROJECTS ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <span class="section-title">Projects</span>
    <div class="section-line"></div>
</div>
<div class="projects-grid">
""", unsafe_allow_html=True)

for p in PROJECTS:
    star_html = '<span class="project-star">★ Featured</span>' if p["star"] else ""
    stack_html = "".join(f'<span class="stack-tag">{t}</span>' for t in p["stack"])
    st.markdown(f"""
    <div class="project-card">
        <div class="project-top">
            <div>
                <div class="project-name">{p['name']}</div>
                {star_html}
            </div>
            <a class="project-link-btn" href="{p['url']}" target="_blank">↗ Live</a>
        </div>
        <p class="project-desc">{p['desc']}</p>
        <div class="project-stack">{stack_html}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── EDUCATION ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <span class="section-title">Education</span>
    <div class="section-line"></div>
</div>
<div class="edu-grid">
    <div class="edu-card">
        <div class="edu-degree">BSc, Computer Science &amp; Engineering</div>
        <div class="edu-school">University of the People — USA (Online)</div>
        <div class="edu-period">2025 – 2029 (Expected)</div>
    </div>
    <div class="edu-card">
        <div class="edu-degree">Diploma, Computer Science &amp; Technology</div>
        <div class="edu-school">Moulvibazar Polytechnic Institute, Sylhet</div>
        <div class="edu-period">2022 – 2026 (Expected)</div>
        <div class="edu-note">GPA 3.60 / 4.00 &nbsp;·&nbsp; Class Representative (7×) &nbsp;·&nbsp; Programming Mentor</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── ACHIEVEMENTS ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <span class="section-title">Achievements</span>
    <div class="section-line"></div>
</div>
<div class="ach-list">
    <div class="ach-item">
        <span class="ach-icon">🥉</span>
        <span class="ach-text"><strong style="color:#e8e8f0;">3rd Place — ASSET Skills Competition 2023</strong> (District Level) · Python for Robotics</span>
    </div>
    <div class="ach-item">
        <span class="ach-icon">🎓</span>
        <span class="ach-text"><strong style="color:#e8e8f0;">Next Level Web Development Course</strong> — Programming Hero (Batch 4, Level 2)</span>
    </div>
    <div class="ach-item">
        <span class="ach-icon">⚡</span>
        <span class="ach-text"><strong style="color:#e8e8f0;">Active Competitive Programmer</strong> — Codeforces · HackerRank · LeetCode</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── CONTACT ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="contact-bar">
    <div class="contact-left">
        <h3>Let's build something great.</h3>
        <p>Open to full-time roles, freelance projects, and AI/ML collaborations.</p>
    </div>
    <div class="contact-links">
        <a class="contact-link" href="mailto:jakuanultimate777@gmail.com">✉ Email</a>
        <a class="contact-link" href="https://github.com/JAKUAN-AHMED" target="_blank">GitHub</a>
        <a class="contact-link" href="https://linkedin.com/in/jakuan-ahmed-0514932a3" target="_blank">LinkedIn</a>
        <a class="contact-link" href="http://jakuan-ahmed.vercel.app" target="_blank">Portfolio</a>
        <a class="contact-link" href="tel:+8801870540683">📞 Call</a>
    </div>
</div>
<div class="footer">
    Crafted with Python &amp; Streamlit &nbsp;·&nbsp; Jakuan Ahmed © 2025
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
