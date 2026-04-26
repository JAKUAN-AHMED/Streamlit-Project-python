import streamlit as st
import html

st.set_page_config(
    page_title="Jakuan Ahmed · Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Syne:wght@400;600;700;800&display=swap');

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
    min-height: 100vh;
}

[data-testid="stHeader"] { background: transparent !important; display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
[data-testid="stMainBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
[data-testid="stMain"] { padding: 0 !important; }
section[data-testid="stSidebar"] { display: none !important; }
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }
[data-testid="stDecoration"] { display: none; }

::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #0a0a0f; }
::-webkit-scrollbar-thumb { background: #00ff88; border-radius: 2px; }

/* ── Wrapper with responsive padding ── */
.port-wrap {
    max-width: 960px;
    margin: 0 auto;
    padding: 0 clamp(20px, 5vw, 64px) 80px;
    width: 100%;
}

/* ══════════════════════════════
   HERO
══════════════════════════════ */
.hero {
    #  padding-top: 100px !important;
    padding-top:0px;
    position: relative;
    overflow: hidden;
}

.hero::after {
    content: '';
    position: absolute;
    top: -80px; right: -80px;
    width: clamp(200px, 40vw, 500px);
    height: clamp(200px, 40vw, 500px);
    border-radius: 50%;
    background: radial-gradient(circle, rgba(0,255,136,0.10) 0%, transparent 70%);
    pointer-events: none;
}

.hero-tag {
    font-family: 'Space Mono', monospace;
    font-size: clamp(9px, 1.5vw, 11px);
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #00ff88;
    background: rgba(0,255,136,0.08);
    border: 1px solid rgba(0,255,136,0.25);
    padding: 6px 14px;
    border-radius: 2px;
    margin-bottom: clamp(20px, 4vw, 28px);
    display: inline-block;
}

.hero-name {
    font-family: 'Syne', sans-serif;
    font-size: clamp(36px, 6vw, 80px);
    font-weight: 800;
    line-height: 1;
    letter-spacing: -2px;
    color: #e8e8f0;
    margin-bottom: clamp(14px, 3vw, 20px);
    white-space: nowrap;
}

.hero-name span {
    color: transparent;
    -webkit-text-stroke: 1.5px rgba(232,232,240,0.35);
}

.hero-role {
    font-family: 'Space Mono', monospace;
    font-size: clamp(11px, 2vw, 14px);
    color: #7878a0;
    margin-bottom: clamp(18px, 3vw, 28px);
    letter-spacing: 0.5px;
    line-height: 1.7;
}

.hero-role b { color: #00ff88; }

.hero-summary {
    font-size: clamp(14px, 2.2vw, 17px);
    line-height: 1.75;
    color: #a0a0c0;
    max-width: 580px;
    margin-bottom: clamp(28px, 5vw, 40px);
}

.hero-links {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: clamp(32px, 5vw, 48px);
}

.hero-link {
    font-family: 'Space Mono', monospace;
    font-size: clamp(9px, 1.4vw, 11px);
    letter-spacing: 1px;
    text-transform: uppercase;
    color: #e8e8f0;
    text-decoration: none;
    border: 1px solid rgba(232,232,240,0.18);
    padding: clamp(7px, 1.4vw, 10px) clamp(12px, 2.2vw, 18px);
    border-radius: 3px;
    transition: all 0.2s;
    background: rgba(255,255,255,0.03);
    display: inline-block;
}

.hero-link:hover { background: rgba(255,255,255,0.08); }
.hero-link.primary { background: #00ff88; color: #0a0a0f; border-color: #00ff88; }
.hero-link.primary:hover { background: #00e87a; }

.hero-stats {
    display: flex;
    gap: clamp(24px, 5vw, 52px);
    flex-wrap: wrap;
    padding-top: clamp(24px, 4vw, 36px);
    border-top: 1px solid rgba(255,255,255,0.06);
}

.hero-stat-num {
    font-family: 'Syne', sans-serif;
    font-size: clamp(28px, 5vw, 40px);
    font-weight: 800;
    color: #00ff88;
    line-height: 1;
    display: block;
}

.hero-stat-label {
    font-family: 'Space Mono', monospace;
    font-size: clamp(8px, 1.1vw, 10px);
    color: #505070;
    letter-spacing: 2px;
    text-transform: uppercase;
    display: block;
    margin-top: 5px;
}

/* ══════════════════════════════
   SECTION HEADER
══════════════════════════════ */
.section-header {
    display: flex;
    align-items: center;
    gap: 16px;
    margin: clamp(44px, 8vw, 68px) 0 clamp(20px, 3.5vw, 32px);
}

.section-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(to right, rgba(0,255,136,0.35), transparent);
}

.section-title {
    font-family: 'Space Mono', monospace;
    font-size: clamp(9px, 1.4vw, 11px);
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #00ff88;
    white-space: nowrap;
}

/* ══════════════════════════════
   SKILLS
══════════════════════════════ */

.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(min(100%, 185px), 1fr));
    gap: clamp(10px, 1.8vw, 16px);
}

.skill-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 8px;
    padding: clamp(14px, 2.2vw, 20px);
    transition: all 0.25s;
}

.skill-card:hover {
    border-color: rgba(0,255,136,0.3);
    background: rgba(0,255,136,0.04);
    transform: translateY(-2px);
}

.skill-card-label {
    font-family: 'Space Mono', monospace;
    font-size: clamp(8px, 1.1vw, 10px);
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #00ff88;
    margin-bottom: 10px;
    display: block;
}

.skill-tags { display: flex; flex-wrap: wrap; gap: 5px; }

.skill-tag {
    font-family: 'Space Mono', monospace;
    font-size: clamp(9px, 1.2vw, 11px);
    color: #a0a0c0;
    background: rgba(255,255,255,0.05);
    padding: 3px 7px;
    border-radius: 2px;
    border: 1px solid rgba(255,255,255,0.07);
}

/* ══════════════════════════════
   EXPERIENCE
══════════════════════════════ */
.exp-card {
    border-left: 2px solid #00ff88;
    padding: clamp(18px, 3vw, 26px) clamp(18px, 3vw, 28px);
    background: rgba(0,255,136,0.03);
    border-radius: 0 8px 8px 0;
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
    gap: 6px;
    margin-bottom: 4px;
}

.exp-role {
    font-family: 'Syne', sans-serif;
    font-size: clamp(16px, 3vw, 20px);
    font-weight: 700;
    color: #e8e8f0;
}

.exp-company {
    font-family: 'Space Mono', monospace;
    font-size: clamp(10px, 1.6vw, 12px);
    color: #00ff88;
    margin-top: 3px;
}

.exp-period {
    font-family: 'Space Mono', monospace;
    font-size: clamp(9px, 1.3vw, 11px);
    color: #505070;
    letter-spacing: 0.5px;
    text-align: right;
    flex-shrink: 0;
}

.exp-bullets {
    list-style: none;
    margin-top: 14px;
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.exp-bullets li {
    font-size: clamp(12px, 1.8vw, 14px);
    color: #8888a8;
    line-height: 1.65;
    padding-left: 18px;
    position: relative;
}

.exp-bullets li::before {
    content: '▸';
    position: absolute;
    left: 0;
    color: #00ff88;
    font-size: 11px;
    top: 2px;
}

/* ══════════════════════════════
   PROJECTS
══════════════════════════════ */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(min(100%, 280px), 1fr));
    gap: clamp(12px, 2.2vw, 20px);
}

