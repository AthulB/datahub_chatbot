import streamlit as st


class Message:
    def __init__(self):
        if 'messages' not in st.session_state:
            st.session_state['messages'] = [{"role": "assistant", "content": "How can I help you?"}]

    def write_messages(self, query, reply):
        st.session_state.messages.append({"role": "user", "content": query})
        st.session_state.messages.append({"role": "assistant", "content": reply})

    def clear_messages(self):
        st.session_state.messages.clear()

    def radio_callback(self, main_category, options):
        cat = st.session_state[main_category]
        if cat not in options.keys():
            self.write_messages(cat, "No unique links available for the selected category.")
        else:
            self.write_messages(cat, options[cat])

    def display_chat_messages(self):
        # Display chat messages
        if st.session_state.messages:
            for message in st.session_state.messages:
                if message['role'] == 'user':
                    st.chat_message("user").markdown(message['content'])
                else:
                    st.chat_message("assistant").markdown(message['content'])