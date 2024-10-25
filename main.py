import streamlit as st
import pandas as pd

from utils.style import ui_markdown
from utils.util import create_option_link, read_excel
from modules.lookup import QueryLookup
from session.message import Message
from modules.faq import faq
from modules.guided_tour import guided_tour




if __name__ == '__main__':
    # Read Chatbot Lookup file
    chatbot_file_path = 'data/chatbot-1.xlsx'
    df = read_excel(chatbot_file_path)

    # ============Render the styling for sidebar=============
    ui_markdown()

    # =============Render the clickable options in sidebar======================
    msgs = Message()
    main_categories = df['Main'].unique().tolist()

    for main_category in main_categories:
        with st.sidebar.expander(main_category, expanded=False):  # Create an expander for each COE
            options = create_option_link(df, main_category)

            selected_category = st.radio(
                "",
                options=options.keys(),
                index=None,
                key=main_category,
                on_change=msgs.radio_callback,
                args=(main_category, options,)
            )
    # # check if columns from excel match the dataframe if not handle missing values
    # for col in ['Main', 'Category', 'Subcategory', 'Questions', 'Answers', 'Links', 'Page']:
    #     if col not in df.columns:
    #         df[col] = ''
    # df.fillna('', inplace=True)

    # ============ Handling User Chat Input ===============

    lookup = QueryLookup(df)
    lookup.create_df_matrix()

    # User input bar for chatbot
    user_input = st.chat_input("Your Question")
    if user_input:
        results = lookup.get_all_matches(user_input)
        msgs.write_messages(user_input, results)

    # ==================Displaying all the messages================
    msgs.display_chat_messages()


    # =================Rendering Guided Tour Section=================

    guided_df = read_excel('data/Guided_Tour.xlsx')

    if 'selected_phase' not in st.session_state:
        st.session_state.selected_phase = None
    if 'selected_process' not in st.session_state:
        st.session_state.selected_process = None
    if 'project_day_clicked' not in st.session_state:
        st.session_state.project_day_clicked = False

    st.sidebar.markdown('<div class="divider-line"></div>', unsafe_allow_html=True)

    guided_tour(guided_df)

    # ======================Rendering FAQ Section=====================

    faq_df = read_excel(chatbot_file_path, sheet_name='FAQ')

    faq(faq_df)


