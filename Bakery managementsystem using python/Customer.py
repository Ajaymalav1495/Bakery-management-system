import streamlit as st
import mysql.connector
import pandas as pd
def customer_page():
    st.title("Customer Page")
    st.write("---")
    st.markdown("Search Box  :")
    a = st.text_input("Enter Customer ID :")
    if st.button("Search"):
        try:
            conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="bakery"
                )
            c = conn.cursor()
            query = "SELECT * FROM customer where customer_ID  in(%s)"
            c.execute(query,(a,))
            data = c.fetchall()
            df = pd.DataFrame(data, columns=['Customer_id', 'Customer_name', 'Contact no','Address'])
            st.dataframe(df)
        except mysql.connector.Error as e:
            st.error(f"Error: {e}")
        finally:
            conn.close()
    
    st.write("---")

    conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="bakery"
            )
    c = conn.cursor()
    query = "SELECT * FROM Customer"
    c.execute(query)
    data = c.fetchall()
    df = pd.DataFrame(data, columns=['Customer_id', 'Customer_name', 'Contact no','Address'])
    st.dataframe(df)
    st.write("---")
