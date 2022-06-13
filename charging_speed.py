from matplotlib.pyplot import title
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

st.subheader(
    "Charging Rates / Power Level : Google Pixel 6 Pro with Gecko 65 Watt GaN Brick"
)
col1, col2 = st.columns(2)
with col1:
    st.image("gecko.jpeg", width=300)
with col2:
    st.image("pixel.jpg", width=300)

data = {
    "power_level": [0, 30, 50, 80, 90, 95, 100],
    "charging_time": [0, 10, 21, 31, 13, 13, 14],
    "charging_rate": [0, 3.00, 0.95, 0.97, 0.77, 0.38, 0.36],
}

charging_data = pd.DataFrame(
    data, columns=["power_level", "charging_time", "charging_rate"]
)

st.subheader("Experiment Results")
st.table(charging_data)

st.subheader("Charging Rate vs Power Level and Charging Time v Power Level")

line_chart = (
    alt.Chart(charging_data)
    .mark_line()
    .encode(
        x=alt.X("power_level", title="Power Level (%)"),
        y=alt.Y("charging_rate", title="Charging Rate(per minute)"),
    )
    .properties(width=700, height=500, title="Charging Rate vs Power Level")
).configure_title(fontSize=20)

st.altair_chart(line_chart, use_container_width=True)

st.subheader("Conclusions:")
st.markdown(
    """
    - Charging rate is fast between 0 and 30% power level.
    - Charging rate is then quickly throttled down between 30% and 50% power level.
    - Further throtling down occurs between 50% and 100% power level.
    - From Internet Sources - "https://www.androidauthority.com/google-pixel-6-charging-test-3051231/"
        - The Google Pixel 6 Pro draws up to a max 22 Watts from power sources.
        - It then throttles down to as little as 2.5 Watts at near 100%.
        - All this is probably to prevent overheating the battery hence extending the battery life.
    - Powerful / Expensive GaN devices are great for many things but will not improve your Pixel 6 Pro's Fast Charging.
    - Follow me @LibranTechie for more Python and Data Science related content.
    """
)
