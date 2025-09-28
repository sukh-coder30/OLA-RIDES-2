import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Connect MySQL
engine = create_engine("mysql+mysqlconnector://root:pass123@localhost/ola_project")
df = pd.read_sql("SELECT * FROM rides", engine)

# App title
st.title("🚖 Ola Ride Analytics Dashboard")

# Sidebar menu
menu = st.sidebar.radio(
    "Navigation",
    ["Overall", "Vehicle Type", "Revenue", "Cancellation", "Ratings"]
)

# ------------------- Overall -------------------
if menu == "Overall":
    st.header("📊 Overall Ride Insights")
    rides_over_time = df.groupby("Date")["Booking_ID"].count().reset_index()
    st.line_chart(rides_over_time, x="Date", y="Booking_ID")

    st.subheader("Booking Status Breakdown")
    status_count = df["Booking_Status"].value_counts()
    st.bar_chart(status_count)

# ------------------- Vehicle Type -------------------
elif menu == "Vehicle Type":
    st.header("🚗 Vehicle Type Insights")
    top_vehicle = df.groupby("Vehicle_Type")["Ride_Distance"].mean().nlargest(5)
    st.bar_chart(top_vehicle)

    avg_ratings = df.groupby("Vehicle_Type")["Customer_Rating"].mean()
    st.bar_chart(avg_ratings)

# ------------------- Revenue -------------------
elif menu == "Revenue":
    st.header("💰 Revenue Insights")
    payment_revenue = df.groupby("Payment_Method")["Booking_Value"].sum()
    st.bar_chart(payment_revenue)

    top_customers = df.groupby("Customer_ID")["Booking_Value"].sum().nlargest(5)
    st.bar_chart(top_customers)

# ------------------- Cancellation -------------------
elif menu == "Cancellation":
    st.header("❌ Cancellation Insights")
    cancel_customer = df["Canceled_Rides_by_Customer"].value_counts().head(5)
    cancel_driver = df["Canceled_Rides_by_Driver"].value_counts().head(5)

    st.subheader("Cancelled by Customers")
    st.bar_chart(cancel_customer)

    st.subheader("Cancelled by Drivers")
    st.bar_chart(cancel_driver)

# ------------------- Ratings -------------------
elif menu == "Ratings":
    st.header("⭐ Ratings Insights")
    st.subheader("Driver Ratings Distribution")
    st.bar_chart(df["Driver_Ratings"].dropna(), bins=20)

    st.subheader("Customer vs Driver Ratings")
    avg_ratings = pd.DataFrame({
        "Customer_Rating": [df["Customer_Rating"].mean()],
        "Driver_Ratings": [df["Driver_Ratings"].mean()]
    })
    st.bar_chart(avg_ratings)
