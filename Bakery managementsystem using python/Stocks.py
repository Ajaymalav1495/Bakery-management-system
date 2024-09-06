import streamlit as st
import mysql.connector
import pandas as pd
def stock_page():
    def check_inputs(input1, input2, input3, input4):
        results = []
        for i, input_string in enumerate([input1, input2, input3, input4], start=1):
            if input_string.strip() == "":
                results.append(f"Input {i} is empty")
            else:
                results.append(f"Input {i} is not empty")
        return results

    def all_inputs_not_empty(input1, input2, input3, input4):
        return all(input_string.strip() != "" for input_string in [input1, input2, input3, input4])

    def stock_page():
        # Streamlit inputs
        p_id = st.text_input("Enter Product ID:").strip()
        p_name = st.text_input("Enter Product Name:").strip()
        price = st.number_input("Enter Price:")
        quantity = st.number_input("Enter Quantity:")
        
        # Check inputs and display results
        if st.button("Submit"):
            input1 = p_id
            input2 = p_name
            input3 = str(price)
            input4 = str(quantity)
            results = check_inputs(input1, input2, input3, input4)
            for result in results:
                st.write(result)

            if all_inputs_not_empty(input1, input2, input3, input4):
                try:
                    # Establish database connection
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",  # Your MySQL password
                        database="bakery"
                    )
                    c = conn.cursor()

                    # Insert query
                    query = "INSERT INTO Stock VALUES (%s, %s, %s, %s)"
                    c.execute(query, (p_id, p_name, price, quantity))

                    # Commit changes
                    conn.commit()
                    st.success("Data inserted successfully!")
                except mysql.connector.Error as e:
                    st.error(f"Error: {e}")
                finally:
                    # Close the connection
                    conn.close()
            else:
                st.error("Sorry, all fields must be filled.")


        st.write("---")
        #search Box
        st.markdown("Search Box:")
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
                query = "SELECT * FROM Stock where Product_ID  in(%s)"
                c.execute(query,(a,))
                data = c.fetchall()
                df = pd.DataFrame(data, columns=['Product_ID', 'Product_Name', 'Price', 'Quantity'])
                st.dataframe(df)
            except mysql.connector.Error as e:
                st.error(f"Error: {e}")
            finally:
                conn.close()

        st.write("---")
        # Show all records
        if st.button("Show"):
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="bakery"
                )
                c = conn.cursor()
                query = "SELECT * FROM Stock"
                c.execute(query)
                data = c.fetchall()
                df = pd.DataFrame(data, columns=['ProductID', 'ProductName', 'Price', 'Quantity'])
                st.dataframe(df)
            except mysql.connector.Error as e:
                st.error(f"Error: {e}")
            finally:
                conn.close()

        
    # Call the function to display the Stock page
    stock_page()
    
