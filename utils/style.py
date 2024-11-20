import streamlit as st


def ui_markdown():
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] *{
            background-color: #4F2170;

        }
        [data-testid="stSidebar"] * {
            color: white;
        }
        .title-container {
            text-align: center;
            color: #4F2170;
            font-weight: bold;
         }
        [data-testid="baseButton-secondary"] {
            background-color: #4F2170; !important
            color: white; !important
            border: 2px solid white; !important
            border-radius: 18px; !important
            padding: 10px 20px; !important
            font-size: 16px; !important

            }
        [data-testid="baseButton-secondary"]:hover {
            background-color: #3b1a56; !important
            }

        .horizontal-container {
            display: flex;
            # justify-content: center;
            # align-items: center;
            # gap: 20px;
            # flex-wrap: nowrap;
            background-color: #4F2170;
        }

        .phase-button {
            background-color: #FFB300;
            color: white;
            border-radius: 8px;
            padding: 12px;
            font-weight: bold;
            margin: 5px;
            width: 200px;
            text-align: center;
            cursor: pointer;
            display: inline-block;
        }
        .phase-button:hover {
            background-color: #FF4500;
        }
        .divider-line {
            border-top: 2px solid white;
            margin: 2px 0;
        }
        [data-testid="stSidebar"] .stRadio input[type="radio"] {
            appearance: auto;  /* Reset to default browser appearance */
            margin-right: 8px; /* Add some space between the circle and text */
        }

        [data-testid="stSidebar"] .stRadio label {
            color: white;  /* Adjust text color if necessary */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='title-container'><h1>D&A Chatbot 💬</h1></div>", unsafe_allow_html=True)

    logo_path = "data/logo.png"
    st.sidebar.image(logo_path, width=280)
    st.sidebar.markdown('<div class="divider-line"></div>', unsafe_allow_html=True)

    if st.sidebar.button("🏠 Home", key="home_button"):
        st.session_state.clear()
        # st.experimental_rerun()
    st.sidebar.markdown('<div class="divider-line"></div>', unsafe_allow_html=True)

    # st.sidebar.markdown('<div class="horizontal-container">', unsafe_allow_html=True)
