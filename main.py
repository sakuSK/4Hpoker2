import streamlit as st

st.title("4H ゲームルール")
st.markdown(''':rainbow[BIG DREAM] ''')
st.subheader("ようこそ！")
st.write("右上のマークを押し、ゲーム名を選択するとルールの確認ができます！")
st.write("")
st.page_link("https://www.instagram.com/nagoya.4h2026?stkn=MWkyZ2pyMXZ6OWYyZg%3D%3D&utm_source=qr", label="instagramのフォローはコチラからお願いします!" )
st.write("このサイトに不具合、お気づきの点がございましたらコチラにご連絡ください。")
st.write("メアド")
st.write("")
st.write("")
st.write("")




with st.sidebar:
    st.page_link("main.py", label="ホーム", icon="❤️")
    st.page_link("pages/1_poker.py", label="ポーカー", icon="♠️")
    st.page_link("pages/2_roulette.py", label="ルーレット", icon="♣️")
    st.page_link("pages/3_blackjack.py", label="ブラックジャック", icon="♦️")




