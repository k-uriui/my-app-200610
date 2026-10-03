import streamlit as st
import random
from datetime import date
from streamlit_local_storage import LocalStorage

localS = LocalStorage()


omikuji_list = ["大吉", "中吉", "小吉", "凶"]


messages = {
    "大吉": [
        "今日は最高の一日になりそう！",
        "思い切って行動してみると良いことがありそう！",
        "笑顔がきっと幸運を呼び込みます！"
    ],
    "中吉": [
        "ちょっといいこと、あるかもよ。",
        "寄り道してみると幸運に出会うかも。",
        "感謝が大切、身近な人に「ありがとう」。"
    ],
    "小吉": [
        "深呼吸をしてから取り掛かろう。",
        "温かいお茶で一息つきましょう。",
        "人に与えた親切は、いつか自分に還るでしょう"
    ],
    "凶": [
        "慌てず騒がず、一歩ずつ。",
        "抗わずに過ぎ去るのを待つのも、強さ。",
        "明日のために、今日は自分を労わろう。"
    ]
}


images = {
    "大吉": "dai.jpg",
    "中吉": "chu.jpg",
    "小吉": "syo.jpg",
    "凶": "kyo.jpg"
}


# --------------------
# 和風デザイン
# --------------------

st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background-color: #f3ead8 !important;
    position: relative;
}


[data-testid="stAppViewContainer"]::before {
    content: "";
    position: fixed;
    inset: 0;

    background:

        /* 和紙の淡い色片 */

        linear-gradient(
            28deg,
            transparent 0 20%,
            rgba(170, 210, 220, 0.28) 21% 70%,
            transparent 71%
        ) 8% 18% / 35px 14px no-repeat,

        linear-gradient(
            145deg,
            transparent 0 30%,
            rgba(244, 191, 202, 0.30) 31% 72%,
            transparent 73%
        ) 30% 12% / 28px 18px no-repeat,

        linear-gradient(
            75deg,
            transparent 0 25%,
            rgba(155, 205, 218, 0.22) 26% 68%,
            transparent 69%
        ) 72% 14% / 40px 15px no-repeat,

        linear-gradient(
            165deg,
            transparent 0 35%,
            rgba(250, 213, 221, 0.34) 36% 75%,
            transparent 76%
        ) 88% 32% / 30px 16px no-repeat,

        linear-gradient(
            18deg,
            transparent 0 22%,
            rgba(180, 220, 228, 0.24) 23% 68%,
            transparent 69%
        ) 16% 48% / 38px 13px no-repeat,

        linear-gradient(
            120deg,
            transparent 0 28%,
            rgba(246, 202, 212, 0.28) 29% 70%,
            transparent 71%
        ) 55% 40% / 33px 18px no-repeat,

        linear-gradient(
            150deg,
            transparent 0 32%,
            rgba(165, 212, 224, 0.20) 33% 72%,
            transparent 73%
        ) 82% 58% / 38px 14px no-repeat,

        linear-gradient(
            35deg,
            transparent 0 24%,
            rgba(248, 211, 218, 0.25) 25% 68%,
            transparent 69%
        ) 25% 78% / 30px 16px no-repeat,

        linear-gradient(
            135deg,
            transparent 0 30%,
            rgba(190, 225, 231, 0.28) 31% 72%,
            transparent 73%
        ) 68% 82% / 43px 15px no-repeat,


        /* 金箔 */

        linear-gradient(
            112deg,
            transparent 0 38%,
            rgba(185, 135, 20, 0.55) 39%,
            rgba(220, 175, 50, 0.65) 58%,
            rgba(185, 135, 20, 0.30) 72%,
            transparent 73%
        ) 12% 14% / 55px 22px no-repeat,

        linear-gradient(
            155deg,
            transparent 0 25%,
            rgba(195, 145, 25, 0.45) 26%,
            rgba(225, 185, 60, 0.60) 55%,
            rgba(185, 135, 15, 0.25) 68%,
            transparent 69%
        ) 78% 30% / 45px 17px no-repeat,

        linear-gradient(
            98deg,
            transparent 0 42%,
            rgba(190, 140, 20, 0.50) 43%,
            rgba(225, 180, 45, 0.58) 62%,
            rgba(180, 130, 10, 0.28) 73%,
            transparent 74%
        ) 30% 52% / 48px 19px no-repeat,

        linear-gradient(
            145deg,
            transparent 0 30%,
            rgba(190, 140, 20, 0.48) 31%,
            rgba(220, 175, 45, 0.55) 60%,
            rgba(180, 130, 10, 0.25) 72%,
            transparent 73%
        ) 86% 70% / 52px 16px no-repeat;


    pointer-events: none;
    z-index: 0;
}


[data-testid="stAppViewContainer"] > * {
    position: relative;
    z-index: 1;
}


/* タイトル */

h1 {
    color: #9e3d3e !important;
    font-size: 38px;
}


/* 本文 */

p {
    color: #4a4036;
    font-size: 20px;
    line-height: 1.8;
    margin-top: 0 !important;
}


/* ボタン文字 */

button p {
    color: #9e3d3e !important;
}


/* スマホ向けボタン */

[data-testid="stButton"] button {
    width: 100%;
    min-height: 60px;
    font-size: 22px;
}


/* Streamlitのヘッダーを透明にする */

[data-testid="stHeader"] {
    background: transparent !important;
    box-shadow: none !important;
    border-bottom: none !important;
}

</style>
""", unsafe_allow_html=True)


# --------------------
# 初期設定
# --------------------

if "fortune" not in st.session_state:
    st.session_state["fortune"] = localS.getItem("omikuji_fortune")

if "message" not in st.session_state:
    st.session_state["message"] = localS.getItem("omikuji_message")

if "last_date" not in st.session_state:
    st.session_state["last_date"] = localS.getItem("omikuji_last_date")

# --------------------
# 画面
# --------------------

st.title("今日のおみくじ")

st.write("今日の運勢は…？")


# --------------------
# おみくじ
# --------------------

if st.button("おみくじをひく"):

    if st.session_state["last_date"] != str(date.today()):

        result = random.choice(omikuji_list)
        message = random.choice(messages[result])
        image = images[result]

        st.session_state["fortune"] = result
        st.session_state["message"] = message
        st.session_state["last_date"] = str(date.today())

        localS.setItem("omikuji_fortune", result, key="set_fortune")
        localS.setItem("omikuji_message", message, key="set_message")
        localS.setItem("omikuji_last_date", str(date.today()), key="set_date")

        st.write(f"今日の運勢は{result}です。")
        st.image(image, use_container_width=True)
        st.write(message)

    else:

        fortune = st.session_state["fortune"]
        message = st.session_state["message"]
        image = images[fortune]

        st.write("おみくじは１日１回です。")
        st.write(f"今日の運勢は{fortune}です。")
        st.image(image, use_container_width=True)
        st.write(message)
        st.write("続きはまた明日！")
