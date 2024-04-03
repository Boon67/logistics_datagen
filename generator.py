from faker import Faker
import random
import json, argparse
parser = argparse.ArgumentParser()
parser.add_argument("-records", help="the number of records to be generated")
args=parser.parse_args()

RECORDS=int(args.records)
fake = Faker()

def generate_tracking_event():
    event_id = fake.uuid4()
    event_timestamp = fake.date_time_this_month()
    event_description = fake.sentence(nb_words=6, variable_nb_words=True)
    event_location = fake.company()
    event_status = random.choice(["Received", "In Transit", "Out for Delivery", "Delivered"])
    return {
        "event_id": event_id,
        "event_timestamp": str(event_timestamp),
        "event_description": event_description,
        "event_location": event_location,
        "event_status": event_status
    }

def generate_package_data():
    tracking_id = fake.uuid4()
    package_id = fake.uuid4()
    status = random.choice(["In Transit", "Out for Delivery", "Delivered"])
    location = fake.city()
    estimated_delivery = fake.date_between(start_date='today', end_date='+30d').strftime('%Y-%m-%d')
    last_updated = fake.date_time_this_month()
    carrier = {"name": fake.company(), "contact": fake.phone_number()}
    sender = {"name": fake.company(), "address": fake.address(), "contact": fake.email()}
    recipient = {"name": fake.name(), "address": fake.address(), "contact": fake.email()}
    
    tracking_events = [generate_tracking_event() for _ in range(random.randint(1, 5))]
    
    return {
        "tracking_id": str(tracking_id),
        "package_id": str(package_id),
        "status": status,
        "location": location,
        "estimated_delivery": estimated_delivery,
        "last_updated": str(last_updated),
        "carrier": carrier,
        "sender": sender,
        "recipient": recipient,
        "tracking_events": tracking_events
    }

# Write the package records to a JSON file
print('Generating %d Records' % (RECORDS))
with open('package_data.json', 'w') as file:
    #file.write('[\n')
    for _ in range(RECORDS):
        package_record = generate_package_data()
        json.dump(package_record, file) # This write a line per record
        #json.dump(package_record, file, indent=2) #This writes a list in json file
        #if (_!=(RECORDS-1)):
            #file.write(',')
        file.write('\n')
        if _ % 10000 == 0:
            print('Records:', (_))
    #file.write(']\n')

print("Package data successfully written to 'package_data.json' file.")
