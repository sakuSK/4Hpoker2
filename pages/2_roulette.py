import streamlit as st


with st.sidebar:
    st.page_link("main.py", label="ホーム", icon="❤️")
    st.page_link("pages/1_poker.py", label="ポーカー", icon="♠️")
    st.page_link("pages/2_roulette.py", label="ルーレット", icon="♣️")
    st.page_link("pages/3_blackjack.py", label="ブラックジャック", icon="♦️")

st.title("ルーレット")
st.subheader("ルーレットとは")
st.write("ルーレットを回して出る数を予想してかけるゲーム。")
st.write("全員がかけ終えた後、ルーレットを回し、チップを受け渡します。")
st.subheader("ベットの仕方")
st.write("一つの数字:36倍")
st.write("格子点（四つの数字）:5倍")
st.write("赤・黒:2倍")
st.write("EVEN（偶数）・ODD（奇数）:2倍")
st.write("前半・後半:2倍")
st.write("3分割:3倍")
