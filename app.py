
from pathlib import Path
import json
import joblib
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "models" / "house_price_model.joblib"
METRICS_PATH = ROOT / "models" / "metrics.json"

st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="wide")

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

st.title("🏠 House Price Prediction")
st.write("Enter property details to estimate the expected selling price.")

with st.sidebar:
    st.header("Project Information")
    if METRICS_PATH.exists():
        metrics = json.loads(METRICS_PATH.read_text())
        st.metric("Best Model", metrics["best_model"])
        st.metric("Test R²", metrics["model_results"][metrics["best_model"]]["R2"])
        st.metric("Test RMSE", f"₹{metrics['model_results'][metrics['best_model']]['RMSE']:,.0f}")
    st.caption("Built using Python, Pandas, Scikit-learn and Streamlit.")

col1, col2, col3 = st.columns(3)

with col1:
    area_sqft = st.number_input("Area (sq. ft.)", 300, 10000, 1800, 50)
    bedrooms = st.slider("Bedrooms", 1, 8, 3)
    bathrooms = st.slider("Bathrooms", 1, 6, 2)
    stories = st.slider("Stories", 1, 5, 2)
    parking = st.slider("Parking Spaces", 0, 5, 1)

with col2:
    property_age = st.slider("Property Age (years)", 0, 60, 5)
    distance_from_city_km = st.number_input("Distance from City Centre (km)", 0.0, 60.0, 8.0, 0.5)
    location_type = st.selectbox("Location Type", ["Urban", "Suburban", "Rural"])
    furnishing_status = st.selectbox(
        "Furnishing Status",
        ["Furnished", "Semi-Furnished", "Unfurnished"]
    )

with col3:
    main_road = st.selectbox("Main Road Access", ["Yes", "No"])
    guest_room = st.selectbox("Guest Room", ["No", "Yes"])
    basement = st.selectbox("Basement", ["No", "Yes"])
    air_conditioning = st.selectbox("Air Conditioning", ["Yes", "No"])
    preferred_area = st.selectbox("Preferred Area", ["No", "Yes"])

input_df = pd.DataFrame([{
    "area_sqft": area_sqft,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "stories": stories,
    "parking": parking,
    "property_age": property_age,
    "distance_from_city_km": distance_from_city_km,
    "location_type": location_type,
    "furnishing_status": furnishing_status,
    "main_road": main_road,
    "guest_room": guest_room,
    "basement": basement,
    "air_conditioning": air_conditioning,
    "preferred_area": preferred_area
}])

st.divider()
if st.button("Predict House Price", type="primary", use_container_width=True):
    prediction = max(float(model.predict(input_df)[0]), 0)
    st.success(f"Estimated House Price: ₹{prediction:,.0f}")
    st.caption("This is an ML-based estimate, not a certified property valuation.")

with st.expander("View Input Data"):
    st.dataframe(input_df, use_container_width=True)
