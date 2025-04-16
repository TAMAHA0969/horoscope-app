
import streamlit as st
import datetime

st.set_page_config(page_title="TAMAHAの星座と宿命数", layout="centered")

st.title("🔮 TAMAHAの星座と宿命数")
name = st.text_input("お名前（ニックネームでもOK）", value="ゲスト")
birth_date = st.date_input("生年月日を選んでください", value=datetime.date(2000, 1, 1), min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today())

if st.button("診断スタート！"):
    st.subheader(f"🌟 {name}さんの結果 🌟")

    # 星座判定
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
        else:
            return "魚座"

    zodiac = get_zodiac_sign(birth_date.month, birth_date.day)
    st.markdown(f"**星座：** {zodiac}")

    # 宿命数
    day = birth_date.day
    destiny_number = day

    role_dict = {
        (1, 10, 19, 28): (1, "リーダー"),
        (6, 15, 24): (6, "リーダー"),
        (9, 18, 27): (9, "リーダー"),
        (2, 11, 20, 29): (2, "サポーター"),
        (4, 13, 22, 31): (4, "サポーター"),
        (7, 16, 25): (7, "サポーター"),
        (3, 12, 21, 30): (3, "ムードメーカー"),
        (5, 14, 23): (5, "ムードメーカー"),
        (8, 17, 26): (8, "ムードメーカー"),
    }

    shukumei = "不明"
    role = "不明"
    for k, v in role_dict.items():
        if day in k:
            shukumei, role = v
            break

    st.markdown(f"**宿命数：** {day}（{role}）")

    # 特徴説明
    role_traits = {
        "リーダー": {
            1: "独立心と創造性、目標達成、自信と自己主張。",
            6: "調和と責任、愛と奉仕、協調性と共感。",
            9: "人道主義と慈悲、理想主義、寛容性と理解。"
        },
        "サポーター": {
            2: "優しく繊細で、人の心を読む力がある平和主義者。",
            4: "地道で堅実な働き者。信頼される縁の下の力持ち。",
            7: "冷静で知的。専門分野を極める隠れた実力者。"
        },
        "ムードメーカー": {
            3: "明るく社交的で、場を楽しく盛り上げる才能あり。",
            5: "自由を愛する行動派。変化にも柔軟に対応できる。",
            8: "自信家で現実的。目標達成能力の高い実行者。"
        }
    }

    if shukumei in role_traits.get(role, {}):
        st.markdown(f"🔍 **あなたの役割：{role}（宿命数{shukumei}）**

🧭 特徴：{role_traits[role][shukumei]}")

    # 宿命数からのひとこと
    special_msg = {
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
        22: "世界を動かす可能性を秘めたマスタープランナー。ビジョンを信じて行動を。",
        33: "愛と癒しのカリスマ。人を導く天性のヒーラー。"
    }

    if destiny_number in special_msg:
        st.markdown(f"📜 **宿命数からのひとこと：** {special_msg[destiny_number]}")
