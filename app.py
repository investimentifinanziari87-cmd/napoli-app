# app.py
"""
PUNTO DI INGRESSO WEB (Streamlit): La cabina di regia per tuo padre.
Versione: 1.4 (Killer del Bollino e Pulizia Totale)
"""
import streamlit as st
from data_provider import DataProvider
from logic_engine import AdvancedAnalysisEngine

# 1. Configurazione della Pagina Web
st.set_page_config(page_title="NapoliCalcio", page_icon="⚽", layout="wide")

# 2. INIEZIONE CSS: Ricostruiamo la veste grafica e NASCONDIAMO IL BOLLINO
st.markdown("""
    <style>
    /* ----------------------------------------- */
    /* KILLER DEI MENU E DEI BOLLINI STREAMLIT   */
    /* ----------------------------------------- */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .viewerBadge_container__1JCJq {display: none !important;}
    .viewerBadge_link__1S137 {display: none !important;}
    [data-testid="stCreatorBadge"] {display: none !important;}
    iframe[title="Streamlit Badge"] {display: none !important;}
    
    /* ----------------------------------------- */
    /* LA NOSTRA GRAFICA AZZURRA                 */
    /* ----------------------------------------- */
    /* Sfondo Principale Azzurro Napoli */
    .stApp {
        background-color: #0087D1 !important;
    }
    
    /* Sfondo Sidebar più scuro per contrasto */
    [data-testid="stSidebar"] {
        background-color: #003c82 !important;
    }
    
    /* Colore dei testi principali: Bianco */
    h1, h2, h3, h4, h5, h6, .stMarkdown p, [data-testid="stSidebar"] p, label {
        color: #FFFFFF !important;
    }

    /* Colore delle Metriche Numeriche */
    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
    }
    [data-testid="stMetricLabel"] p {
        color: #E0E0E0 !important;
        font-weight: bold;
    }

    /* Personalizzazione Pagelle (Le tendine bianche) */
    [data-testid="stExpander"] {
        background-color: #FFFFFF !important;
        border-radius: 10px !important;
        border: none !important;
    }
    /* Titolo del giocatore nella tendina (Azzurro) */
    [data-testid="stExpander"] summary p {
        color: #0087D1 !important; 
        font-weight: bold !important;
        font-size: 1.1rem !important;
    }

    /* Adattamento dei riquadri Info (Super Report) */
    .stAlert {
        background-color: rgba(255, 255, 255, 0.95) !important;
        border-radius: 10px !important;
        border: none !important;
    }
    .stAlert p {
        color: #003c82 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. IL LOGO VETTORIALE
logo_svg = """
<div style="display: flex; justify-content: center; margin-bottom: 10px; margin-top: 20px;">
    <svg width="160" height="160" viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">
        <circle cx="80" cy="80" r="75" fill="#0087D1" />
        <circle cx="80" cy="80" r="72" fill="none" stroke="white" stroke-width="2.5" />
        <circle cx="80" cy="80" r="62" fill="none" stroke="white" stroke-width="2.5" />
        <path d="M 50 110 L 50 50 L 110 110 L 110 50" fill="none" stroke="white" stroke-width="14" stroke-linecap="square" stroke-linejoin="miter" />
    </svg>
</div>
"""
st.markdown(logo_svg, unsafe_allow_html=True)


# --- INIZIO LOGICA DELL'APP ---

@st.cache_data
def load_matches():
    return DataProvider.get_last_matches()

matches = load_matches()

# --- MENU LATERALE (Sidebar) ---
st.sidebar.title("NapoliCalcio")

if not matches:
    st.sidebar.error("Nessuna partita trovata.")
else:
    match_dict = {f"{m['comp']} | {m['opponent']} ({m['score']})": m for m in matches}
    
    st.sidebar.markdown("### ⚽ Seleziona Partita")
    selected_match_label = st.sidebar.radio("", list(match_dict.keys()))
    selected_match = match_dict[selected_match_label]

    # --- SIMULAZIONE LOGICA DATI ---
    win = "-" in selected_match['score'] and int(selected_match['score'].split("-")[0]) > int(selected_match['score'].split("-")[1])
    
    team_stats = {
        'opp_passes': 300 if win else 450, 
        'def_actions': 55 if win else 30, 
        'att_left': 45 if win else 30, 
        'att_center': 25 if win else 40, 
        'att_right': 30 if win else 30,
        'passes_final_third': 220 if win else 110, 
        'total_passes': 550
    }
    coach_data = AdvancedAnalysisEngine.analyze_coach_strategy(team_stats)
    
    players_mock_stats = [
        ("Meret", {'prog_passes': 1, 'passes_box': 0, 'dribbles': 0}),
        ("Di Lorenzo", {'prog_passes': 6 if win else 3, 'passes_box': 2, 'dribbles': 1}),
        ("Rrahmani", {'prog_passes': 3, 'passes_box': 0, 'dribbles': 0}),
        ("Buongiorno", {'prog_passes': 8, 'passes_box': 0, 'dribbles': 1}),
        ("Olivera", {'prog_passes': 5, 'passes_box': 1, 'dribbles': 2}),
        ("Lobotka", {'prog_passes': 15, 'passes_box': 1, 'dribbles': 2}),
        ("Anguissa", {'prog_passes': 7, 'passes_box': 2, 'dribbles': 3}),
        ("McTominay", {'prog_passes': 5, 'passes_box': 4, 'dribbles': 3 if win else 1}),
        ("Politano", {'prog_passes': 4, 'passes_box': 5, 'dribbles': 4}),
        ("Kvaratskhelia", {'prog_passes': 9 if win else 3, 'passes_box': 7, 'dribbles': 8}),
        ("Lukaku", {'prog_passes': 2, 'passes_box': 8, 'dribbles': 1}),
    ]
    players_data = [
        AdvancedAnalysisEngine.analyze_player_advanced(name, stats) 
        for name, stats in players_mock_stats
    ]

    # --- DASHBOARD CENTRALE WEB ---
    st.markdown(f"<h2 style='text-align: center;'>{selected_match['comp']}: Napoli vs {selected_match['opponent']}</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.header("TACTICAL BOARD: STRATEGIA MISTER")
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="PPDA (Pressing)", value=coach_data['ppda'])
    col2.metric(label="Asimmetria (Manovra)", value="Vedi Info Sotto") 
    col3.metric(label="Dominio (IDT)", value=f"{coach_data['idt']}%")
    
    st.caption(f"**Asimmetria:** {coach_data['asymmetry']}")

    st.info(coach_data['report_possesso'])
    st.warning(coach_data['report_non_possesso'])
    st.success(coach_data['chiave_tattica'])

    st.markdown("---")

    st.header("👕 LE PAGELLE TATTICHE")
    
    for player in players_data:
        with st.expander(f"{player['name']} | xT: {player['xt']} | LBA: {player['lba']}"):
            st.markdown(f"<div style='color: #222222 !important; font-size: 1rem; line-height: 1.5;'>{player['profile']}</div>", unsafe_allow_html=True)
