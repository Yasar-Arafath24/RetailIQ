import streamlit as st


def load_css():

    st.markdown(

    """

    <style>


    /* =========================
       MAIN APP BACKGROUND
    ========================== */


    .stApp {

        background-color: #f5f7fb;

        color: #1f2937;

    }



    /* =========================
       ALL TEXT FIX
    ========================== */


    h1, h2, h3, h4, h5, h6 {

        color: #111827 !important;

        font-weight: 700;

    }



    p, span, label, div {

        color: #374151;

    }



    /* =========================
       SIDEBAR
    ========================== */


    section[data-testid="stSidebar"] {


        background:

        linear-gradient(

        180deg,

        #111827,

        #1e293b

        );

    }



    section[data-testid="stSidebar"] * {


        color: white !important;

    }



    /* sidebar select box */


    section[data-testid="stSidebar"]

    .stSelectbox div {


        background-color:#334155;

        color:white;

        border-radius:10px;

    }



    /* =========================
       METRIC CARDS
    ========================== */


    div[data-testid="metric-container"] {


        background:white;


        padding:20px;


        border-radius:18px;


        box-shadow:

        0 8px 20px

        rgba(0,0,0,0.08);


        border:

        1px solid #e5e7eb;


    }



    div[data-testid="metric-container"] label {


        color:#6b7280 !important;

        font-size:14px;

    }



    div[data-testid="metric-container"]


    div {


        color:#111827 !important;

        font-size:28px;

        font-weight:700;

    }



    /* =========================
       BUTTONS
    ========================== */


    .stButton button {


        background:

        linear-gradient(

        135deg,

        #2563eb,

        #1d4ed8

        );


        color:white;


        border:none;


        border-radius:12px;


        padding:10px 20px;


        font-weight:600;


        transition:0.3s;

    }



    .stButton button:hover {


        transform:scale(1.03);


    }



    /* =========================
       DATAFRAME
    ========================== */


    .stDataFrame {


        border-radius:15px;

        overflow:hidden;


    }



    /* =========================
       INPUT BOXES
    ========================== */


    input, textarea {


        background:white !important;


        color:#111827 !important;


        border-radius:10px !important;

    }



    /* =========================
       ALERT BOXES
    ========================== */


    .stAlert {


        border-radius:15px;

    }



    /* =========================
       DIVIDER
    ========================== */


    hr {


        border-color:#e5e7eb;

    }



    </style>


    """,

    unsafe_allow_html=True

    )