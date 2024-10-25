import streamlit as st


def faq(df):
    if st.sidebar.button("📚 FAQs", key="faq_button"):
        st.session_state.clear()

        st.write("### Frequently Asked Questions")

        for _, row in df.iterrows():
            question = row['Common_Question']
            link_name = row['Name']
            link_url = row['Ans_Links']
            st.write(f"**Q:** {question}")
            if link_name and link_url:
                st.write(f"- **Link:** [{link_name}]({link_url})")
            st.write("---")