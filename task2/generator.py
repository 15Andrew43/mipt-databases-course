import json
import random
import sys

def generate_data(num_elements):
    data = []
    for _ in range(num_elements):
        user_id = random.randint(100, 999)
        product_id = random.randint(1, 10)
        order_id = random.randint(1000, 9999)
        
        user = {
            "id": user_id,
            "name": "User" + str(user_id),
            "age": random.randint(20, 50),
            "email": "user" + str(user_id) + "@example.com",
            "address": {
                "city": "City" + str(user_id),
                "zip": str(random.randint(10000, 99999)),
                "country": "Country" + str(user_id)
            },
            "tags": ["tag1", "tag2", "tag3"]
        }

        products = [
            {"id": i, "name": "Product" + str(i), "price": random.randint(100, 1000)} for i in range(1, 4)
        ]

        orders = {
            "order1": {
                "id": order_id,
                "user_id": user_id,
                "total_amount": sum([product['price'] for product in products]),
                "items": [{"product_id": product_id, "quantity": random.randint(1, 3)} for product_id in range(1, 4)]
            },
            "order2": {
                "id": order_id + 1,
                "user_id": user_id,
                "total_amount": random.randint(100, 1000),
                "items": [{"product_id": product_id, "quantity": random.randint(1, 3)} for product_id in range(1, 4)]
            }
        }

        data.append({"user": user, "products": products, "orders": orders})
    
    return data

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <num_elements>")
        sys.exit(1)

    num_elements = int(sys.argv[1])

    data_to_load = generate_data(num_elements)

    with open('generated_data.json', 'w') as f:
        json.dump(data_to_load, f, indent=2)

    print(f"Данные успешно сгенерированы и сохранены в файле generated_data.json с {num_elements} элементами.")
