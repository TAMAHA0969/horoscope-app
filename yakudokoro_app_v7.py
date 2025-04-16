
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="TAMAHAの宿命と星座で見るあなたの役割", layout="centered")

st.title("🔮 TAMAHAの宿命と星座で見るあなたの役割 🔮")
st.markdown("生年月日を入力すると、あなたの【宿命数・星座・役割】がわかります。")

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
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "魚座"
    else:
        return "不明"

# 星座の特性
zodiac_traits = {
    "牡羊座": "冒険心とリーダーシップ",
    "牡牛座": "安定を愛する堅実家",
    "双子座": "知識を追求するコミュニケーター",
    "蟹座": "家庭を大切にする温かい心の持ち主",
    "獅子座": "輝きを放つ情熱的なリーダー",
    "乙女座": "完璧を求める細やかな分析者",
    "天秤座": "調和と美を追求するバランス感覚の持ち主",
    "蠍座": "深い洞察力を持つ神秘的な探求者",
    "射手座": "自由を愛する楽観的な冒険者",
    "山羊座": "責任感が強く実用的な現実主義者",
    "水瓶座": "革新を求める独立心旺盛な未来志向者",
    "魚座": "感受性豊かで共感力の高い夢想家"
}

# 宿命数（日のみ）
def calc_destiny_number(birthdate):
    total = birthdate.day
    while total not in [11, 22] and total > 9:
        total = sum(int(d) for d in str(total))
    return total

# 宿命数の特性
destiny_messages = {
    1: "先駆者として道を切り拓く力を持っています。",
    2: "人を支える縁の下の力持ちとして活躍します。",
    3: "自由な発想で場を明るくする表現者です。",
    4: "地道な努力で安定を築く実直な人です。",
    5: "変化を恐れず飛び込める冒険家です。",
    6: "思いやりに溢れた面倒見の良い人です。",
    7: "深い思索を重ねる内面重視タイプです。",
    8: "実行力があり成果を出す現実主義者です。",
    9: "大きな愛で人を包み込む存在です。",
    11: "直感力と癒しのエネルギーを持つ人です。",
    22: "壮大なビジョンを形にできる実現者です。"
}

# 役割分類（11→2、22→4）
def get_role_group(number):
    if number in [1, 6, 8]:
        return "リーダー・指導者グループ"
    elif number in [2, 4, 7, 11, 22]:
        return "サポーター・調整役グループ"
    elif number in [3, 5, 9]:
        return "ムードメーカー・表現者グループ"
    else:
        return "不明"

# 入力と表示
birth_date = st.date_input("🎂 生年月日を入力してください", value=datetime(2000, 1, 1),
    min_value=datetime(1900, 1, 1), max_value=datetime(2025, 12, 31))

if birth_date:
    zodiac = get_zodiac_sign(birth_date.month, birth_date.day)
    destiny = calc_destiny_number(birth_date)
    role_group = get_role_group(destiny)
    zodiac_trait = zodiac_traits.get(zodiac, "未知の魅力")
    destiny_trait = destiny_messages.get(destiny, "未知の特性")

    st.subheader("🪞 あなたの診断結果")
    st.markdown(f"**🌟 星座：** {zodiac}")
    st.markdown(f"**🔢 宿命数（日）：** {destiny}")
    st.markdown(f"**🧭 あなたの役割：** {role_group}")
    st.markdown("---")
    st.markdown("💬 **統合メッセージ**")
    st.markdown(
        f"あなたは「{zodiac_trait}（{zodiac}）」という外側の資質を持ち、
"
        f"内面では「{destiny_trait}」
"
        f"つまり、**“{role_group}”としての魂の役割**を担っています。"
    )
