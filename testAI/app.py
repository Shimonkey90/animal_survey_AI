import streamlit as st

st.title('AI動物調べアプリ')
st.caption('これはテストアプリです')

# subheaderでサブヘッダーを用意
st.subheader('このアプリについて')

# textでテキスト表示
st.text('AIに動物名を伝えるとその動物の特徴を教えてくれます')

with st.form(key='animal_name'):
    # text_inputでテキストボックスを設置
    name = st.text_input('動物名')
    # buttonでボタンの設置
    submit_btn = st.form_submit_button('調査')
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        st.text(f'{name}を調査します！')