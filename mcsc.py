import streamlit as st
import requests
import math

st.set_page_config(page_title="Green Journey Advisor", layout="centered")

# ---- Header ----
st.title("🌿 Green Journey Advisor")
st.markdown("Plan your journey the eco-friendly way! 🌍")

# ---- Input Section ----
st.header("🚆 Plan Your Journey")
from_location = st.text_input("Enter starting point")
to_location = st.text_input("Enter destination")

def get_lat_lon(location):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': location,
        'format': 'json'
    }
    try:
        response = requests.get(url, params=params, headers={'User-Agent': 'GreenJourneyApp/1.0'})
        data = response.json()
        if data:
            lat = float(data[0]['lat'])
            lon = float(data[0]['lon'])
            return lat, lon
        else:
            return None, None
    except Exception as e:
        return None, None

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c  # in km
    return distance

if st.button("Suggest Green Options"):
    if not from_location or not to_location:
        st.error("Please enter both starting point and destination.")
    else:
        lat1, lon1 = get_lat_lon(from_location)
        lat2, lon2 = get_lat_lon(to_location)

        if None in (lat1, lon1, lat2, lon2):
            st.error("Could not find one or both locations. Please check the spelling and try again.")
        else:
            distance = haversine(lat1, lon1, lat2, lon2)
            st.write(f"Distance between **{from_location}** and **{to_location}** is approximately **{distance:.2f} km**.")

            st.success(f"Green options from {from_location} to {to_location}:")

            if distance <= 10:
                st.markdown("- 🚶 Walk if under 2km")
            elif distance <= 88:
                st.markdown("- 🚲 Use a bike for medium distances")
            else:
                st.markdown("- 🚌 Prefer electric buses or shared rides or aeroplanes or trains")

            carbon_saved = round(distance * 0.2, 2)  # Example: 0.2 kg CO2 saved per km
            st.markdown(f"🌱 Estimated Carbon Saved: **{carbon_saved} kg CO₂**")

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
