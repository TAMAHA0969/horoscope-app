import streamlit as st
from datetime import datetime
import calendar

st.set_page_config(page_title="TAMAHAの星座と宿命数", page_icon="🔮")

def calc_life_path_number(year, month, day):
    total = sum(int(d) for d in f"{year}{month:02d}{day:02d}")
    while total > 9 and total not in [11, 22, 33]:
        total = sum(int(d) for d in str(total))
    return total

def calc_destiny_number(day):
    if day in [11, 22, 33]:
        return day
    while day > 9:
        day = sum(int(d) for d in str(day))
    return day

def calc_mission_number(month, day):
    total = month + day
    while total > 9 and total not in [11, 22, 33]:
        total = sum(int(d) for d in str(total))
    return total

def get_zodiac_sign(month, day):
    zodiac = [
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
        ((12, 22), (1, 19), "山羊座")
    ]
    for start, end, sign in zodiac:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign
    return "不明"

destiny_roles = {
    1: "リーダー（宿命数1）: 独立心と創造性、自己主張が強く新しい道を切り開く力。",
    2: "サポーター（宿命数2）: 協調性が高く、相手に寄り添う力が強み。",
    3: "ムードメーカー（宿命数3）: 楽しい雰囲気をつくる天才。明るく社交的。",
    4: "サポーター（宿命数4）: 地道な努力と安定を重んじる実直な支え手。",
    5: "ムードメーカー（宿命数5）: 行動力があり、新しい風を吹かせる改革者。",
    6: "リーダー（宿命数6）: 愛情深く面倒見が良い。調和を保つ統率者。",
    7: "サポーター（宿命数7）: 深い洞察力と冷静さで周囲を支える知恵者。",
    8: "ムードメーカー（宿命数8）: エネルギッシュに人を巻き込む影響力の持ち主。",
    9: "リーダー（宿命数9）: 理想を追求し、皆を導く慈愛ある哲学者。",
    11: "サポーター（宿命数11）: 直感と精神性の高さで支えるマスターナンバー。",
    22: "サポーター（宿命数22）: 世界を動かす力を秘めたマスタープランナー。",
    33: "リーダー（宿命数33）: 無償の愛で人々を導くカリスマ的存在。"
}

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
    11: "特別な意味を持つ数字。直感力を信じ、導かれるように行動しよう。",
    22: "世界を動かす可能性を秘めたマスタープランナー。ビジョンを信じて行動を。",
    33: "無償の愛で人を癒す力。与えることで自分も満たされていく。"
}

st.title("🔮 TAMAHAの星座と宿命数")

name = st.text_input("お名前（ニックネームでもOK）", "ゲスト")
birthdate = st.date_input("生年月日を選んでください", min_value=datetime(1900, 1, 1))

if st.button("診断スタート！"):
    year = birthdate.year
    month = birthdate.month
    day = birthdate.day

    zodiac = get_zodiac_sign(month, day)
    destiny = calc_destiny_number(day)
    life_path = calc_life_path_number(year, month, day)
    mission = calc_mission_number(month, day)

    role = destiny_roles.get(destiny, "不明")
    role_msg = destiny_messages.get(destiny, "あなたの魅力を活かして進みましょう！")

    st.subheader(f"✨ {name}さんの結果 ✨")
    st.markdown(f"**星座：** {zodiac}")
    st.markdown(f"**宿命数：** {destiny}（{role}）")
    st.markdown(f"**運命数：** {life_path}")
    st.markdown(f"**使命数：** {mission}")
    st.markdown(f"🔍 **あなたの役割：** {role}")
    st.markdown(f"📜 **宿命数からのひとこと：** {role_msg}")
