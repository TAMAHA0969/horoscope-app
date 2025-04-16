
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="星座 × 宿命数 アプリ", layout="centered")

st.title("🌸 星座 × 宿命数 アプリ - 2025年春 🌸")
st.markdown("生年月日を入力すると、あなたの星座・宿命数・役割がわかります！")

# 星座判定関数
def get_zodiac_sign(month, day):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "牡羊座"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "牡牛座"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return "双子座"
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return "蟹座"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "獅子座"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "乙女座"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 23):
        return "天秤座"
    elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
        return "蠍座"
    elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
        return "射手座"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "山羊座"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "水瓶座"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "魚座"
    else:
        return "不明"

# 宿命数計算関数
def calc_destiny_number(birthdate):
    total = sum(int(d) for d in birthdate.strftime("%Y%m%d"))
    while total not in [11, 22] and total > 9:
        total = sum(int(d) for d in str(total))
    return total

# 宿命数ごとの一言アドバイス
destiny_messages = {
    1: "自分を信じて突き進め！先駆者の道はあなたが切り拓く。",
    2: "支える力が強み。無理に前に出なくても、陰の力が光る！",
    3: "自由と楽しさが鍵。型にはまらず、自分の感性を信じよう。",
    4: "地道な努力が実を結ぶ。焦らず、一歩ずつ確実に前進を！",
    5: "変化を恐れず、新しい世界へ飛び込もう！柔軟さが武器。",
    6: "人を支えるのは素晴らしい。でも、自分を大事にすることも忘れずに！",
    7: "一人の時間があなたを成長させる。内なる声に耳を傾けて。",
    8: "成功をつかむ力あり！自信を持って堂々とリーダーシップを発揮しよう。",
    9: "すべてを受け入れる大きな愛を持つ人。手放すことで新たな道が開く！",
    11: "直感とスピリチュアルな感性が導く道。人を癒す力があるマスターナンバー。",
    22: "世界を動かす可能性を秘めたマスタープランナー。ビジョンを信じて行動を。"
}

# 役割グループ
supporter_group = [2, 4, 7, 11, 22]

# 入力フォーム
birth_date = st.date_input("🎂 生年月日を入力してください", value=datetime(1990, 1, 1))

if birth_date:
    sign = get_zodiac_sign(birth_date.month, birth_date.day)
    destiny = calc_destiny_number(birth_date)

    st.subheader("🔮 結果")
    st.markdown(f"**あなたの星座：** {sign}")
    st.markdown(f"**あなたの宿命数：** {destiny}")
    st.markdown(f"**宿命数からのメッセージ：** {destiny_messages[destiny]}")

    if destiny in supporter_group:
        st.markdown("**あなたの役割：サポーター（宿命数2・4・7・11・22）**")
        st.info("""
あなたは、他者を支え、調和をもたらす力を持っています。  
目立つことよりも、縁の下の力持ちとしてチームや組織を支えることに喜びを感じるタイプ。  
繊細な感受性と直感力を活かし、人々の心に寄り添い、安心感を提供する存在です。
        """)

