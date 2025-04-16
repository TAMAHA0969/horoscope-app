
import streamlit as st
from datetime import datetime
import calendar

st.set_page_config(page_title="TAMAHAの星座と宿命数", page_icon="🔮")

st.title("🔮 TAMAHAの星座と宿命数")

name = st.text_input("お名前（ニックネームでもOK）", "ゲスト")
birthdate = st.date_input("生年月日を選んでください", value=datetime(2000, 1, 1),
                          min_value=datetime(1900, 1, 1), max_value=datetime.today())

def calculate_life_path_number(birthdate):
    digits = [int(d) for d in birthdate.strftime("%Y%m%d")]
    total = sum(digits)
    while total not in [11, 22, 33] and total > 9:
        total = sum(int(d) for d in str(total))
    return total

def calculate_destiny_number(birthdate):
    return calculate_life_path_number(birthdate)

def calculate_mission_number(birthdate):
    digits = [int(d) for d in f"{birthdate.month:02d}{birthdate.day:02d}"]
    total = sum(digits)
    while total not in [11, 22, 33] and total > 9:
        total = sum(int(d) for d in str(total))
    return total

def calculate_zodiac_sign(birthdate):
    month = birthdate.month
    day = birthdate.day
    zodiac_dates = [
        ((1, 20), (2, 18), "水瓶座"),
        ((2, 19), (3, 20), "魚座"),
        ((3, 21), (4, 19), "牡羊座"),
        ((4, 20), (5, 20), "牡牛座"),
        ((5, 21), (6, 21), "双子座"),
        ((6, 22), (7, 22), "蟹座"),
        ((7, 23), (8, 22), "獅子座"),
        ((8, 23), (9, 22), "乙女座"),
        ((9, 23), (10, 23), "天秤座"),
        ((10, 24), (11, 22), "蠍座"),
        ((11, 23), (12, 21), "射手座"),
        ((12, 22), (1, 19), "山羊座"),
    ]
    for start, end, sign in zodiac_dates:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign
    return "不明"

def get_role_and_message(shukumei):
    group_roles = {
        1: ("リーダー", "1は創造性と自立の象徴。目標達成力が高く、自信に満ちたリーダーです。"),
        6: ("リーダー", "6は愛と責任のリーダー。調和を重視し、周囲の幸せを願う存在です。"),
        9: ("リーダー", "9は理想と慈愛を持つリーダー。社会貢献と高いビジョンを大切にします。"),
        2: ("サポーター", "2は繊細で協調性あるサポーター。調和を保ち、支える力に優れます。"),
        4: ("サポーター", "4は安定と誠実の象徴。地道な努力で組織を支える信頼の存在。"),
        7: ("サポーター", "7は洞察力に優れたサポーター。内面の探究と分析力で支えます。"),
        3: ("ムードメーカー", "3は明るく自由なムードメーカー。表現力があり、人を楽しませる力が抜群。"),
        5: ("ムードメーカー", "5は好奇心と行動力が特徴。変化を恐れず前進するパワーがあります。"),
        8: ("ムードメーカー", "8はカリスマ性とパワーで周囲を惹きつけるムードメーカー。"),
        11: ("サポーター", "11は直感と霊性を持つマスターナンバー。繊細で高次のビジョンを伝える存在。"),
        22: ("サポーター", "22は現実化の力を持つマスターナンバー。組織的な力で夢を現実にします。"),
        33: ("リーダー", "33は無償の愛のマスターナンバー。大いなる奉仕と包容力を持ちます。"),
    }
    role, message = group_roles.get(shukumei, ("不明", ""))
    return role, message

if st.button("診断スタート！"):
    zodiac_sign = calculate_zodiac_sign(birthdate)
    shukumei = birthdate.day
    destiny = calculate_destiny_number(birthdate)
    mission = calculate_mission_number(birthdate)
    role, role_msg = get_role_and_message(shukumei)

    st.subheader(f"✨ {name}さんの結果 ✨")
    st.markdown(f"**星座：** {zodiac_sign}")
    st.markdown(f"**宿命数：** {shukumei}（{role}）")
    st.markdown(f"**運命数：** {destiny}")
    st.markdown(f"**使命数：** {mission}")
    st.markdown(f"🔍 **あなたの役割：{role}（宿命数{shukumei}）**")

📘 **宿命数からのひとこと：** {role_msg}")
