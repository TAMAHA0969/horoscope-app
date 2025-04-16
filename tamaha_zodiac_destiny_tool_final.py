
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="TAMAHAの星座と宿命数", page_icon="🔮")

st.title("🔮 TAMAHAの星座と宿命数")

name = st.text_input("お名前（ニックネームでもOK）", "あなた")
birth_date = st.date_input("生年月日を選んでください", format="YYYY/MM/DD")

if st.button("診断スタート！"):
    birthday = birth_date.strftime("%Y-%m-%d")
    year, month, day = birth_date.year, birth_date.month, birth_date.day

    # 星座の計算
    zodiac_signs = [
        ("山羊座", (1, 1), (1, 19)), ("水瓶座", (1, 20), (2, 18)), ("魚座", (2, 19), (3, 20)),
        ("牡羊座", (3, 21), (4, 19)), ("牡牛座", (4, 20), (5, 20)), ("双子座", (5, 21), (6, 20)),
        ("蟹座", (6, 21), (7, 22)), ("獅子座", (7, 23), (8, 22)), ("乙女座", (8, 23), (9, 22)),
        ("天秤座", (9, 23), (10, 22)), ("蠍座", (10, 23), (11, 21)), ("射手座", (11, 22), (12, 21)), ("山羊座", (12, 22), (12, 31))
    ]

    zodiac = "不明"
    for sign, (start_month, start_day), (end_month, end_day) in zodiac_signs:
        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
            zodiac = sign
            break

    # 宿命数
    destiny_raw = day
    destiny_special_note = ""
    if destiny_raw in [11, 22, 33]:
        destiny = destiny_raw
        destiny_group = {11: 2, 22: 4, 33: 6}[destiny_raw]
        destiny_role = {2: "サポーター", 4: "サポーター", 6: "リーダー"}[destiny_group]
        destiny_feature = {
            11: "直感力と感受性に優れたビジョナリー。インスピレーションで道を切り開く人。",
            22: "世界を動かすマスタープランナー。大きな夢を着実に形にしていこう。",
            33: "無償の愛を注ぐヒーラー。誰かの幸せを心から願える存在。"
        }[destiny_raw]
    else:
        destiny = sum(map(int, str(destiny_raw)))
        while destiny > 9:
            destiny = sum(map(int, str(destiny)))
        destiny_group = destiny
        if destiny in [1, 6, 9]:
            destiny_role = "リーダー"
        elif destiny in [2, 4, 7]:
            destiny_role = "サポーター"
        else:
            destiny_role = "ムードメーカー"
        destiny_feature = {
            1: "自分を信じて突き進め！先駆者の道はあなたが切り拓く。",
            2: "支える力が強み。無理に前に出なくても、陰の力が光る！",
            3: "自由と楽しさが鍵。型にはまらず、自分の感性を信じよう。",
            4: "地道な努力が実を結ぶ。焦らず、一歩ずつ確実に前進を！",
            5: "変化を恐れず、新しい世界へ飛び込もう！柔軟さが武器。",
            6: "人を支えるのは素晴らしい。でも、自分を大事にすることも忘れずに！",
            7: "一人の時間があなたを成長させる。内なる声に耳を傾けて。",
            8: "成功をつかむ力あり！自信を持って堂々とリーダーシップを発揮しよう。",
            9: "すべてを受け入れる大きな愛を持つ人。手放すことで新たな道が開く！"
        }[destiny]

    # 運命数（全ての数字を足す）
    all_digits = list(str(year) + str(month).zfill(2) + str(day).zfill(2))
    life_path = sum(map(int, all_digits))
    while life_path > 9 and life_path not in [11, 22, 33]:
        life_path = sum(map(int, str(life_path)))

    # 使命数（月＋日）
    mission = month + day
    while mission > 9 and mission not in [11, 22, 33]:
        mission = sum(map(int, str(mission)))

    # 結果表示
    st.markdown(f"## ✨ {name}さんの結果 ✨")
    st.markdown(f"**星座：** {zodiac}")
    st.markdown(f"**宿命数：** {destiny_raw}（{destiny_role}（宿命数{destiny_group}））")
    st.markdown(f"**運命数：** {life_path}")
    st.markdown(f"**使命数：** {mission}")
    st.markdown(f"🔍 **あなたの役割：** {destiny_role}（宿命数{destiny_group}）→ {destiny_feature}")
