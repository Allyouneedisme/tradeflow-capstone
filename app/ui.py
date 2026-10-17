import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# API_URL = "http://localhost:8000" # Use this for local testing
API_URL = "http://tradeflow-service" # Use this for Kubernetes

st.set_page_config(page_title="TradeFlow", page_icon="🌍", layout="wide")

st.title("🌍 TradeFlow - Import/Export Management")
st.markdown("Manage your products, orders, and shipments in one place.")

# Sidebar navigation
menu = ["Dashboard", "Add Product", "Create Order"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Dashboard":
    st.header("Current Products")
    try:
        response = requests.get(f"{API_URL}/products/")
        if response.status_code == 200:
            products = response.json()
            if products:
                df = pd.DataFrame(products)
                st.dataframe(df, use_container_width=True)
            else:
                st.info("No products found. Add one from the sidebar!")
        else:
            st.error("Failed to fetch products.")
    except Exception as e:
        st.warning(f"Could not connect to API: {e}")

elif choice == "Add Product":
    st.header("Add a New Product")
    with st.form("product_form"):
        name = st.text_input("Product Name")
        sku = st.text_input("SKU")
        price = st.number_input("Price", min_value=0.0, step=0.01)
        quantity = st.number_input("Quantity", min_value=0, step=1)
        submitted = st.form_submit_button("Save Product")
        
        if submitted:
            payload = {"name": name, "sku": sku, "price": price, "quantity": quantity}
            try:
                response = requests.post(f"{API_URL}/products/", json=payload)
                if response.status_code == 200:
                    st.success(f"Product {name} added successfully!")
                else:
                    st.error("Failed to add product.")
            except Exception as e:
                st.error(f"Error: {e}")

elif choice == "Create Order":
    st.header("Create a New Order")
    with st.form("order_form"):
        order_number = st.text_input("Order Number (e.g., ORD-001)")
        order_type = st.selectbox("Order Type", ["IMPORT", "EXPORT"])
        product_id = st.number_input("Product ID", min_value=1, step=1)
        quantity = st.number_input("Quantity", min_value=1, step=1)
        total_cost = st.number_input("Total Cost", min_value=0.0, step=0.01)
        submitted = st.form_submit_button("Create Order")
        
        if submitted:
            payload = {
                "order_number": order_number, "order_type": order_type,
                "product_id": product_id, "quantity": quantity, "total_cost": total_cost
            }
            try:
                response = requests.post(f"{API_URL}/orders/", json=payload)
                if response.status_code == 200:
                    st.success(f"Order {order_number} created successfully!")
                else:
                    st.error("Failed to create order.")
            except Exception as e:
                st.error(f"Error: {e}")
