import streamlit as st
import requests

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="🏠 Дом-О-Метр",
    page_icon="🏡",
    layout="centered",
)

# ─── Cartoon CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;800;900&family=Fredoka+One&display=swap');

/* ── Root & Background ── */
html, body, [data-testid="stAppViewContainer"] {
    background: #FFF8EC !important;
}

[data-testid="stAppViewContainer"] {
    background-image:
        radial-gradient(circle at 10% 20%, #FFE0A3 0%, transparent 40%),
        radial-gradient(circle at 90% 80%, #C8F0D8 0%, transparent 40%),
        radial-gradient(circle at 50% 50%, #FFD6E8 0%, transparent 60%);
}

/* floating clouds */
[data-testid="stAppViewContainer"]::before {
    content: "☁️  ☁️       ☁️    ☁️  ☁️";
    position: fixed;
    top: 18px;
    left: 0; right: 0;
    font-size: 2rem;
    letter-spacing: 1.4rem;
    opacity: .35;
    pointer-events: none;
    animation: drift 18s linear infinite;
    white-space: nowrap;
    overflow: hidden;
}
@keyframes drift { from{transform:translateX(-60px)} to{transform:translateX(60px)} }

/* ── Typography ── */
* { font-family: 'Nunito', sans-serif !important; }

h1, [data-testid="stMarkdownContainer"] h1 {
    font-family: 'Fredoka One', cursive !important;
}

/* ── Hide default header/footer ── */
header[data-testid="stHeader"], footer { display:none !important; }
[data-testid="stDecoration"] { display:none !important; }

/* ── Main container card ── */
[data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"]:first-child {
    background: white;
    border-radius: 28px;
    border: 3.5px solid #222;
    box-shadow: 6px 6px 0px #222;
    padding: 2rem 2.5rem !important;
    margin-top: 2rem;
}

/* ── Title ── */
.cartoon-title {
    font-family: 'Fredoka One', cursive !important;
    font-size: 3rem;
    color: #222;
    text-align: center;
    letter-spacing: 1px;
    line-height: 1.1;
    text-shadow: 3px 3px 0 #FFB347, 5px 5px 0 #FF6B6B;
    margin-bottom: 0.3rem;
}
.cartoon-subtitle {
    text-align: center;
    color: #888;
    font-size: 1rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
    letter-spacing: .5px;
}

/* ── Number inputs ── */
[data-testid="stNumberInput"] {
    background: #FFFDE7 !important;
    border-radius: 14px !important;
    border: 2.5px solid #222 !important;
    box-shadow: 3px 3px 0 #222;
    margin-bottom: 0.5rem;
    overflow: hidden;
}
[data-testid="stNumberInput"] input {
    font-size: 1.1rem !important;
    font-weight: 800 !important;
    color: #222 !important;
}
[data-testid="stNumberInput"] label {
    font-weight: 800 !important;
    color: #444 !important;
    font-size: 0.95rem !important;
}

/* ── Select box ── */
[data-testid="stSelectbox"] > div > div {
    background: #E8F5FF !important;
    border: 2.5px solid #222 !important;
    border-radius: 14px !important;
    box-shadow: 3px 3px 0 #222 !important;
    font-weight: 800 !important;
    color: #222 !important;
}
[data-testid="stSelectbox"] label {
    font-weight: 800 !important;
    color: #444 !important;
}

/* ── Button ── */
[data-testid="stButton"] button {
    width: 100% !important;
    background: #FF6B6B !important;
    color: white !important;
    font-family: 'Fredoka One', cursive !important;
    font-size: 1.4rem !important;
    border: 3px solid #222 !important;
    border-radius: 16px !important;
    box-shadow: 5px 5px 0 #222 !important;
    padding: 0.6rem 1.5rem !important;
    letter-spacing: 1px;
    transition: transform .1s, box-shadow .1s !important;
    margin-top: 0.8rem;
}
[data-testid="stButton"] button:hover {
    background: #FF4757 !important;
    transform: translate(-2px, -2px) !important;
    box-shadow: 7px 7px 0 #222 !important;
}
[data-testid="stButton"] button:active {
    transform: translate(3px, 3px) !important;
    box-shadow: 2px 2px 0 #222 !important;
}

/* ── Success alert ── */
[data-testid="stAlert"] {
    border-radius: 18px !important;
    border: 3px solid #222 !important;
    box-shadow: 4px 4px 0 #222 !important;
    font-weight: 800 !important;
    font-size: 1.05rem !important;
}

/* ── Divider ── */
.cartoon-divider {
    border: none;
    border-top: 2.5px dashed #DDD;
    margin: 1.2rem 0;
}

/* ── Section labels ── */
.section-badge {
    display: inline-block;
    background: #222;
    color: white;
    font-family: 'Fredoka One', cursive !important;
    font-size: 0.85rem;
    border-radius: 20px;
    padding: 2px 14px;
    margin-bottom: 10px;
    letter-spacing: .5px;
}

/* ── Emoji row ── */
.emoji-row {
    text-align: center;
    font-size: 2rem;
    letter-spacing: 1rem;
    margin-bottom: .5rem;
    animation: bounce 2.2s ease-in-out infinite;
}
@keyframes bounce {
    0%,100% { transform: translateY(0) }
    50%      { transform: translateY(-8px) }
}

/* ── Price tag ── */
.price-tag {
    background: #A8E6CF;
    border: 3px solid #222;
    border-radius: 20px;
    box-shadow: 5px 5px 0 #222;
    text-align: center;
    padding: 1.2rem 1rem;
    margin-top: 0.5rem;
}
.price-tag .label {
    font-size: 0.9rem;
    font-weight: 800;
    color: #555;
    margin-bottom: 4px;
}
.price-tag .amount {
    font-family: 'Fredoka One', cursive !important;
    font-size: 2.5rem;
    color: #222;
    letter-spacing: 1px;
}
.price-tag .currency {
    font-size: 1.1rem;
    font-weight: 800;
    color: #666;
}

/* ── Column gap fix ── */
[data-testid="stColumns"] { gap: 1rem; }
</style>
""", unsafe_allow_html=True)


# ─── Data ──────────────────────────────────────────────────────────────────────
nei_list = [
    '_Blueste', '_BrDale', '_BrkSide', '_ClearCr', '_CollgCr',
    '_Crawfor', '_Edwards', '_Gilbert', '_IDOTRR', '_MeadowV',
    '_Mitchel', '_NAmes', '_NPkVill', '_NWAmes', '_NoRidge',
    '_NridgHt', '_OldTown', '_SWISU', '_Sawyer', '_SawyerW',
    '_Somerst', '_StoneBr', '_Timber', '_Veenker',
]

api_url = 'http://127.0.0.1:8000/predict/'

# ─── Header ────────────────────────────────────────────────────────────────────
st.markdown('<div class="emoji-row">🏡 🌳 🏠</div>', unsafe_allow_html=True)
st.markdown('<div class="cartoon-title">🏠 Дом-О-Метр</div>', unsafe_allow_html=True)
st.markdown('<div class="cartoon-subtitle">Введи параметры — узнай цену своего дома!</div>', unsafe_allow_html=True)
st.markdown('<hr class="cartoon-divider">', unsafe_allow_html=True)

# ─── Form ──────────────────────────────────────────────────────────────────────
st.markdown('<span class="section-badge">📐 Размеры</span>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    area = st.number_input('🛋️ Жилая площадь (кв.фут)', min_value=0, value=0, step=10)
    bsmt = st.number_input('🏚️ Площадь подвала (кв.фут)', min_value=0, value=0, step=10)
with col2:
    bath = st.number_input('🛁 Кол-во ванных комнат', min_value=0, value=0, step=1)
    garage = st.number_input('🚗 Вместимость гаража (машин)', min_value=0, value=0, step=1)

st.markdown('<hr class="cartoon-divider">', unsafe_allow_html=True)
st.markdown('<span class="section-badge">✨ Характеристики</span>', unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    year = st.number_input('📅 Год постройки', min_value=1800, max_value=2025, value=2000, step=1)
with col4:
    overall_qual = st.number_input('⭐ Качество (1–10)', min_value=1, max_value=10, value=5, step=1)

st.markdown('<hr class="cartoon-divider">', unsafe_allow_html=True)
st.markdown('<span class="section-badge">📍 Расположение</span>', unsafe_allow_html=True)
neighborhood = st.selectbox('🗺️ Район', nei_list)

st.markdown('<hr class="cartoon-divider">', unsafe_allow_html=True)

# ─── Submit ────────────────────────────────────────────────────────────────────
if st.button('🔮 Узнать цену!'):
    data = {
        "GrLivArea":    area,
        "YearBuilt":    year,
        "GarageCars":   garage,
        "TotalBsmtSF":  bsmt,
        "FullBath":     bath,
        "OverallQual":  overall_qual,
        "Neighborhood": neighborhood,
    }
    try:
        with st.spinner('🏗️ Считаем...'):
            answer = requests.post(api_url, json=data, timeout=10)

        if answer.status_code == 200:
            result  = answer.json()
            price   = result.get('price', 'N/A')
            # Try to format as currency
            try:
                price_fmt = f"${float(price):,.0f}"
            except (ValueError, TypeError):
                price_fmt = str(price)

            st.markdown(f"""
            <div class="price-tag">
                <div class="label">🎉 Оценочная стоимость дома</div>
                <div class="amount">{price_fmt}</div>
                <div class="currency">USD · approx.</div>
            </div>
            """, unsafe_allow_html=True)
            st.balloons()
        else:
            st.error(f'😬 Ошибка сервера: {answer.status_code}')

    except requests.exceptions.RequestException:
        st.error('🚧 Не удалось подключиться к API. Проверь, запущен ли сервер!')