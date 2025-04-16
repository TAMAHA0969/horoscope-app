
import streamlit as st
from datetime import datetime

def reduce_number(n):
    while n not in [11, 22] and n >= 10:
        n = sum([int(d) for d in str(n)])
    return n

def calculate_numbers(year, month, day):
    total_digits = [int(d) for d in str(year) + str(month).zfill(2) + str(day).zfill(2)]
    life_path = reduce_number(sum(total_digits))
    destiny = reduce_number(sum([int(d) for d in str(day)]))
    mission = reduce_number(sum([int(d) for d in str(month).zfill(2) + str(day).zfill(2)]))
    return life_path, destiny, mission

st.set_page_config(page_title="TAMAHA数秘術 自動計算", page_icon="🔢")
st.title("🔢 運命数・宿命数・使命数 自動計算")

birthdate = st.date_input(
    "あなたの生年月日を選んでください",
    value=datetime(1990, 1, 1),
    min_value=datetime(1900, 1, 1),
    max_value=datetime.today()
)

if st.button("計算する"):
    year, month, day = birthdate.year, birthdate.month, birthdate.day
    life, destiny, mission = calculate_numbers(year, month, day)

    st.subheader("📘 計算結果")
    st.markdown(f"**運命数（ライフパス）**： {life}")
    st.markdown(f"**宿命数（日）**： {destiny}")
    st.markdown(f"**使命数（月＋日）**： {mission}")
