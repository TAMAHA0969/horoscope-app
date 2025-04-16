
import streamlit as st
import datetime
import math
import calendar
from dateutil import parser

st.set_page_config(page_title="TAMAHAの星座と宿命数")

st.title("🔮 TAMAHAの星座と宿命数")

name = st.text_input("お名前（ニックネームでもOK）", value="")
birth_date = st.date_input("生年月日を選んでください", value=datetime.date(2000, 1, 1), min_value=datetime.date(1900, 1, 1))

if st.button("診断スタート！"):

    # 星座判定関数
    def get_zodiac_sign(month, day):
        zodiac_signs = [
            ("山羊座", 1, 19), ("水瓶座", 2, 18), ("魚座", 3, 20), ("牡羊座", 4, 19), ("牡牛座", 5, 20),
            ("双子座", 6, 20), ("蟹座", 7, 22), ("獅子座", 8, 22), ("乙女座", 9, 22), ("天秤座", 10, 22),
            ("蠍座", 11, 21), ("射手座", 12, 21), ("山羊座", 12, 31)
        ]
        for sign, m, d in zodiac_signs:
            if month == m and day <= d:
                return sign
        return "山羊座"

    # 宿命数を日から
    def get_shukumei_number(day):
        if day in [11, 22, 33]:
            return day
        while day >= 10:
            day = sum(int(d) for d in str(day))
        return day

    # 運命数：全て足す
    def get_unmei_number(year, month, day):
        total = sum(int(d) for d in f"{year}{month:02d}{day:02d}")
        while total not in [11, 22, 33] and total >= 10:
            total = sum(int(d) for d in str(total))
        return total

    # 使命数：月と日
    def get_shimei_number(month, day):
        total = sum(int(d) for d in f"{month:02d}{day:02d}")
        while total not in [11, 22, 33] and total >= 10:
            total = sum(int(d) for d in str(total))
        return total

    # 宿命分類と特徴
    role_map = {
        "leader": [1, 6, 9],
        "supporter": [2, 4, 7],
        "moodmaker": [3, 5, 8],
    }

    role_descriptions = {
        "leader": "組織を引っ張るリーダー。責任感が強く、指導力や統率力を持つ。",
        "supporter": "組織の調和を保ち、冷静な判断力で支える縁の下の力持ち。",
        "moodmaker": "活発でエネルギッシュ。人を楽しませ、場を明るくするムードメーカー。",
    }

    shukumei_advices = {
        1: "自分を信じて突き進め！先駆者の道はあなたが切り拓く。",
        2: "支える力が強み。無理に前に出なくても、陰の力が光る！",
        3: "自由と楽しさが鍵。型にはまらず、自分の感性を信じよう。",
        4: "地道な努力が実を結ぶ。焦らず、一歩ずつ確実に前進を！",
        5: "変化を恐れず、新しい世界へ飛び込もう！柔軟さが武器。",
        6: "人を支えるのは素晴らしい。でも、自分を大事にすることも忘れずに！",
        7: "一人の時間があなたを成長させる。内なる声に耳を傾けて。",
        8: "成功をつかむ力あり！自信を持って堂々とリーダーシップを発揮しよう。",
        9: "すべてを受け入れる大きな愛を持つ人。手放すことで新たな道が開く。",
        11: "特別な意味を持つ数字です。スピリチュアルな感性を活かして、人の心を照らす存在に。",
        22: "世界を変える可能性を秘めたマスターナンバー。ビジョンを信じて行動を。",
        33: "深い愛と奉仕の心を持つ。人々の癒しとなる存在です。",
    }

    zodiac = get_zodiac_sign(birth_date.month, birth_date.day)
    shukumei = get_shukumei_number(birth_date.day)
    unmei = get_unmei_number(birth_date.year, birth_date.month, birth_date.day)
    shimei = get_shimei_number(birth_date.month, birth_date.day)

    role = "不明"
    for r, nums in role_map.items():
        if (shukumei in nums) or (shukumei == 11 and 2 in nums) or (shukumei == 22 and 4 in nums) or (shukumei == 33 and 6 in nums):
            role = r
            break

    st.subheader(f"🌟 {name}さんの結果 🌟")
    st.markdown(f"**星座：** {zodiac}")
    st.markdown(f"**宿命数：** {shukumei}（{role_map.get(role, [])} に該当／**{role_map.get(role, [])} → {role}**）")
    st.markdown(f"**運命数：** {unmei}")
    st.markdown(f"**使命数：** {shimei}")

    if role != "不明":
        st.markdown(f"🔍 **あなたの役割：{role_map.get(role, [])} → {role.capitalize()}**")
        st.markdown(f"🤝 **特徴：** {role_descriptions[role]}")
    st.markdown(f"📩 **宿命数からのひとこと：** {shukumei_advices.get(shukumei, '自分らしく輝いてください！')}")
