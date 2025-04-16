
import streamlit as st

def reduce_number(n):
    while n not in [11, 22] and n >= 10:
        n = sum([int(d) for d in str(n)])
    return n

def calculate_numbers(year, month, day):
    # 運命数
    total_digits = [int(d) for d in str(year) + str(month).zfill(2) + str(day).zfill(2)]
    life_path = reduce_number(sum(total_digits))

    # 宿命数（日）
    destiny = reduce_number(sum([int(d) for d in str(day)]))

    # 使命数（月＋日）
    mission = reduce_number(sum([int(d) for d in str(month).zfill(2) + str(day).zfill(2)]))

    return life_path, destiny, mission

st.set_page_config(page_title="TAMAHA数秘術診断", page_icon="🔢")
st.title("🔢 数秘術診断：運命・宿命・使命数")

birthdate = st.date_input("あなたの生年月日を選んでください")

if st.button("診断する"):
    year, month, day = birthdate.year, birthdate.month, birthdate.day
    life, destiny, mission = calculate_numbers(year, month, day)

    st.subheader("🔮 結果")
    st.markdown(f"**運命数（ライフパス）**： {life}")
    st.markdown(f"**宿命数（日）**： {destiny}")
    st.markdown(f"**使命数（月＋日）**： {mission}")
