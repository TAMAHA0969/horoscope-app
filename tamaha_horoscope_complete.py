
import streamlit as st
from datetime import datetime, date

# 宿命数の分類
role_groups = {
    "リーダー": [1, 6, 9],
    "サポーター": [2, 4, 7],
    "ムードメーカー": [3, 5, 8]
}

# 宿命数に対応する一言
shukumei_messages = {
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
    22: "世界を動かす可能性を秘めたマスタープランナー。ビジョンを信じて行動を。",
    33: "愛と奉仕のカリスマ。みんなの幸せのために大きな力を発揮するマスターナンバー。"
}

# 星座判定
def get_zodiac_sign(month, day):
    signs = [
        ((1, 20), "山羊座"), ((2, 19), "水瓶座"), ((3, 21), "魚座"), ((4, 20), "牡羊座"),
        ((5, 21), "牡牛座"), ((6, 22), "双子座"), ((7, 23), "蟹座"), ((8, 23), "獅子座"),
        ((9, 23), "乙女座"), ((10, 24), "天秤座"), ((11, 23), "蠍座"), ((12, 22), "射手座"),
        ((12, 32), "山羊座")  # Year-end catch
    ]
    for (m, d), sign in signs:
        if (month, day) < (m, d):
            return prev
        prev = sign
    return "山羊座"

# 数秘の計算
def calc_numerology(value):
    while value > 9 and value not in [11, 22, 33]:
        value = sum(int(d) for d in str(value))
    return value

st.title("🔮 TAMAHAの星座と宿命数")

name = st.text_input("お名前（ニックネームでもOK）", "ゲスト")
birth_date = st.date_input("生年月日を選んでください", value=date(2000, 1, 1), min_value=date(1900, 1, 1))

if st.button("診断スタート！"):
    month, day = birth_date.month, birth_date.day
    zodiac = get_zodiac_sign(month, day)

    # 数秘の計算
    destiny = calc_numerology(birth_date.year + birth_date.month + birth_date.day)
    mission = calc_numerology(birth_date.month + birth_date.day)
    fate = calc_numerology(birth_date.day)

    # 宿命数を役割分類（11→2, 22→4, 33→6）
    role_number = {11: 2, 22: 4, 33: 6}.get(fate, fate)
    role = next((k for k, v in role_groups.items() if role_number in v), "不明")
    fate_msg = shukumei_messages.get(fate, "特別な意味を持つ数字です。")

    st.subheader(f"🌟 {name}さんの結果 🌟")
    st.write(f"星座：**{zodiac}**")
    st.write(f"宿命数：**{fate}（{role}）**")
    st.write(f"運命数：**{destiny}**")
    st.write(f"使命数：**{mission}**")

    st.write(f"🔍 あなたの役割：**{role}**（宿命数{', '.join(map(str, role_groups[role]))}）")
    st.write(f"📝 宿命数からのひとこと：{fate_msg}")
