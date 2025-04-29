import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

actions = [
    (0, 0),    # HVAC off
    (1, 21),   # Low fan, setpoint 21°C
    (2, 23),   # High fan, setpoint 23°C
    (1, 24),   # Low fan, setpoint 24°C
]
st.title("HVAC Control System")
current_temperature = st.slider("Enter Current Temperature (°C)", min_value=15, max_value=30, value=22)

if current_temperature < 21:
    action = 3 
elif 21 <= current_temperature <= 22:
    action = 0 
elif 22 < current_temperature <= 23:
    action = 2 
else:
    action = 1 
action_label = actions[action]
st.write(f"Recommended HVAC action: {action_label[0]} (Fan Speed: {'High' if action_label[0] == 2 else 'Low' if action_label[0] == 1 else 'Off'}), Setpoint: {action_label[1]}°C")

st.subheader("Current Temperature and Recommended Action")
fig, ax = plt.subplots(figsize=(5, 3))
ax.barh([f"Action {action_label[0]}"], [action_label[1]], color='skyblue')
ax.set_xlabel("Setpoint Temperature (°C)")
ax.set_title("Recommended HVAC Action Based on Current Temperature")
st.pyplot(fig)
