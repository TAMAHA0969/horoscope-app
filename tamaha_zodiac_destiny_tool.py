
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="TAMAHAの星座と宿命数", layout="centered")

def get_zodiac_sign(month: int, day: int) -> str:
    zodiac_signs = [
        ("山羊座", (12, 22), (1, 19)),
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
    ]
    for sign, start, end in zodiac_signs:
        start_month, start_day = start
        end_month, end_day = end
        if ((month == start_month and day >= start_day) or 
            (month == end_month and day <= end_day)):
            return sign
    return "不明"

def calc_life_path_number(y, m, d):
    return reduce_to_single_digit(y + m + d)

def calc_mission_number(m, d):
    return reduce_to_single_digit(m + d)

def calc_destiny_number(d):
    return reduce_to_single_digit(d)

def reduce_to_single_digit(n):
    while n > 9 and n not in [11, 22, 33]:
        n = sum(map(int, str(n)))
    return n

def get_group(number):
    if number in [1, 6, 9]:
        return "リーダー（宿命数1・6・9）"
    elif number in [2, 4, 7]:
        return "サポーター（宿命数2・4・7）"
    elif number in [3, 5, 8]:
        return "ムードメーカー（宿命数3・5・8）"
    else:
        return "不明"

def get_role_text(group):
    if group.startswith("リーダー"):
        return "責任感が強く、指導力や統率力を持つリーダータイプ。"
    elif group.startswith("サポーター"):
        return "冷静な判断で支える縁の下の力持ち。"
    elif group.startswith("ムードメーカー"):
        return "活発で社交的、人を楽しませるムードメーカー。"
    return ""

def get_advice_text(destiny):
    advice = {
        1: "自分を信じて突き進め！先駆者の道はあなたが切り拓く。",
        2: "支える力が強み。無理に前に出なくても、陰の力が光る！",
        3: "自由と楽しさが鍵。型にはまらず、自分の感性を信じよう。",
        4: "地道な努力が実を結ぶ。焦らず、一歩ずつ確実に前進を！",
        5: "変化を恐れず、新しい世界へ飛び込もう！柔軟さが武器。",
        6: "人を支えるのは素晴らしい。でも、自分を大事にすることも忘れずに！",
        7: "一人の時間があなたを成長させる。内なる声に耳を傾けて。",
        8: "成功をつかむ力あり！自信を持って堂々とリーダーシップを発揮しよう。",
        9: "すべてを受け入れる大きな愛を持つ人。手放すことで新たな道が開く！",
        11: "世界を変える可能性を秘めたマスターナンバー。ビジョンを信じて行動を。",
        22: "世界を動かすマスタープランナー。大きな夢を着実に形にしていこう。",
        33: "愛と奉仕の象徴。みんなの幸せを願い、光を広げる存在。"
    }
    return advice.get(destiny, "特別な意味を持つ数字です。")

st.title("🔮 TAMAHAの星座と宿命数")

name = st.text_input("お名前（ニックネームでもOK）", "")
birth = st.date_input("生年月日を選んでください", min_value=datetime(1900, 1, 1))

if st.button("診断スタート！"):
    year, month, day = birth.year, birth.month, birth.day
    zodiac = get_zodiac_sign(month, day)
    destiny_raw = day
    destiny = reduce_to_single_digit(destiny_raw)
    # 特別数値の扱い
    group = get_group(destiny if destiny not in [11, 22, 33] else {11:2, 22:4, 33:6}[destiny])
    role = get_role_text(group)
    life_path = calc_life_path_number(year, month, day)
    mission = calc_mission_number(month, day)
    
    st.subheader(f"🌟 {name}さんの結果 🌟")
    st.write(f"**星座：** {zodiac}")
    st.write(f"**宿命数：** {destiny_raw}（{group}）")
    st.write(f"**運命数：** {life_path}")
    st.write(f"**使命数：** {mission}")
    st.markdown(f"🔍 **あなたの役割：** {group} — {role}")
    st.markdown(f"📜 **宿命数からのひとこと：** {get_advice_text(destiny_raw)}")
