
import streamlit as st
from datetime import datetime
import calendar

st.set_page_config(page_title="TAMAHA", page_icon="")

st.title(" TAMAHA")

name = st.text_input("OK", "")
birthdate = st.date_input("", value=datetime(2000, 1, 1),
                          min_value=datetime(1900, 1, 1), max_value=datetime.today())

def calculate_life_path_number(birthdate):
    digits = [int(d) for d in birthdate.strftime("%Y%m%d")]
    total = sum(digits)
    while total not in [11, 22, 33] and total > 9:
        total = sum(int(d) for d in str(total))
    return total

def calculate_destiny_number(birthdate):
    return calculate_life_path_number(birthdate)

def calculate_mission_number(birthdate):
    digits = [int(d) for d in f"{birthdate.month:02d}{birthdate.day:02d}"]
    total = sum(digits)
    while total not in [11, 22, 33] and total > 9:
        total = sum(int(d) for d in str(total))
    return total

def calculate_zodiac_sign(birthdate):
    month = birthdate.month
    day = birthdate.day
    zodiac_dates = [
        ((1, 20), (2, 18), ""),
        ((2, 19), (3, 20), ""),
        ((3, 21), (4, 19), ""),
        ((4, 20), (5, 20), ""),
        ((5, 21), (6, 21), ""),
        ((6, 22), (7, 22), ""),
        ((7, 23), (8, 22), ""),
        ((8, 23), (9, 22), ""),
        ((9, 23), (10, 23), ""),
        ((10, 24), (11, 22), ""),
        ((11, 23), (12, 21), ""),
        ((12, 22), (1, 19), ""),
    ]
    for start, end, sign in zodiac_dates:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign
    return ""

def get_role_and_message(shukumei):
    group_roles = {
        1: ("", "1"),
        6: ("", "6"),
        9: ("", "9"),
        2: ("", "2"),
        4: ("", "4"),
        7: ("", "7"),
        3: ("", "3"),
        5: ("", "5"),
        8: ("", "8"),
        11: ("", "11"),
        22: ("", "22"),
        33: ("", "33"),
    }
    role, message = group_roles.get(shukumei, ("", ""))
    return role, message

if st.button(""):
    zodiac_sign = calculate_zodiac_sign(birthdate)
    shukumei = birthdate.day
    destiny = calculate_destiny_number(birthdate)
    mission = calculate_mission_number(birthdate)
    role, role_msg = get_role_and_message(shukumei)

    st.subheader(f" {name} ")
    st.markdown(f"**** {zodiac_sign}")
    st.markdown(f"**** {shukumei}{role}")
    st.markdown(f"**** {destiny}")
    st.markdown(f"**** {mission}")
    st.markdown(f" **{role}{shukumei}**")

 **** {role_msg}")
