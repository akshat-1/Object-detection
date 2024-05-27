import streamlit as st
from detector import begin_capture

st.title("MONITOR YOUR FOOTAGES")
frame_ph = st.empty()

stop_btn = st.button("STOP")

begin_capture(stop_btn, frame_ph).begin()




