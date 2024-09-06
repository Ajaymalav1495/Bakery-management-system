import streamlit as st
from streamlit_option_menu import option_menu

# Import your page files
from Home import home_page
from Employee import employee_page
from Customer import customer_page
from Inventory import inventory_page
from Billing import billing_page


# Create a sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Employee", "Customer", "Inventory", "Billing"],
        icons=["house", "people", "person", "box", "cash"],
        menu_icon="cast",
        default_index=0,
    )
# Redirect to the selected page
if selected == "Home":
    home_page()
elif selected == "Employee":
    employee_page()
elif selected == "Customer":
    customer_page()
elif selected == "Inventory":
    inventory_page()
elif selected == "Billing":
    billing_page()
