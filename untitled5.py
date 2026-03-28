import streamlit as st
from PIL import Image
import os

# Configuration de la page
st.set_page_config(
    page_title="Malak Benfarhour - Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialiser l'état de session
if 'show_certification' not in st.session_state:
    st.session_state.show_certification = False

# Fonction pour trouver les images
def find_certification_image():
    possible_names = ["image.png", "image.PNG", "certification.png", "certificat.png", "certif.png"]
    all_files = os.listdir('.')
    for name in possible_names:
        if name in all_files:
            return name
    for file in all_files:
        if file.lower().endswith(('.png', '.jpg')):
            return file
    return None

certif_image_path = find_certification_image()

# CSS Ultra Premium
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Background Gradient avec effet glassmorphism */
    .stApp {
        background: radial-gradient(circle at 10% 20%, rgba(99,102,241,0.05) 0%, rgba(139,92,246,0.03) 100%);
    }
    
    /* Main Container */
    .main-container {
        max-width: 1400px;
        margin: 0 auto;
        padding: 0 1rem;
    }
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Navigation Bar - Glassmorphism */
    .nav-bar {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(20px);
        border-radius: 80px;
        padding: 0.8rem 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.02), 0 1px 0 rgba(255,255,255,0.8);
        border: 1px solid rgba(255,255,255,0.5);
        position: sticky;
        top: 20px;
        z-index: 1000;
    }
    
    .nav-links {
        display: flex;
        justify-content: center;
        gap: 3rem;
        flex-wrap: wrap;
    }
    
    .nav-link {
        color: #4b5563;
        text-decoration: none;
        font-weight: 500;
        padding: 0.5rem 0;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
        font-size: 1rem;
        position: relative;
        letter-spacing: -0.2px;
    }
    
    .nav-link:hover {
        color: #6366f1;
        transform: translateY(-2px);
    }
    
    .nav-link.active {
        color: #6366f1;
    }
    
    .nav-link.active::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        border-radius: 2px;
        transform: scaleX(1);
    }
    
    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(40px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-12px); }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 20px rgba(99,102,241,0.1); }
        50% { box-shadow: 0 0 30px rgba(99,102,241,0.2); }
    }
    
    /* Hero Section - Premium */
    .hero-premium {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #2e1065 100%);
        border-radius: 40px;
        padding: 3rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
        animation: fadeInUp 0.7s ease-out;
        box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25);
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .hero-premium::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%);
        animation: float 20s ease-in-out infinite;
    }
    
    .hero-premium::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="20" cy="20" r="2" fill="rgba(255,255,255,0.1)"/><circle cx="80" cy="40" r="1.5" fill="rgba(255,255,255,0.1)"/><circle cx="50" cy="85" r="2" fill="rgba(255,255,255,0.1)"/></svg>') repeat;
        opacity: 0.3;
        pointer-events: none;
    }
    
    .hero-premium h1 {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #fff 0%, #c4b5fd 50%, #a78bfa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.75rem;
        letter-spacing: -1px;
    }
    
    /* Cards Premium */
    .card-premium {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(12px);
        border-radius: 28px;
        padding: 2rem;
        box-shadow: 0 20px 35px -12px rgba(0,0,0,0.08);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        border: 1px solid rgba(255,255,255,0.6);
        height: 100%;
        animation: fadeInUp 0.7s ease-out;
    }
    
    .card-premium:hover {
        transform: translateY(-8px);
        box-shadow: 0 30px 50px -12px rgba(0,0,0,0.2);
        border-color: rgba(99,102,241,0.3);
        background: rgba(255, 255, 255, 1);
    }
    
    /* Stats Cards */
    .stat-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.98) 0%, rgba(255,255,255,0.95) 100%);
        backdrop-filter: blur(12px);
        border-radius: 24px;
        padding: 1.6rem;
        text-align: center;
        transition: all 0.4s ease;
        border: 1px solid rgba(255,255,255,0.5);
        position: relative;
        overflow: hidden;
    }
    
    .stat-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(99,102,241,0.1), transparent);
        transition: left 0.6s ease;
    }
    
    .stat-card:hover::before {
        left: 100%;
    }
    
    .stat-card:hover {
        transform: translateY(-6px);
        border-color: #6366f1;
        box-shadow: 0 20px 35px -10px rgba(99,102,241,0.2);
    }
    
    .stat-number {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    /* Skill Tags */
    .skill-tag-premium {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        color: #4f46e5;
        padding: 0.6rem 1.3rem;
        border-radius: 50px;
        display: inline-block;
        margin: 0.4rem;
        font-size: 0.85rem;
        font-weight: 600;
        transition: all 0.3s ease;
        border: 1px solid rgba(79,70,229,0.15);
        cursor: default;
        backdrop-filter: blur(4px);
    }
    
    .skill-tag-premium:hover {
        transform: translateY(-3px) scale(1.02);
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        border-color: transparent;
        box-shadow: 0 8px 20px rgba(99,102,241,0.3);
    }
    
    /* Section Title */
    .section-title-premium {
        font-size: 2.2rem;
        font-weight: 700;
        margin: 2.5rem 0 1.8rem 0;
        padding-left: 1.2rem;
        border-left: 5px solid #6366f1;
        display: inline-block;
        background: linear-gradient(135deg, #1e293b 0%, #475569 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.5px;
    }
    
    /* Badge */
    .badge-premium {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        padding: 0.3rem 1rem;
        border-radius: 40px;
        font-size: 0.7rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 1rem;
        letter-spacing: 0.3px;
    }
    
    /* Certification Card */
    .certif-card {
        background: linear-gradient(135deg, #fffbeb 0%, #fef7e0 100%);
        border-left: 5px solid #f59e0b;
        padding: 2rem;
        border-radius: 24px;
        box-shadow: 0 15px 30px -10px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    
    .certif-card:hover {
        transform: translateX(5px);
        box-shadow: 0 20px 35px -10px rgba(245,158,11,0.15);
    }
    
    /* Button Premium */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.8rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
        font-size: 1rem;
        letter-spacing: 0.3px;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 30px -8px rgba(99,102,241,0.5);
    }
    
    /* Modal */
    .modal-premium {
        background: white;
        border-radius: 32px;
        padding: 2rem;
        margin-top: 1.5rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 30px 60px -15px rgba(0,0,0,0.25);
        animation: fadeInUp 0.5s ease-out;
    }
    
    /* Divider */
    .divider-premium {
        height: 2px;
        background: linear-gradient(90deg, #6366f1 0%, #8b5cf6 50%, transparent 100%);
        margin: 1.2rem 0;
    }
    
    /* Footer */
    .footer-premium {
        text-align: center;
        padding: 2rem;
        background: rgba(255,255,255,0.9);
        backdrop-filter: blur(12px);
        border-radius: 28px;
        margin-top: 2rem;
        color: #64748b;
        font-size: 0.85rem;
        border: 1px solid rgba(255,255,255,0.6);
    }
    
    /* Profile Image */
    .profile-img-wrapper {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        border-radius: 50%;
        padding: 5px;
        display: inline-block;
        transition: all 0.4s ease;
    }
    
    .profile-img-wrapper:hover {
        transform: scale(1.02);
        box-shadow: 0 20px 35px -10px rgba(99,102,241,0.4);
    }
    
    /* Scroll behavior */
    html {
        scroll-behavior: smooth;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .hero-premium h1 { font-size: 2.2rem; }
        .section-title-premium { font-size: 1.6rem; }
        .card-premium { padding: 1.4rem; }
        .nav-links { gap: 1.2rem; }
        .nav-link { font-size: 0.85rem; }
        .hero-premium { padding: 2rem; }
        .stat-number { font-size: 2rem; }
    }
</style>
""", unsafe_allow_html=True)

# Main Container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Barre de navigation
st.markdown("""
<div class="nav-bar">
    <div class="nav-links">
        <a href="#home" class="nav-link">✨ Accueil</a>
        <a href="#about" class="nav-link">👤 Profil</a>
        <a href="#skills" class="nav-link">⚡ Compétences</a>
        <a href="#work" class="nav-link">🚀 Réalisations</a>
        <a href="#contact" class="nav-link">📞 Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Home Section
st.markdown('<div id="home"></div>', unsafe_allow_html=True)

# Header Premium avec photo
col1, col2 = st.columns([1, 2.2])

with col1:
    try:
        if os.path.exists("photo.png"):
            profile_image = Image.open("photo.png")
            st.markdown('<div class="profile-img-wrapper">', unsafe_allow_html=True)
            st.image(profile_image, width=280, use_container_width=False)
            st.markdown('</div>', unsafe_allow_html=True)
        elif os.path.exists("photo.jpg"):
            profile_image = Image.open("photo.jpg")
            st.markdown('<div class="profile-img-wrapper">', unsafe_allow_html=True)
            st.image(profile_image, width=280, use_container_width=False)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="profile-img-wrapper">
                <div style="width: 280px; height: 280px; background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%); 
                            border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                            border: 4px solid white; box-shadow: 0 20px 35px -10px rgba(0,0,0,0.2);">
                    <span style="font-size: 100px;">✨</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    except:
        pass

with col2:
    st.markdown("""
    <div class="hero-premium">
        <h1>Malak Benfarhour</h1>
        <p style="font-size: 1.2rem; color: #cbd5e1; margin-bottom: 1rem; letter-spacing: -0.2px;">✨ Ingénieure en Génie Industriel</p>
        <p style="font-size: 1rem; color: #a5b4fc; line-height: 1.7;">Étudiante motivée en 2ème année de génie industriel, spécialisée en optimisation des systèmes, logistique et data intelligence. Rigoureuse et passionnée par l'innovation industrielle.</p>
    </div>
    """, unsafe_allow_html=True)

# About Section
st.markdown('<div id="about"></div>', unsafe_allow_html=True)

# Contact et À propos
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card-premium">
        <h3 style="margin-bottom: 1.2rem;">Contact</h3>
        <p style="margin-bottom: 0.8rem;">📱 06 18 82 00 65</p>
        <p style="margin-bottom: 0.8rem;">✉️ malakbenfarhour@gmail.com</p>
        <p style="margin-bottom: 1rem;">📍 Safi, Maroc</p>
        <div class="divider-premium"></div>
        <h3 style="margin-top: 1rem; margin-bottom: 1rem;">🎯 Disponible</h3>
        <p>✨ Stage PFA | Alternance</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card-premium">
        <h3 style="margin-bottom: 1.2rem;">À propos de moi</h3>
        <p style="margin-bottom: 0.8rem;"><strong>🎯 Objectif :</strong> Optimisation des performances industrielles</p>
        <p style="margin-bottom: 0.8rem;"><strong>💡 Passion :</strong> Data Intelligence & Innovation</p>
        <p style="margin-bottom: 0.8rem;"><strong>⭐ Qualités :</strong> Rigueur, Travail en équipe, Adaptabilité</p>
        <p><strong>🏆 Certifiée :</strong> Data Visualization & BI</p>
    </div>
    """, unsafe_allow_html=True)

# Statistiques
st.markdown('<div class="section-title-premium">📊 En chiffres</div>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="stat-card"><p class="stat-number">48h</p><p>Formation certifiée</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="stat-card"><p class="stat-number">2+</p><p>Projets majeurs</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stat-card"><p class="stat-number">OCP</p><p>Expérience industrielle</p></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="stat-card"><p class="stat-number">3</p><p>Langues parlées</p></div>', unsafe_allow_html=True)

# Formation et Expérience
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-title-premium">🎓 Formation</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-premium">
        <div class="badge-premium">2021-2022</div>
        <h3>📚 Baccalauréat Sciences Physiques</h3>
        <p style="color: #64748b;">Lycée Ibn khaldoun, Safi</p>
        <p style="color: #6366f1; font-weight: 600;">✨ Mention Très Bien</p>
        <div class="divider-premium"></div>
        <div class="badge-premium" style="background: linear-gradient(135deg, #f59e0b 0%, #f97316 100%);">En cours</div>
        <h3>🎓 Ingénierie en Génie Industriel</h3>
        <p style="color: #64748b;">ENSA Safi - 2ème année</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section-title-premium">💼 Expérience</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-premium">
        <div class="badge-premium">Juillet 2024 | 1 mois</div>
        <h3>🏭 MAROC CHIMIE - Groupe OCP</h3>
        <p style="color: #64748b;">Stage d'observation | Site de Safi</p>
        <ul style="margin-left: 1rem; margin-top: 1rem; color: #334155;">
            <li>🔧 Étude technique du turbo-alternateur</li>
            <li>⚡ Observation des enjeux de production énergétique</li>
            <li>🛡️ Analyse des cycles de maintenance et sécurité</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Skills Section
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)

# Compétences
st.markdown('<div class="section-title-premium">⚡ Compétences Techniques</div>', unsafe_allow_html=True)
st.markdown('<div class="card-premium">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<h4 style="margin-bottom: 1rem;">📊 Data & BI</h4>', unsafe_allow_html=True)
    st.markdown('<span class="skill-tag-premium">Power BI</span>', unsafe_allow_html=True)
    st.markdown('<span class="skill-tag-premium">Python (Pandas)</span>', unsafe_allow_html=True)
    st.markdown('<span class="skill-tag-premium">Matplotlib/Seaborn</span>', unsafe_allow_html=True)
    st.markdown('<span class="skill-tag-premium">Plotly</span>', unsafe_allow_html=True)

with col2:
    st.markdown('<h4 style="margin-bottom: 1rem;">🏭 Génie Industriel</h4>', unsafe_allow_html=True)
    st.markdown('<span class="skill-tag-premium">Gestion de production</span>', unsafe_allow_html=True)
    st.markdown('<span class="skill-tag-premium">Optimisation des flux</span>', unsafe_allow_html=True)
    st.markdown('<span class="skill-tag-premium">Logistique & SCM</span>', unsafe_allow_html=True)
    st.markdown('<span class="skill-tag-premium">Contrôle qualité</span>', unsafe_allow_html=True)
    st.markdown('<span class="skill-tag-premium">Maintenance industrielle</span>', unsafe_allow_html=True)

with col3:
    st.markdown('<h4 style="margin-bottom: 1rem;">💻 Outils & Dev</h4>', unsafe_allow_html=True)
    st.markdown('<span class="skill-tag-premium">VBA Excel</span>', unsafe_allow_html=True)
    st.markdown('<span class="skill-tag-premium">Minitab</span>', unsafe_allow_html=True)
    st.markdown('<span class="skill-tag-premium">SQL</span>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Work Section
st.markdown('<div id="work"></div>', unsafe_allow_html=True)

# Projets
st.markdown('<div class="section-title-premium">🚀 Projets Académiques</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card-premium">
        <div class="badge-premium">IoT</div>
        <h3>📡 Poubelle Intelligente</h3>
        <p style="color: #475569;">Conception et programmation d'un système automatisé de gestion des déchets avec capteurs ultrasoniques et notification en temps réel.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card-premium">
        <div class="badge-premium">Algorithmique</div>
        <h3>💻 Système de Gestion (Langage C)</h3>
        <p style="color: #475569;">Développement d'une application console complète pour la gestion de stocks avec manipulation avancée de fichiers et structures de données.</p>
    </div>
    """, unsafe_allow_html=True)

# Certification
st.markdown('<div class="section-title-premium">🏆 Certification</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1.6, 1])

with col1:
    st.markdown("""
    <div class="certif-card">
        <div class="badge-premium" style="background: linear-gradient(135deg, #f97316 0%, #f59e0b 100%);">✓ Certifiée</div>
        <h2 style="color: #1e293b; margin-bottom: 0.5rem;">Data Visualization & Business Intelligence</h2>
        <p style="font-size: 1rem; font-weight: 500; color: #f97316;">YaneCode Academy</p>
        <p><strong>📅 Durée :</strong> 48 heures (2 mois)</p>
        <p><strong>👩‍🎓 Bénéficiaire :</strong> BENFARHOUR Malak</p>
        <div class="divider-premium"></div>
        <h4>📚 Compétences acquises :</h4>
        <ul style="margin-top: 0.5rem;">
            <li>✅ Principes fondamentaux de la Data Visualization</li>
            <li>✅ Analyse avec Python (Pandas, Matplotlib, Seaborn)</li>
            <li>✅ Automatisation Excel & VBA</li>
            <li>✅ Tableaux de bord Power BI</li>
            <li>✅ Analyse décisionnelle</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card-premium" style="background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%); color: white; border: none;">
        <h3 style="text-align: center;">📜 À propos</h3>
        <div class="divider-premium" style="background: rgba(255,255,255,0.3);"></div>
        <p style="text-align: center;">Formation professionnelle en Data Visualization & Business Intelligence</p>
        <p style="text-align: center; margin-top: 1rem;">✨ Certification validée par YaneCode Academy</p>
    </div>
    """, unsafe_allow_html=True)

# Bouton
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("📜 Voir la certification", use_container_width=True):
        st.session_state.show_certification = True

# Modal
if st.session_state.show_certification:
    st.markdown('<div class="modal-premium">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([5, 1, 1])
    with col3:
        if st.button("✖️ Fermer"):
            st.session_state.show_certification = False
            st.rerun()
    
    st.markdown('<h2 style="color: #6366f1; text-align: center;">📜 Certificat de Formation</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;"><strong>BENFARHOUR Malak</strong></p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;">Data Visualization & Business Intelligence - YaneCode Academy</p>', unsafe_allow_html=True)
    
    if certif_image_path:
        try:
            image = Image.open(certif_image_path)
            st.image(image, use_container_width=True)
        except:
            st.warning("⚠️ Image non trouvée")
    else:
        st.warning("⚠️ Image non trouvée")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Engagements
st.markdown('<div class="section-title-premium">🤝 Engagements</div>', unsafe_allow_html=True)
st.markdown("""
<div class="card-premium">
    <h3>🔄 Club Rotaract ENSA Safi</h3>
    <p><strong>Responsable Relations Internes</strong></p>
    <p style="color: #475569;">Organisation d'événements, coordination d'équipes, développement du réseau professionnel et animation de la vie associative.</p>
</div>
""", unsafe_allow_html=True)

# Langues
st.markdown('<div class="section-title-premium">🌍 Langues</div>', unsafe_allow_html=True)
st.markdown('<div class="card-premium">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<h4>Français</h4>', unsafe_allow_html=True)
    st.progress(0.85)
    st.markdown('<p style="text-align: right;">Avancé (B2)</p>', unsafe_allow_html=True)

with col2:
    st.markdown('<h4>Anglais</h4>', unsafe_allow_html=True)
    st.progress(0.60)
    st.markdown('<p style="text-align: right;">Intermédiaire (B1)</p>', unsafe_allow_html=True)

with col3:
    st.markdown('<h4>Arabe</h4>', unsafe_allow_html=True)
    st.progress(1.0)
    st.markdown('<p style="text-align: right;">Langue maternelle</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Objectif
st.markdown('<div class="section-title-premium">🎯 Objectif</div>', unsafe_allow_html=True)
st.markdown("""
<div class="card-premium">
    <p style="font-size: 1rem; line-height: 1.7; color: #334155;">Contribuer efficacement à l'optimisation et l'amélioration des performances industrielles en mettant en œuvre des solutions innovantes en gestion de production, logistique et qualité. Forte de mes compétences en data visualisation et analyse décisionnelle, je souhaite apporter une valeur ajoutée dans un environnement industriel exigeant.</p>
</div>
""", unsafe_allow_html=True)

# Contact Section
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer-premium">
    <p>© 2025 Malak Benfarhour - Portfolio Professionnel</p>
    <p style="font-size: 0.7rem; margin-top: 0.5rem;">✨ Disponible pour un stage PFA | Alternance</p>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)