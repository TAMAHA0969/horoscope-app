
import streamlit as st
import datetime
import calendar

st.set_page_config(page_title="TAMAHAの星座と宿命数", layout="centered")

st.title("🔮 TAMAHAの星座と宿命数")
name = st.text_input("お名前（ニックネームでもOK）", "ゲスト")
birth_date = st.date_input("生年月日を選んでください", value=datetime.date(2000, 1, 1),
                           min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today())

submit = st.button("診断スタート！")

if submit:
    def calc_life_path_number(date):
        total = sum(int(d) for d in date.strftime("%Y%m%d"))
        while total > 9 and total not in [11, 22, 33]:
            total = sum(int(d) for d in str(total))
        return total

    def calc_destiny_number(date):
        total = date.day
        if total not in [11, 22, 33]:
            total = sum(int(d) for d in str(total))
        return total

    def calc_mission_number(date):
        total = date.month + date.day
        if total not in [11, 22, 33]:
            total = sum(int(d) for d in str(total))
        return total

    def get_zodiac_sign(date):
        month, day = date.month, date.day
        signs = [
            (120, "山羊座"), (219, "水瓶座"), (321, "魚座"), (420, "牡羊座"),
            (521, "牡牛座"), (621, "双子座"), (722, "蟹座"), (823, "獅子座"),
            (923, "乙女座"), (1023, "天秤座"), (1122, "蠍座"), (1222, "射手座"), (1231, "山羊座")
        ]
        mmdd = month * 100 + day
        for cutoff, sign in signs:
            if mmdd <= cutoff:
                return sign
        return "山羊座"

    def get_role(number):
        if number in [1, 6, 9, 11, 22, 33]:
            return "リーダー"
        elif number in [2, 4, 7]:
            return "サポーター"
        elif number in [3, 5, 8]:
            return "ムードメーカー"
        else:
            return "不明"

    def get_role_description(number):
        descriptions = {
            1: "独立心が強く、自信にあふれる創造的なリーダー。目標達成に向けた推進力があります。",
            6: "調和と責任感を大切にし、仲間を支える温かいリーダーです。",
            9: "理想を掲げ、寛容な心で人々を導くヒューマニティリーダー。",
            2: "縁の下の力持ち。調和を保ち、冷静に物事を進めることが得意です。",
            4: "安定と実直さ。地道な努力で組織をしっかり支えます。",
            7: "内面の探究を重視し、直感と洞察力でサポートする役割です。",
            3: "陽気で創造的。場の雰囲気を明るくし、自然と人を惹きつけます。",
            5: "自由と変化を好み、情報通で柔軟なコミュニケーター。",
            8: "行動力と実行力に優れたリーダーシップ型ムードメーカー。",
            11: "高い精神性とインスピレーションを持つビジョナリー。人を導く直感の使い手。",
            22: "世界を動かす可能性を秘めたマスタープランナー。ビジョンを信じて行動を。",
            33: "深い愛と奉仕精神で人々を癒すマスターヒーラー。人類全体への貢献を目指します。"
        }
        return descriptions.get(number, "役割情報が見つかりませんでした。")

    def get_destiny_message(number):
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
            11: "インスピレーションで道を切り拓く特別な導き手。",
            22: "大きな夢を現実に変える力。社会的成功のポテンシャル大。",
            33: "無償の愛と癒しで人々を包みこむ。高次の奉仕者。"
        }
        return messages.get(number, "特別な意味を持つ数字です。")

    zodiac = get_zodiac_sign(birth_date)
    destiny = calc_destiny_number(birth_date)
    life_path = calc_life_path_number(birth_date)
    mission = calc_mission_number(birth_date)
    role = get_role(destiny)
    role_desc = get_role_description(destiny)
    destiny_msg = get_destiny_message(destiny)

    st.subheader(f"✨ {name}さんの結果 ✨")
    st.markdown(f"**星座：** {zodiac}")
    st.markdown(f"**宿命数：** {destiny}（{role}）")
    st.markdown(f"**運命数：** {life_path}")
    st.markdown(f"**使命数：** {mission}")
    st.markdown(f"🔍 **あなたの役割：** {role}（宿命数{destiny}） – {role_desc}")
    st.markdown(f"📄 **宿命数からのひとこと：** {destiny_msg}")
