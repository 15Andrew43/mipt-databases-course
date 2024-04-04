import json
import random
import string

def generate_random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_email():
    domains = ["example.com", "test.com", "gmail.com", "hotmail.com"]
    username = generate_random_string(random.randint(5, 10))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def generate_random_address():
    streets = ["Street 1", "Street 2", "Street 3", "Avenue 1", "Avenue 2"]
    cities = ["City 1", "City 2", "City 3", "Town 1", "Town 2"]
    countries = ["Country 1", "Country 2", "Country 3", "Nation 1", "Nation 2"]
    return {
        "street": random.choice(streets),
        "city": random.choice(cities),
        "country": random.choice(countries)
    }

def generate_random_interests():
    interests = ["Sports", "Music", "Movies", "Books", "Travel"]
    return random.sample(interests, random.randint(1, 3))

def generate_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "name": generate_random_string(),
            "age": random.randint(18, 65),
            "email": generate_random_email(),
            "address": generate_random_address(),
            "interests": generate_random_interests()
        }
        data.append(record)
    return data

def write_to_json_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    num_records = 1000000
    output_file = "data.json"
    data = generate_data(num_records)
    write_to_json_file(data, output_file)
    print(f"Generated {num_records} records and sasdfved to {output_file}.")
