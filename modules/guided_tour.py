import streamlit as st


def guided_tour(guided_df):
    # project day in life process
    if st.sidebar.button("📋 Project Day In Life", key="project_day_button"):
        st.session_state.clear()
        # st.experimental_rerun()
        st.session_state.project_day_clicked = True
        st.session_state.selected_phase = None
        st.session_state.selected_process = None  #
        st.session_state.messages = []
    # phases selection
    if st.session_state.project_day_clicked:
        st.write("### What Phase are you currently in?")
        phases = guided_df['Phases'].unique().tolist()
        phase_emojis = {
            'Pre Discovery': '🔍',
            'Discovery & Analysis': '📊',
            'Design': '✏️',
            'Build': '💻',
            'Testing': '🧪',
            'Hyper Care': '🚀',
            'Support': '⚙️'
        }
        st.markdown('<div class="horizontal-container">', unsafe_allow_html=True)
        for phase in phases:
            emoji = phase_emojis.get(phase, '')
            if st.button(f"{emoji} {phase}", key=phase, use_container_width=True):
                st.session_state.selected_phase = phase
        st.markdown('</div>', unsafe_allow_html=True)

    # Process selection based on phase
    if st.session_state.selected_phase:
        selected_phase = st.session_state.selected_phase
        st.session_state.messages = []
        st.write(f"### {selected_phase} phase: What process do you need help with?")
        processes = guided_df[guided_df['Phases'] == selected_phase]['Process'].unique().tolist()
        st.markdown('<div class="horizontal-container">', unsafe_allow_html=True)
        for process in processes:
            if st.button(f"{process}", key=f"process_{process}"):
                st.session_state.selected_process = process
        st.markdown('</div>', unsafe_allow_html=True)

    # Show details based on the selected process
    if st.session_state.selected_process:
        selected_process = st.session_state.selected_process
        st.write(f"### Details for **{selected_process}** process:")

        # Filter the DataFrame for the selected phase and process
        process_data = guided_df[
            (guided_df['Phases'] == selected_phase) &
            (guided_df['Process'] == selected_process)
            ]
        # display details from excel(show link name redirect to link URL)
        for _, row in process_data.iterrows():
            document_name = row['Document']
            document_url = row['Document_link']
            st.write(
                f"**Document**: [{document_name}]({document_url})" if document_url else f"**Document**: {document_name}")

            spoc_name = row['SPOC']
            spoc_url = row['SPOC_link']
            st.write(f"**SPOC**: [{spoc_name}]({spoc_url})" if spoc_url else f"**SPOC**: {spoc_name}")

            raci_name = row['RACI']
            raci_url = row['RACI_link']
            st.write(f"**RACI**: [{raci_name}]({raci_url})" if raci_url else f"**RACI**: {raci_name}")
            st.write("---")
            st.session_state.clear()

        st.session_state.messages = []