class DistributedDatabase:
    def __init__(self):
        self.nodes = [{}, {}]  # Two database nodes

    def insert_order(self, order_data):
        for node in self.nodes:
            node[order_data["order_id"]] = order_data

    def get_order(self, order_id):
        for node in self.nodes:
            if order_id in node:
                return node[order_id]
        return None

# Example usage
db = DistributedDatabase()

order_data = {"order_id": "12345", "customer_id": "9876", "total_amount": 100.50}
db.insert_order(order_data)

order_id = "12345"
order = db.get_order(order_id)
print("Retrieved Order:", order)
print("Order proceeded successfully")
