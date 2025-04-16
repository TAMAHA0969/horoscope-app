
import streamlit as st
from datetime import date
import math

# 星座を計算する関数
def get_zodiac_sign(month, day):
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
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign
    return "不明"

# 宿命数、運命数、使命数を計算
def calc_numerology(birthdate):
    year, month, day = birthdate.year, birthdate.month, birthdate.day
    # 運命数：すべての数字を合計
    destiny = sum(int(d) for d in f"{year}{month:02}{day:02}")
    while destiny > 9 and destiny not in [11, 22, 33]:
        destiny = sum(int(d) for d in str(destiny))

    # 宿命数：日
    soul = day
    while soul > 9 and soul not in [11, 22, 33]:
        soul = sum(int(d) for d in str(soul))

    # 使命数：月と日
    mission = sum(int(d) for d in f"{month:02}{day:02}")
    while mission > 9 and mission not in [11, 22, 33]:
        mission = sum(int(d) for d in str(mission))

    return destiny, soul, mission

# 宿命数ごとのグループ
def get_group(soul):
    group_1 = [1, 6, 9]
    group_2 = [2, 4, 7]
    group_3 = [3, 5, 8]
    if soul in group_1:
        return "リーダー・指導者グループ", "組織を引っ張るリーダー。責任感が強く、指導力や統率力を持つ。世話好きで、人の面倒を見ることが得意なタイプ。"
    elif soul in group_2:
        return "サポーター・調整役グループ", "組織の調和を保ち、冷静な判断力でサポートする縁の下の力持ち。計画を緻密に立て、組織が円滑に回るよう尽力します。"
    elif soul in group_3:
        return "ムードメーカー・営業グループ", "活発でエネルギッシュ、人を楽しませる能力が高い。人と人をつなげるコミュニケーション力、営業力があり、社交的で行動派。"
    else:
        return "不明", "不明"

# 宿命数ごとの一言アドバイス
def get_soul_message(soul):
    messages = {
        1: "自分を信じて突き進め！先駆者の道はあなたが切り拓く。",
        2: "支える力が強み。無理に前に出なくても、陰の力が光る！",
        3: "自由と楽しさが鍵。型にはまらず、自分の感性を信じよう。",
        4: "地道な努力が実を結ぶ。焦らず、一歩ずつ確実に前進を！",
        5: "変化を恐れず、新しい世界へ飛び込もう！柔軟さが武器。",
        6: "人を支えるのは素晴らしい。でも、自分を大事にすることも忘れずに！",
        7: "一人の時間があなたを成長させる。内なる声に耳を傾けて。",
        8: "成功をつかむ力あり！自信を持って堂々とリーダーシップを発揮しよう。",
        9: "すべてを受け入れる大きな愛を持つ人。手放すことで新たな道が開く！",
    }
    return messages.get(soul, "特別な意味を持つ数字です。")

# Streamlit UI
st.title("🔮 TAMAHAの星座と宿命数")
name = st.text_input("お名前（ニックネームでもOK）")
birthdate = st.date_input("生年月日を選んでください", min_value=date(1900, 1, 1))

if st.button("診断スタート！"):
    zodiac = get_zodiac_sign(birthdate.month, birthdate.day)
    destiny, soul, mission = calc_numerology(birthdate)
    group, role = get_group(soul)
    message = get_soul_message(soul)

    st.subheader(f"🌟 {name}さんの結果 🌟")
    st.markdown(f"**星座：** {zodiac}")
    st.markdown(f"**宿命数：** {soul}（{group}）")
    st.markdown(f"**運命数：** {destiny}")
    st.markdown(f"**使命数：** {mission}")
    st.divider()
    st.markdown(f"**🔎 あなたの役割：** {role}")
    st.markdown(f"**📝 宿命数からのひとこと：** _{message}_")
