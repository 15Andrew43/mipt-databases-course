import csv
import sys
import random
import string

def generate_csv(filename, num_rows):
    meaningful_words = {
        'ITEM_NAME': ['watch', 'sundial', 'clock', 'compass', 'glass', 'mechanism', 'log', 'train', 'pocket', 'timer', 'hourglass', 'scale', 'pendulum', 'calendar', 'scale', 'calendar', 'anemometer', 'thermometer', 'barometer', 'sundial'],
        'TITLE': ['Pocket horizontal sundial', 'Ship\'s log-glass', 'Model of train of wheels', 'Pocket watch', 'Spring-driven clock mechanism', 'Hourglass', 'Glass timer', 'Barometer', 'Thermometer', 'Anemometer', 'Pendulum clock', 'Pocket compass', 'Ship\'s clock', 'Glass scale', 'Sun clock', 'Hourglass timer', 'Weather glass', 'Clockwork mechanism', 'Glass calendar', 'Glass pendulum'],
        'MAKER': ['Ansonia Clock Co.', 'Abbot Horne', 'New York Clockmakers', 'John Smith', 'George Brown', 'Robert Johnson', 'James Davis', 'William Wilson', 'Elizabeth Taylor', 'Richard Martin', 'Mary Robinson', 'Joseph White', 'Thomas Harris', 'Margaret Moore', 'Edward Thompson', 'Sarah King', 'David Lee', 'Helen Allen', 'Daniel Wright', 'Anna Garcia'],
        'PLACE_MADE': ['New York', 'London', 'Paris', 'Berlin', 'Moscow', 'Tokyo', 'Beijing', 'Sydney', 'Rome', 'Madrid', 'Athens', 'Cairo', 'Dubai', 'Mumbai', 'Rio de Janeiro', 'Mexico City', 'Toronto', 'Los Angeles', 'Chicago', 'Singapore'],
        'MATERIALS': ['glass', 'wood', 'metal', 'plastic', 'ceramic', 'paper', 'cloth', 'leather', 'stone', 'clay', 'rubber', 'bronze', 'silver', 'gold', 'copper', 'brass', 'aluminum', 'titanium', 'carbon fiber', 'nickel'],
        'MEASUREMENTS': ['small', 'medium', 'large', 'tiny', 'huge', 'miniature', 'gigantic', 'massive', 'sizable', 'compact', 'enormous', 'tiny', 'oversized', 'diminutive', 'petite', 'immense', 'lilliputian', 'vast', 'mammoth', 'minuscule'],
        'DESCRIPTION': ['Antique clock mechanism', 'Old pocket watch', 'Vintage sundial', 'Modern glass timer', 'Historical barometer', 'Traditional thermometer', 'Classic anemometer', 'Retro pendulum clock', 'Ancient compass', 'Unique hourglass', 'Collectible glass scale', 'Artistic glass pendulum', 'Contemporary glass calendar', 'Elegant glass hourglass', 'Handcrafted sundial', 'Delicate glass thermometer', 'Exquisite glass anemometer', 'Stylish glass barometer', 'Fashionable glass clock', 'Intricate glass mechanism'],
        'WHOLE_PART': ['WHOLE', 'PART'],
        'COLLECTION': ['SCM - Time Measurement', 'Antique Clocks Collection', 'Vintage Watches Exhibit', 'Modern Timepieces Collection', 'Historical Clocks Display', 'Sundials Showcase', 'Barometers Collection', 'Thermometers Exhibit', 'Anemometers Collection', 'Horology Museum', 'Clockwork Art Gallery', 'Glass Instruments Collection', 'Precision Instruments Exhibit', 'Timekeeping Devices Display', 'Timepiece Artifacts Collection', 'Chronometry Museum', 'Clockmakers Exhibition', 'Temporal Artifacts Display', 'Horological Instruments Collection', 'Timekeeping Artifacts Exhibit']
    }

    fieldnames = ['id_NUMBER', 'ITEM_NAME', 'TITLE', 'MAKER', 'DATE_MADE', 'PLACE_MADE', 'MATERIALS', 'MEASUREMENTS', 'DESCRIPTION', 'WHOLE_PART', 'COLLECTION']


    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_rows):
            row = {
                'id_NUMBER': ''.join(random.choices(string.ascii_letters + string.digits, k=8)),
                'ITEM_NAME': random.choice(meaningful_words['ITEM_NAME']),
                'TITLE': random.choice(meaningful_words['TITLE']),
                'MAKER': random.choice(meaningful_words['MAKER']),
                'DATE_MADE': f"{random.randint(1900, 2022)}-{random.randint(1, 12)}-{random.randint(1, 28)}",
                'PLACE_MADE': random.choice(meaningful_words['PLACE_MADE']),
                'MATERIALS': random.choice(meaningful_words['MATERIALS']),
                'MEASUREMENTS': random.choice(meaningful_words['MEASUREMENTS']),
                'DESCRIPTION': random.choice(meaningful_words['DESCRIPTION']),
                'WHOLE_PART': random.choice(meaningful_words['WHOLE_PART']),
                'COLLECTION': random.choice(meaningful_words['COLLECTION'])
            }
            writer.writerow(row)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py filename num_rows")
        sys.exit(1)

    filename = sys.argv[1]
    num_rows = int(sys.argv[2])

    generate_csv(filename, num_rows)
