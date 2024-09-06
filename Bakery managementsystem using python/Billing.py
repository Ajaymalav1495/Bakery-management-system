
import streamlit as st
import mysql.connector
import uuid
def billing_page():
        st.title("Billing Page")
        def generate_unique_order_id():
            return str(uuid.uuid4())
        # Input fields for customer details
        ord_id = generate_unique_order_id()
        order_id=st.text_input("Order ID", value=ord_id)
        c_name = st.text_input("Enter Customer Name")
        c_no = st.text_input("Enter Customer Contact No.")
        c_add = st.text_input("Enter Customer Address")

        if st.button("Submit"):
            # Check if inputs are empty
            if not c_name or not c_no or not c_add:
                st.error("One or more input fields are empty.")
            else:
                # Connect to MySQL
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="bakery"
                )
                cursor = conn.cursor()

                # Check if customer already exists
                check_query = "SELECT * FROM customer WHERE customer_name=%s AND contact=%s"
                cursor.execute(check_query, (c_name, c_no))
                existing_data = cursor.fetchone()
                l1=[]
                for i in existing_data:
                    l1.append(i)
                    C_id1 = l1[0]
                    

                if existing_data:
                    st.warning("Customer already exists. Please check the details.")
                else:
                    # Insert data into the database
                    insert_query = "INSERT INTO customer (customer_name, contact, address) VALUES (%s, %s, %s)"
                    cursor.execute(insert_query, (c_name, c_no, c_add))
                    conn.commit()
                    st.success("New customer data inserted successfully!")

                # Generate and display unique order ID
                st.text_input("Order ID", value=C_id1)

                # Close the connection
                cursor.close()
                conn.close()

    # Run the billing page function
billing_page()
