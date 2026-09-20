import streamlit as st
import time

# Page Configuration
st.set_page_config(
    page_title="Happy Birthday Gauri! 🎉",
    page_icon="🎂",
    layout="centered"
)

# Custom Styling (Vibrant Colourful Theme + Extra Large Text)
st.markdown("""
    <style>
    /* Vibrant Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #a1c4fd 100%) !important;
        color: #1a1a2e !important;
    }
    
    /* Main Title Styling */
    .main-title {
        text-align: center;
        color: #581225;
        font-family: 'Comic Sans MS', 'Trebuchet MS', cursive, sans-serif;
        font-size: 3.5rem;
        font-weight: 900;
        letter-spacing: 2px;
        margin-bottom: 8px;
        text-shadow: 2px 2px 8px rgba(255, 255, 255, 0.8);
    }
    
    .sub-title {
        text-align: center;
        color: #3b185f;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 25px;
    }
    
    /* Cake Box with Bright Contrast */
    .cake-box {
        background-color: #ffffff;
        border: 4px solid #ff4757;
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
        font-size: 1.3rem;
        font-weight: bold;
        line-height: 1.35;
        white-space: pre;
        box-shadow: 0 10px 30px rgba(255, 71, 87, 0.3);
        margin-bottom: 25px;
    }
    
    .flame {
        color: #ff3f34;
        font-size: 1.4rem;
        font-weight: 900;
        text-shadow: 0 0 10px #ffaa00;
    }
    
    .smoke {
        color: #70a1ff;
        font-size: 1.4rem;
        font-weight: bold;
    }
    
    .cake-body {
        color: #2ed573;
    }

    /* Wish Letter Card with Extra Large Text */
    .letter-card {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 35px;
        border-radius: 20px;
        border: 3px solid #ff6b81;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.15);
        margin-top: 25px;
    }
    
    .wish-heading {
        color: #d63031;
        font-size: 2.2rem;
        font-weight: 900;
        margin-bottom: 20px;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    
    .wish-text {
        color: #2d3436 !important;
        font-size: 1.35rem !important;
        font-weight: 600 !important;
        line-height: 1.8 !important;
        margin-bottom: 14px !important;
    }
    
    .signature {
        text-align: right;
        color: #6c5ce7;
        font-weight: 900;
        font-size: 1.6rem;
        margin-top: 30px;
    }
    
    /* Make Streamlit Buttons Large & Bold */
    div.stButton > button {
        font-size: 1.4rem !important;
        font-weight: bold !important;
        border-radius: 15px !important;
        background-color: #ff4757 !important;
        color: white !important;
        border: none !important;
        padding: 12px 24px !important;
        box-shadow: 0 6px 20px rgba(255, 71, 87, 0.4) !important;
    }
    </style>
""", unsafe_allow_html=True)

# App States
if "step" not in st.session_state:
    st.session_state.step = "start"

st.markdown("<h1 class='main-title'>💖 HAPPY BIRTHDAY GAURI 💖</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>✨ A Special Birthday Surprise for You! ✨</p>", unsafe_allow_html=True)

# STEP 1: START SURPRISE
if st.session_state.step == "start":
    st.write("")
    st.write("")
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        if st.button("🎁 Click Here to Unlock Surprise!", use_container_width=True):
            st.session_state.step = "candle"
            st.rerun()

