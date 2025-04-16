
import streamlit as st
from datetime import datetime
import math
import calendar

st.set_page_config(page_title="TAMAHAの星座と宿命数", layout="centered")

st.title("🔮 TAMAHAの星座と宿命数")

name = st.text_input("お名前（ニックネームでもOK）")
birth_date = st.date_input("生年月日を選んでください", value=datetime(2000, 1, 1),
                           min_value=datetime(1900, 1, 1), max_value=datetime.today())

if st.button("診断スタート！"):

    # 星座の計算
    def get_zodiac(month, day):
        zodiacs = [
            ("山羊座", (1, 20)), ("水瓶座", (2, 19)), ("魚座", (3, 21)),
            ("牡羊座", (4, 20)), ("牡牛座", (5, 21)), ("双子座", (6, 22)),
            ("蟹座", (7, 23)), ("獅子座", (8, 23)), ("乙女座", (9, 23)),
            ("天秤座", (10, 24)), ("蠍座", (11, 23)), ("射手座", (12, 22)), ("山羊座", (12, 31))
        ]
        for sign, (m, d) in zodiacs:
            if (month, day) <= (m, d):
                return sign
        return "山羊座"

    # 運命数計算（全ての数字の合計を1桁になるまで）
    def calc_unmei(year, month, day):
        num = int(f"{year}{month:02d}{day:02d}")
        while num > 9 and num not in [11, 22, 33]:
            num = sum(map(int, str(num)))
        return num

    # 宿命数（日）
    def calc_shukumei(day):
        return day if day in [11, 22, 33] else sum(map(int, str(day)))

    # 使命数（月＋日）
    def calc_shimei(month, day):
        total = month + day
        while total > 9 and total not in [11, 22, 33]:
            total = sum(map(int, str(total)))
        return total

    birth = birth_date
    zodiac = get_zodiac(birth.month, birth.day)
    shukumei = calc_shukumei(birth.day)
    unmei = calc_unmei(birth.year, birth.month, birth.day)
    shimei = calc_shimei(birth.month, birth.day)

    # 宿命分類（役割分担）
    if shukumei in [11]:
        role_number = 2
    elif shukumei in [22]:
        role_number = 4
    elif shukumei in [33]:
        role_number = 6
    else:
        role_number = shukumei

    group_map = {
        (1, 6, 9): "リーダー（宿命数1・6・9）",
        (2, 4, 7): "サポーター（宿命数2・4・7）",
        (3, 5, 8): "ムードメーカー（宿命数3・5・8）"
    }
    role = "不明"
    for keys, value in group_map.items():
        if role_number in keys:
            role = value
            break

    advice_map = {
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
        22: "特別な意味を持つ数字です。",
        33: "特別な意味を持つ数字です。"
    }

    st.subheader(f"🌟 {name}さんの結果 🌟")
    st.write(f"**星座：** {zodiac}")
    st.write(f"**宿命数：** {shukumei}（{role}）")
    st.write(f"**運命数：** {unmei}")
    st.write(f"**使命数：** {shimei}")
    st.write("---")
    st.write(f"🔍 あなたの役割：**{role}**")
    st.write(f"📄 宿命数からのひとこと：**{advice_map.get(shukumei, 'メッセージなし')}**")
