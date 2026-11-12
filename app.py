import streamlit as st

# st.set_page_config(page_title="DigiSiv", page_icon=":material/edit:")
pg = st.navigation(
    [
        st.Page("p3_z_trans.py"),
    ]
)
pg.run()