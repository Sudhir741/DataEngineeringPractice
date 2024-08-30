import csv

class Product:
    def __init__(self, product_id, category, subcategory, price, cost):
        self.product_id = product_id
        self.category = category
        self.subcategory = subcategory
        self.price = price
        self.cost = cost

    def profit_margin(self):
        return (self.cost - self.price) / self.cost * 100

class Transaction:
    def __init__(self, transaction_id, product, quantity, date):
        self.transaction_id = transaction_id
        self.product = product
        self.quantity = quantity
        self.date = date

    def total_sales(self):
        return self.product.price * self.quantity

def read_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row

def process_data(data):
    products = {}
    transactions = []

    for row in data:
        product_id = row['Product ID']
        if product_id not in products:
            products[product_id] = Product(
                product_id,
                row['Product Category'],
                row['Product Subcategory'],
                float(row['Product Price']),
                float(row['Total Sales'])
            )
        transaction = Transaction(
            row['Transaction ID'],
            products[product_id],
            int(row['Quantity Sold']),
            row['Transaction Date']
        )
        transactions.append(transaction)

    return products, transactions

def calculate_profit_margins(products):
    profit_margins = {product_id: product.profit_margin() for product_id, product in products.items()}
    return profit_margins

def most_profitable_products(profit_margins, top_n=5):
    sorted_products = sorted(profit_margins.items(), key=lambda x: x[1], reverse=True)
    return sorted_products[:top_n]

#Passing files and calling functions
data = read_data('processed_data.csv')
products, transactions = process_data(data)
profit_margins = calculate_profit_margins(products)
top_profitable_products = most_profitable_products(profit_margins)

print("Top Profitable Products:")
for product_id, margin in top_profitable_products:
    print(f"Product ID: {product_id}, Profit Margin: {margin:.2f}%")
