
def generate_order_id():
    import uuid
    return str(uuid.uuid4())
order_id = generate_order_id()
print(f"Your unique order ID is: {order_id}")


