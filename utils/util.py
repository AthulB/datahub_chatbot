import pandas as pd
import streamlit as st


@st.cache_resource
def read_excel(file_path, sheet_name=None):
    if sheet_name:
        return pd.read_excel(file_path, sheet_name=sheet_name)
    else:
        return pd.read_excel(file_path)


# redirecting to certain slide/page of doc
def construct_link(base_link, page):
    if page:
        return f"{base_link}#page={page}"
    return base_link


def create_option_link(df, main_category):
    df_filtered = df[df['Main'].str.strip().str.lower() == main_category.strip().lower()]
    options = {}
    for _,row in df_filtered.iterrows():
        link_name = row['Links'].strip()
        link_url = construct_link(row['Answers'].strip(), None)
        if f"• {row['Category']}" not in options:
            options[f"• {row['Category']}"] = set()
        options[f"• {row['Category']}"].add(f"- [{link_name}]({link_url})")

    for key in options.keys():
        lst = list(options[key])
        options[key] = "\n\n".join(lst)
    return options
