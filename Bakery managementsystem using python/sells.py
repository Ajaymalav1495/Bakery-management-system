import streamlit as st
import mysql.connector
import pandas as pd

def salling_page():
    st.write("---")
    st.markdown("Search Box  :")
    a = st.text_input("Enter product ID :")
    if st.button("Search"):
        try:
            conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="bakery"
                )
            c = conn.cursor()
            query = "SELECT * FROM Sales where Product_ID  in(%s)"
            c.execute(query,(a,))
            data = c.fetchall()
            df = pd.DataFrame(data, columns=['Product_id', 'Product_name', 'Quantity'])
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
    query = "SELECT * FROM Sales"
    c.execute(query)
    data = c.fetchall()
    df = pd.DataFrame(data, columns=['Product_id', 'Product_name', 'Quantity'])
    st.dataframe(df)