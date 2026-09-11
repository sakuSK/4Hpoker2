import streamlit as st

i=1

with st.sidebar:
    st.page_link("main.py", label="ホーム", icon="❤️")
    st.page_link("pages/1_poker.py", label="ポーカー", icon="♠️")
    st.page_link("pages/2_roulette.py", label="ルーレット", icon="♣️")
    st.page_link("pages/3_blackjack.py", label="ブラックジャック", icon="♦️")

st.title("ポーカー")

st.write("")
st.write("")
st.write("")
st.write("ポーカーはローリスクローリターンとハイリスクハイリターンの２台用意しています。")
st.write("初心者はローリスクローリターン台を強くお勧めいたします。")  
st.header("ゲームの流れ（両卓共通）")
st.write("カードを7枚貰い、確認後、ベット（賭けを）し、カードを任意で交換。")
st.write("その後追加ベットをし、カードを再度最大3枚まで交換し、ショーダウンする。（作れる一番強い役を出す）")
st.header("ベット")
st.write("ベットはプレイヤー全員のベット額が等しくなるまで続きます。")    
st.write("右端のプレイヤーから時計回りにいくら賭けるか宣言し、賭けていきます。")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.image("/Users/saku/Desktop/4Hpoker/役表.jpg", caption="役表")
