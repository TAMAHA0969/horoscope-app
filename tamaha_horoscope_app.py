
import streamlit as st
from datetime import datetime
import swisseph as swe

signs = ['牡羊座', '牡牛座', '双子座', '蟹座', '獅子座', '乙女座',
         '天秤座', '蠍座', '射手座', '山羊座', '水瓶座', '魚座']

st.set_page_config(page_title="Tamaha ホロスコープ診断", page_icon="🔮")
st.title("🔮 あなたのホロスコープ診断")
st.caption("by tamaha-okrock.com")

name = st.text_input("お名前（ニックネームでもOK）")
birth_date = st.date_input("生年月日", value=datetime(1990, 1, 1))
birth_time = st.time_input("出生時間", value=datetime.strptime("12:00", "%H:%M").time())
lat = st.number_input("出生地の緯度（例：大阪→34.6937）", value=34.6937)
lon = st.number_input("出生地の経度（例：大阪→135.5023）", value=135.5023)

if st.button("ホロスコープを生成！"):
    utc_offset = 9
    jd = swe.julday(birth_date.year, birth_date.month, birth_date.day,
                    birth_time.hour + birth_time.minute / 60 - utc_offset)

    house_cusps, ascmc = swe.houses(jd, lat, lon, b'P')

    planets = {
        '太陽': swe.SUN, '月': swe.MOON, '水星': swe.MERCURY, '金星': swe.VENUS, '火星': swe.MARS,
        '木星': swe.JUPITER, '土星': swe.SATURN, '天王星': swe.URANUS, '海王星': swe.NEPTUNE, '冥王星': swe.PLUTO
    }

    def get_house(pos):
        for i in range(12):
            start = house_cusps[i]
            end = house_cusps[i + 1] if i < 11 else house_cusps[0] + 360
            if start <= pos < end or (i == 11 and pos >= house_cusps[11]):
                return i + 1
        return 12

    st.subheader(f"🌟 {name}さんのホロスコープ結果")
    for pname, pid in planets.items():
        lon_deg = swe.calc_ut(jd, pid)[0][0]
        sign = signs[int(lon_deg // 30)]
        house = get_house(lon_deg)
        st.markdown(f"**【{pname}】**：{house}ハウス　{sign}（{lon_deg:.2f}°）")

    st.success("診断完了！星たちからのメッセージをどうぞ🌌")
