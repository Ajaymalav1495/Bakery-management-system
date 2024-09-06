import streamlit as st
from sells import salling_page
from Stocks import stock_page

def inventory_page():
    st.title("Billing Page")
    st.write("---")
    # Create a dropdown menu
    option = st.selectbox(
        'Select a Page',
        ('Stock', 'Sells')
    )
    st.write("---")
    # Redirect to the selected page
    if option == 'Stock':
        st.header("Stock Page")
        stock_page()
        # Add your stock-related content here
    elif option == 'Sells':
        st.header("Sells Page")
        salling_page()
        # Add your sells-related content here
    st.write("---")