# STEP 2: MAKE A WISH & BLOW CANDLE
elif st.session_state.step == "candle":
    st.markdown("## 🕯️ Step 1: Make a Wish!")
    st.info("💡 **Close your eyes, make a beautiful wish, and blow out the candles!**")

    lit_cake = """
         <span class='flame'>  (i)     (i)     (i)  </span>
         <span class='flame'>   ||      ||      ||   </span>
        .-----. .-----. .-----.
       (   i   )(   i   )(   i   )
      <span class='cake-body'>=============================</span>
      <span class='cake-body'>|   H A P P Y   D A Y !     |</span>
      <span class='cake-body'>|~~~~~~~~~~~~~~~~~~~~~~~~~~~|</span>
      <span class='cake-body'>|    G A U R I  🎂 ✨      |</span>
      <span class='cake-body'>=============================</span>
     \\_____________________________/
    """
    st.markdown(f"<div class='cake-box'>{lit_cake}</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("💨 Blow Out Candles!", use_container_width=True):
            st.session_state.step = "blown"
            st.rerun()
    with col2:
        st.audio_input("🎤 Or Blow into your Mic!")

# STEP 3: BLOWN CANDLES & FIREWORKS & LARGE LETTER
elif st.session_state.step in ["blown", "letter"]:
    st.balloons()

    blown_cake = """
         <span class='smoke'>  (~)     (~)     (~)  </span>
         <span class='smoke'>   ||      ||      ||   </span>
        .-----. .-----. .-----.
       (   .   )(   .   )(   .   )
      <span class='cake-body'>=============================</span>
      <span class='cake-body'>|   H A P P Y   D A Y !     |</span>
      <span class='cake-body'>|~~~~~~~~~~~~~~~~~~~~~~~~~~~|</span>
      <span class='cake-body'>|    G A U R I  🎂 ✨      |</span>
      <span class='cake-body'>=============================</span>
     \\_____________________________/
    """
    st.markdown(f"<div class='cake-box'>{blown_cake}</div>", unsafe_allow_html=True)
    st.success("🎉 **Your wish has been locked in! May all your dreams come true!** ✨")

    if st.session_state.step == "blown":
        time.sleep(1)
        st.session_state.step = "letter"
        st.rerun()

    # Extended Message List (Clean strings with correct comma formatting)
    messages = [
        "There are people who make the world a little lighter, simply by being a part of it.",
        "You bring so much warmth, laughter, and genuine joy to the lives of everyone around you.",
        "On your birthday, I want to remind you how much your presence, kindness, and strength are appreciated.",
        "May this upcoming year treat you with the same grace, endless happiness, and comfort that you so effortlessly give to others every single day.",
        "Keep shining bright, and keep being uniquely you.",
        "Life moves so fast, but moments like today remind us to pause and celebrate the people who truly matter.",
        "Your ability to turn ordinary days into memorable ones is a gift to everyone who knows you.",
        "Through every challenge, your resilience and quiet strength always shine through.",
        "You have this amazing way of listening, understanding, and making people feel valued.",
        "In a world that can often feel loud and chaotic, your calm and steady nature is a true blessing.",
        "Thank you for all the shared laughs, the spontaneous conversations, and the constant positivity.",
        "Thank you for being someone people can rely on, no matter the time or place.",
        "As you step into another incredible year, I hope you take time to celebrate yourself.",
        "I hope you realize how big of an impact your small acts of kindness have on those around you.",
        "May this year bring you closer to all the dreams and goals you've been working toward.",
        "May you find success in every endeavor, courage in every hurdle, and peace in every quiet moment.",
        "May your days be filled with good health, boundless energy, and non-stop inspiration.",
        "I wish you surrounding yourself with people who uplift you just as much as you uplift them.",
        "Never doubt the value you bring to the lives of the people around you.",
        "Never stop pursuing what makes your eyes light up and your heart feel full.",
        "The world is undeniably a better, brighter, and happier place with you in it.",
        "Celebrate today with all the excitement and cheer that you rightfully deserve.",
        "Here’s to another year of growth, great memories, and endless possibilities.",
        "Cheers to you, your journey, and everything wonderful that lies ahead!"
    ]

    st.markdown("<div class='letter-card'>", unsafe_allow_html=True)
    st.markdown("<div class='wish-heading'>Dear Gauri,</div>", unsafe_allow_html=True)

    for line in messages:
        st.markdown(f"<p class='wish-text'>✨ {line}</p>", unsafe_allow_html=True)
        time.sleep(0.5)

    st.markdown("<p class='signature'>— Wishing you the absolute best, always! 🎈🎉</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    time.sleep(1)
    st.snow()