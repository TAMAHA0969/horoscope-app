
# tamaha_horoscope_TAMAHA_clean.py

import streamlit as st
from datetime import date
import calendar

st.set_page_config(page_title="TAMAHAの星座と宿命数", layout="centered")

st.title("🔮 TAMAHAの星座と宿命数")

# 入力フォーム
with st.form("birth_form"):
    name = st.text_input("お名前（ニックネームでもOK）")
    birth_date = st.date_input("生年月日を選んでください", value=date(2000, 1, 1), min_value=date(1900, 1, 1), max_value=date.today())
    submitted = st.form_submit_button("診断スタート！")

# 星座を計算する関数
def get_zodiac(month, day):
    zodiacs = [
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
    for sign, start, end in zodiacs:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign
    return "不明"

# 宿命数を計算する関数（日だけで出す）
def calc_destiny_number(day):
    return reduce_to_single_digit(day)

# 運命数を計算する関数（年月日すべての合計）
def calc_fate_number(y, m, d):
    total = sum(map(int, str(y) + str(m).zfill(2) + str(d).zfill(2)))
    return reduce_to_single_digit(total)

# 使命数を計算する関数（月と日）
def calc_mission_number(m, d):
    total = sum(map(int, str(m).zfill(2) + str(d).zfill(2)))
    return reduce_to_single_digit(total)

# 一桁にする処理（11, 22, 33はマスターナンバーとしてそのまま）
def reduce_to_single_digit(n):
    while n > 9 and n not in (11, 22, 33):
        n = sum(map(int, str(n)))
    return n

# グループ分けの辞書
group_roles = {
    (1, 10, 19, 28): "リーダー（宿命数1）",
    (6, 15, 24): "リーダー（宿命数6）",
    (9, 18, 27): "リーダー（宿命数9）",
    (2, 11, 20, 29): "サポーター（宿命数2）",
    (4, 13, 22, 31): "サポーター（宿命数4）",
    (7, 16, 25): "サポーター（宿命数7）",
    (3, 12, 21, 30): "ムードメーカー（宿命数3）",
    (5, 14, 23): "ムードメーカー（宿命数5）",
    (8, 17, 26): "ムードメーカー（宿命数8）"
}

# アドバイス辞書
advice_dict = {
    1: "自分を信じて突き進め！先駆者の道はあなたが切り拓く。",
    2: "支える力が強み。無理に前に出なくても、陰の力が光る！",
    3: "自由と楽しさが鍵。型にはまらず、自分の感性を信じよう。",
    4: "地道な努力が実を結ぶ。焦らず、一歩ずつ確実に前進を！",
    5: "変化を恐れず、新しい世界へ飛び込もう！柔軟さが武器。",
    6: "人を支えるのは素晴らしい。でも、自分を大事にすることも忘れずに！",
    7: "一人の時間があなたを成長させる。内なる声に耳を傾けて。",
    8: "成功をつかむ力あり！自信を持って堂々とリーダーシップを発揮しよう。",
    9: "すべてを受け入れる大きな愛を持つ人。手放すことで新たな道が開く！"
}

# 表示ロジック
if submitted:
    year, month, day = birth_date.year, birth_date.month, birth_date.day
    zodiac = get_zodiac(month, day)
    fate = calc_fate_number(year, month, day)
    destiny = calc_destiny_number(day)
    mission = calc_mission_number(month, day)

    role = ""
    for key, value in group_roles.items():
        if day in key:
            role = value

    st.subheader(f"🌟 {name}さんの結果 🌟")
    st.markdown(f"**星座：** {zodiac}")
    st.markdown(f"**宿命数：** {destiny}（{role}）")
    st.markdown(f"**運命数：** {fate}")
    st.markdown(f"**使命数：** {mission}")
    st.markdown("---")
    st.markdown(f"📝 宿命数からの一言：**{advice_dict[destiny]}**")
