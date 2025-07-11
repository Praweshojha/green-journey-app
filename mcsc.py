import streamlit as st

st.set_page_config(page_title="Green Journey Advisor", layout="centered")

# ---- Header ----
st.title("🌿 Green Journey Advisor")
st.markdown("Plan your journey the eco-friendly way! 🌍")

# ---- Input Section ----
st.header("🚆 Plan Your Journey")
from_location = st.text_input("Enter starting point")
to_location = st.text_input("Enter destination")

if st.button("Suggest Green Options"):
    st.success(f"Green options from {from_location} to {to_location}:")
    st.markdown("- 🚶 Walk if under 2km")
    st.markdown("- 🚲 Use a bike for medium distances")
    st.markdown("- 🚌 Prefer electric buses or shared rides")
    st.markdown("- 🌱 Estimated Carbon Saved: *1.4kg CO₂*")

# ---- Tips Section ----
st.header("♻ Eco Travel Tips")
with st.expander("Click to view tips"):
    st.markdown("""
    - Use public transport whenever possible  
    - Avoid flights for short distances  
    - Offset your carbon footprint using online services  
    - Carry reusable bottles and bags  
    """)

# ---- Footer ----
st.markdown("---")
st.caption("Developed as part of HCI Assignment - Green Journey Advisor")