.project-card {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    padding: clamp(20px, 3vw, 28px);
    transition: all 0.25s;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    gap: 14px;
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
    border-color: rgba(0,255,136,0.22);
    background: rgba(0,255,136,0.03);
    transform: translateY(-4px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.3);
}

.project-card:hover::before { opacity: 1; }

.project-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 10px;
}

.project-name {
    font-family: 'Syne', sans-serif;
    font-size: clamp(15px, 2.6vw, 19px);
    font-weight: 700;
    color: #e8e8f0;
    line-height: 1.2;
}

.project-subtitle {
    font-family: 'Space Mono', monospace;
    font-size: clamp(8px, 1.1vw, 10px);
    color: #505070;
    letter-spacing: 1px;
    margin-top: 2px;
}

.project-badge {
    font-family: 'Space Mono', monospace;
    font-size: 8px;
    color: #ffd700;
    background: rgba(255,215,0,0.08);
    border: 1px solid rgba(255,215,0,0.2);
    padding: 2px 7px;
    border-radius: 2px;
    display: inline-block;
    margin-top: 5px;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.project-links { display: flex; gap: 5px; flex-shrink: 0; flex-wrap: wrap; }

.project-link-btn {
    font-family: 'Space Mono', monospace;
    font-size: clamp(8px, 1.1vw, 9px);
    letter-spacing: 0.5px;
    text-transform: uppercase;
    color: #00ff88;
    text-decoration: none;
    border: 1px solid rgba(0,255,136,0.3);
    padding: 5px 10px;
    border-radius: 2px;
    transition: all 0.2s;
    white-space: nowrap;
}

.project-link-btn:hover { background: #00ff88; color: #0a0a0f; }
.project-link-btn.gh { color: #a0a0c0; border-color: rgba(160,160,192,0.25); }
.project-link-btn.gh:hover { background: #a0a0c0; color: #0a0a0f; }

.project-bullets {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 6px;
    flex: 1;
}

.project-bullets li {
    font-size: clamp(12px, 1.6vw, 13px);
    color: #686888;
    line-height: 1.65;
    padding-left: 16px;
    position: relative;
}

.project-bullets li::before {
    content: '▸';
    position: absolute;
    left: 0;
    color: #00b4ff;
    font-size: 10px;
    top: 2px;
}

.project-stack { display: flex; flex-wrap: wrap; gap: 5px; }

.stack-tag {
    font-family: 'Space Mono', monospace;
    font-size: clamp(8px, 1.1vw, 10px);
    color: #00b4ff;
    background: rgba(0,180,255,0.07);
    border: 1px solid rgba(0,180,255,0.18);
    padding: 3px 7px;
    border-radius: 2px;
}

/* ══════════════════════════════
   EDUCATION
══════════════════════════════ */
.edu-card {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    padding: clamp(20px, 3vw, 26px);
    transition: all 0.25s;
}

.edu-card:hover {
    border-color: rgba(0,180,255,0.28);
    background: rgba(0,180,255,0.04);
    transform: translateY(-2px);
}

.edu-degree {
    font-family: 'Syne', sans-serif;
    font-size: clamp(15px, 2.5vw, 18px);
    font-weight: 700;
    color: #e8e8f0;
    margin-bottom: 8px;
    line-height: 1.3;
}

.edu-school {
    font-family: 'Space Mono', monospace;
    font-size: clamp(10px, 1.4vw, 12px);
    color: #00b4ff;
    margin-bottom: 5px;
}

.edu-period {
    font-family: 'Space Mono', monospace;
    font-size: clamp(9px, 1.2vw, 11px);
    color: #404060;
    letter-spacing: 1px;
    margin-bottom: 10px;
}

.edu-note {
    font-size: clamp(11px, 1.5vw, 13px);
    color: #7878a0;
    line-height: 1.6;
}

.edu-gpa {
    display: inline-block;
    font-family: 'Space Mono', monospace;
    font-size: clamp(10px, 1.3vw, 11px);
    color: #00ff88;
    background: rgba(0,255,136,0.08);
    border: 1px solid rgba(0,255,136,0.2);
    padding: 2px 10px;
    border-radius: 2px;
    margin-top: 10px;
}

/* ══════════════════════════════
   ACHIEVEMENTS
══════════════════════════════ */
.ach-list { display: flex; flex-direction: column; gap: 10px; }

.ach-item {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    padding: clamp(14px, 2.2vw, 18px) clamp(14px, 2.2vw, 22px);
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 8px;
    transition: all 0.2s;
}

.ach-item:hover {
    border-color: rgba(0,255,136,0.2);
    background: rgba(0,255,136,0.03);
    transform: translateX(4px);
}

.ach-icon { font-size: clamp(18px, 2.8vw, 22px); flex-shrink: 0; line-height: 1.4; }

.ach-text {
    font-size: clamp(12px, 1.7vw, 14px);
    color: #a0a0c0;
    line-height: 1.6;
}

/* ══════════════════════════════
   CONTACT
══════════════════════════════ */
.contact-bar {
    margin-top: clamp(44px, 7vw, 64px);
    padding: clamp(24px, 4vw, 36px);
    border: 1px solid rgba(0,255,136,0.13);
    border-radius: 12px;
    background: rgba(0,255,136,0.025);
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
}

.contact-left h3 {
    font-family: 'Syne', sans-serif;
    font-size: clamp(18px, 3.5vw, 24px);
    font-weight: 800;
    color: #e8e8f0;
    margin-bottom: 5px;
}

.contact-left p {
    font-size: clamp(12px, 1.6vw, 14px);
    color: #606080;
}

.contact-links { display: flex; flex-wrap: wrap; gap: 8px; }

.contact-link {
    font-family: 'Space Mono', monospace;
    font-size: clamp(9px, 1.2vw, 11px);
    letter-spacing: 0.5px;
    text-transform: uppercase;
    color: #e8e8f0;
    text-decoration: none;
    border: 1px solid rgba(232,232,240,0.13);
    padding: clamp(8px, 1.4vw, 10px) clamp(12px, 1.8vw, 16px);
    border-radius: 4px;
    transition: all 0.2s;
    background: rgba(255,255,255,0.03);
}

.contact-link:hover { background: #00ff88; color: #0a0a0f; border-color: #00ff88; }

.footer {
    text-align: center;
    margin-top: clamp(40px, 6vw, 60px);
    padding: 20px 0;
    border-top: 1px solid rgba(255,255,255,0.05);
    font-family: 'Space Mono', monospace;
    font-size: clamp(9px, 1.1vw, 11px);
    color: #303050;
    letter-spacing: 1px;
}
</style>
""", unsafe_allow_html=True)

# ── DATA ──────────────────────────────────────────────────────────────────────
SKILLS = {
    "Languages":      ["TypeScript", "JavaScript", "Python", "C", "C++"],
    "Frontend":       ["React.js", "Next.js", "Tailwind CSS", "Shadcn/UI", "Zustand"],
    "Backend":        ["Node.js", "Express.js", "REST API", "JWT", "Prisma"],
    "Databases":      ["MongoDB", "Mongoose", "MySQL"],
    "Cloud & DevOps": ["AWS EC2", "AWS S3", "CDN", "Nginx", "VPS", "SSH", "Git", "Vercel"],
}

PROJECTS = [
    {
        "name": "Admission Mirror",
        "subtitle": None,
        "featured": True,
        "live_url": "https://admission-mirror.vercel.app",
        "github_url": None,
        "bullets": [
            "Full-featured university admission prep platform covering 11+ universities — exam simulation engine with timer, review & analytics, 8-week study plans, and practice games (flashcards, quiz, formula sprint).",
            "Built Python scraper to automate MongoDB seeding (~90% less manual work); modular Next.js architecture with JWT auth and Zustand for seamless sessions.",
        ],
        "stack": ["Next.js", "TypeScript", "MongoDB", "Tailwind", "Zustand", "JWT", "Python (Scraper)"],
    },
    {
        "name": "Motivate App",
        "subtitle": "Fitness & Wellness Platform",
        "featured": False,
        "live_url": "https://play.google.com",
        "github_url": "https://github.com/JAKUAN-AHMED",
        "bullets": [
            "Full-featured fitness platform for home or gym training — users track progress, connect with personal trainers, access a TDEE calculator and healthy recipes section.",
            "Community features: post sharing, trainer-to-user chat, and before/after transformation image uploads.",
            "Secure auth + AWS EC2, S3, and CDN for media delivery; React-based admin dashboard for complete app management.",
        ],
        "stack": ["Node.js", "Express.js", "MongoDB", "AWS EC2", "S3", "CDN", "React (Dashboard)"],
    },
    {
        "name": "Jordan",
        "subtitle": "Gaming Platform Backend",
        "featured": False,
        "live_url": None,
        "github_url": "https://github.com/JAKUAN-AHMED",
        "bullets": [
            "Backend for a rabbit-eats-carrots game featuring a complete coin economy and in-game purchase system.",
            "Stripe payment integration for coin purchases; secure JWT auth with role-based access control.",
            "Deployed on AWS EC2 with Nginx reverse proxy; S3 for asset storage.",
        ],
        "stack": ["Node.js", "Express.js", "MongoDB", "AWS EC2", "S3", "Stripe"],
    },
]

# ── RENDER ────────────────────────────────────────────────────────────────────
st.markdown('<div class="port-wrap">', unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="hero">
    <span class="hero-tag">⚡ Open to opportunities</span>
    <h1 class="hero-name">JAKUAN <span>AHMED</span></h1>
    <p class="hero-role">
        <b>Software Engineer</b> &nbsp;·&nbsp; Currently Learning AI/ML
        &nbsp;·&nbsp; Sylhet, Bangladesh
    </p>
    <p class="hero-summary">
        Full-stack engineer delivering production-grade systems using TypeScript, React,
        Next.js, and Node.js. Skilled in scalable REST APIs, cloud deployment on AWS,
        and modular architecture. Currently expanding into AI/ML to build intelligent,
        data-driven products.
    </p>
    <div class="hero-links">
        <a class="hero-link primary" href="mailto:jakuanultimate777@gmail.com">✉ Email Me</a>
        <a class="hero-link" href="https://github.com/JAKUAN-AHMED" target="_blank">GitHub</a>
        <a class="hero-link" href="https://linkedin.com/in/jakuan-ahmed-0514932a3" target="_blank">LinkedIn</a>
        <a class="hero-link" href="http://jakuan-ahmed.vercel.app" target="_blank">Portfolio</a>
        <a class="hero-link" href="tel:+8801870540683">📞 Call</a>
    </div>
</div>
""", unsafe_allow_html=True)

# SKILLS - build entire block in one string, single render call
# NO INDENTATION inside HTML strings to prevent Streamlit markdown code-block rendering
skills_cards_html = ""
for cat, tags in SKILLS.items():
    tags_html = "".join(f'<span class="skill-tag">{html.escape(t)}</span>' for t in tags)
    skills_cards_html += (
        '<div class="skill-card">'
        f'<span class="skill-card-label">{html.escape(cat)}</span>'
        f'<div class="skill-tags">{tags_html}</div>'
        '</div>'
    )

st.markdown(
    '<div class="section-header">'
    '<span class="section-title">Technical Skills</span>'
    '<div class="section-line"></div>'
    '</div>'
    f'<div class="skills-grid">{skills_cards_html}</div>',
    unsafe_allow_html=True,
)

# EXPERIENCE
st.markdown("""
<div class="section-header">
    <span class="section-title">Work Experience</span>
    <div class="section-line"></div>
</div>
<div class="exp-card">
    <div class="exp-top">
        <div>
            <div class="exp-role">Software Developer</div>
            <div class="exp-company">SparkTech &nbsp;·&nbsp; On-Site, Bangladesh</div>
        </div>
        <div class="exp-period">APR 2025 – PRESENT</div>
    </div>
    <ul class="exp-bullets">
        <li>Built optimized RESTful APIs with modular architecture using Node.js, Express.js, and MongoDB; deployed on VPS via SSH with Nginx as reverse proxy.</li>
        <li>Delivered 12+ full-stack client projects on schedule; implemented JWT authentication, role-based access control, and AWS S3 for file/media storage.</li>
        <li>Collaborated with design and product teams using agile workflows to ship features with high client satisfaction.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

project_cards_html = ""

for p in PROJECTS:
    name = html.escape(p.get("name", ""))
    subtitle = html.escape(p.get("subtitle", "")) if p.get("subtitle") else ""

    badge = '<span class="project-badge">★ Featured</span>' if p.get("featured") else ""
    subtitle_html = f'<div class="project-subtitle">{subtitle}</div>' if subtitle else ""

    links_html = ""
    if p.get("live_url"):
        links_html += f'<a class="project-link-btn" href="{p["live_url"]}" target="_blank">↗ Live</a>'
    if p.get("github_url"):
        links_html += f'<a class="project-link-btn gh" href="{p["github_url"]}" target="_blank">GitHub</a>'

    bullets_html = "".join(f"<li>{html.escape(b)}</li>" for b in p["bullets"])
    stack_html = "".join(f'<span class="stack-tag">{html.escape(t)}</span>' for t in p["stack"])

    project_cards_html += (
        '<div class="project-card">'
        '<div class="project-header">'
        '<div>'
        f'<div class="project-name">{name}</div>'
        f'{subtitle_html}'
        f'{badge}'
        '</div>'
        f'<div class="project-links">{links_html}</div>'
        '</div>'
        f'<ul class="project-bullets">{bullets_html}</ul>'
        f'<div class="project-stack">{stack_html}</div>'
        '</div>'
    )

st.markdown(
    '<div class="section-header">'
    '<span class="section-title">Projects</span>'
    '<div class="section-line"></div>'
    '</div>'
    f'<div class="projects-grid">{project_cards_html}</div>',
    unsafe_allow_html=True,
)


# EDUCATION
st.markdown("""
<div class="section-header">
    <span class="section-title">Education</span>
    <div class="section-line"></div>
</div>
<div class="edu-card">
    <div class="edu-degree">Diploma, Computer Science &amp; Technology</div>
    <div class="edu-school">Moulvibazar Polytechnic Institute — Sylhet, Bangladesh</div>
    <div class="edu-period">2022 – 2026 (Expected)</div>
    <div class="edu-note">Class Representative (7×) &nbsp;·&nbsp; Programming Mentor</div>
    <span class="edu-gpa">GPA 3.60 / 4.00</span>
</div>
""", unsafe_allow_html=True)

# ACHIEVEMENTS
st.markdown("""
<div class="section-header">
    <span class="section-title">Achievements</span>
    <div class="section-line"></div>
</div>
<div class="ach-list">
    <div class="ach-item">
        <span class="ach-icon">🥉</span>
        <span class="ach-text">
            <strong style="color:#e8e8f0;">3rd Place — ASSET Skills Competition 2023</strong>
            &nbsp;(District Level) &nbsp;·&nbsp; Python for Robotics
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

# CONTACT
st.markdown("""
<div class="contact-bar">
    <div class="contact-left">
        <h3>Let's build something great.</h3>
        <p>Open to full-time roles, freelance projects &amp; AI/ML collaborations.</p>
    </div>
    <div class="contact-links">
        <a class="contact-link" href="mailto:jakuanultimate777@gmail.com">✉ Email</a>
        <a class="contact-link" href="https://github.com/JAKUAN-AHMED" target="_blank">GitHub</a>
        <a class="contact-link" href="https://linkedin.com/in/jakuan-ahmed-0514932a3" target="_blank">LinkedIn</a>
        <a class="contact-link" href="http://jakuan-ahmed.vercel.app" target="_blank">Portfolio</a>
        <a class="contact-link" href="https://admission-mirror.vercel.app" target="_blank">Admission Mirror</a>
    </div>
</div>
<div class="footer">
    Crafted with Python &amp; Streamlit &nbsp;·&nbsp; Jakuan Ahmed © 2025
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
