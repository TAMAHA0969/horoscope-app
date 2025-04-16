
import streamlit as st
from datetime import datetime
import calendar

# 宿命数の分類と特徴
shukumei_roles = {
    1: "リーダー",
    2: "サポーター",
    3: "ムードメーカー",
    4: "サポーター",
    5: "ムードメーカー",
    6: "リーダー",
    7: "サポーター",
    8: "ムードメーカー",
    9: "リーダー",
    11: "サポーター",
    22: "サポーター",
    33: "リーダー"
}

shukumei_comments = {
    1: "自分を信じて突き進め！先駆者の道はあなたが切り拓く。",
    2: "支える力が強み。無理に前に出なくても、陰の力が光る！",
    3: "自由と楽しさが鍵。型にはまらず、自分の感性を信じよう。",
    4: "地道な努力が実を結ぶ。焦らず、一歩ずつ確実に前進を！",
    5: "変化を恐れず、新しい世界へ飛び込もう！柔軟さが武器。",
    6: "人を支えるのは素晴らしい。でも、自分を大事にすることも忘れずに！",
    7: "一人の時間があなたを成長させる。内なる声に耳を傾けて。",
    8: "成功をつかむ力あり！自信を持って堂々とリーダーシップを発揮しよう。",
    9: "すべてを受け入れる大きな愛を持つ人。手放すことで新たな道が開く！",
    11: "特別な意味を持つ数字です。",
    22: "世界を動かす可能性を秘めたマスタープランナー。ビジョンを信じて行動を。",
    33: "無条件の愛を広げるヒーラー。人々に癒しと希望を届けよう。"
}

st.title("🔮 TAMAHAの星座と宿命数")

name = st.text_input("お名前（ニックネームでもOK）", "ゲスト")
birth_date = st.date_input("生年月日を選んでください", min_value=datetime(1900, 1, 1), max_value=datetime.today())

if st.button("診断スタート！"):
    # 星座を計算
    month = birth_date.month
    day = birth_date.day

    zodiac_signs = [
        ("山羊座", (1, 1), (1, 19)),
        ("水瓶座", (1, 20), (2, 18)),
        ("魚座", (2, 19), (3, 20)),
        ("牡羊座", (3, 21), (4, 19)),
        ("牡牛座", (4, 20), (5, 20)),
        ("双子座", (5, 21), (6, 21)),
        ("蟹座", (6, 22), (7, 22)),
        ("獅子座", (7, 23), (8, 22)),
        ("乙女座", (8, 23), (9, 22)),
        ("天秤座", (9, 23), (10, 23)),
        ("蠍座", (10, 24), (11, 22)),
        ("射手座", (11, 23), (12, 21)),
        ("山羊座", (12, 22), (12, 31))
    ]

    zodiac = "不明"
    for sign, start, end in zodiac_signs:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            zodiac = sign
            break

    # 宿命数（誕生日の日）
    shukumei_raw = day
    if shukumei_raw in [11, 22, 33]:
        shukumei = shukumei_raw
    else:
        shukumei = sum(map(int, str(shukumei_raw)))
        while shukumei > 9:
            shukumei = sum(map(int, str(shukumei)))

    role = shukumei_roles.get(shukumei, "不明")
    advice = shukumei_comments.get(shukumei, "特別な意味を持つ数字です。")

    st.markdown(f"✨ {name}さんの結果 ✨")
    st.markdown(f"星座：**{zodiac}**")
    st.markdown(f"宿命数：**{shukumei}（{role}）**")
    st.markdown(f"🔍 **あなたの役割：{role}（宿命数{shukumei}）**")
    st.markdown(f"📄 **宿命数からのひとこと：** {advice}")
