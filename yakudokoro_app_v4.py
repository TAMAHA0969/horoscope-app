
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="宿命数 × 星座 アプリ", layout="centered")

st.title("🌟 宿命数（月＋日）× 星座で知るあなたの役割 🌟")
st.markdown("生年月日を入力すると、あなたの【宿命数・星座・役割】がわかります。")

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

# 宿命数（月＋日）の計算
def calc_destiny_number(birthdate):
    total = birthdate.month + birthdate.day
    while total not in [11, 22] and total > 9:
        total = sum(int(d) for d in str(total))
    return total

# 一言メッセージ
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

# 宿命数に基づく役割分類（11→2、22→4として分類）
def get_role_group(number):
    if number in [1, 6, 8]:
        return "リーダー・指導者グループ"
    elif number in [2, 4, 7, 11, 22]:
        return "サポーター・調整役グループ"
    elif number in [3, 5, 9]:
        return "ムードメーカー・表現者グループ"
    else:
        return "不明"

# 入力フォーム
birth_date = st.date_input("🎂 生年月日を入力してください", value=datetime(2000, 1, 1), min_value=datetime(1900, 1, 1), max_value=datetime(2025, 12, 31))

if birth_date:
    zodiac = get_zodiac_sign(birth_date.month, birth_date.day)
    destiny = calc_destiny_number(birth_date)
    role_group = get_role_group(destiny)

    st.subheader("🪞 あなたの診断結果")
    st.markdown(f"**🌟 星座：** {zodiac}")
    st.markdown(f"**🔢 宿命数（月＋日）：** {destiny}")
    st.markdown(f"**🧭 あなたの役割：** {role_group}")
    st.markdown("---")
    st.markdown(f"**💬 一言メッセージ：** {destiny_messages[destiny]}")
