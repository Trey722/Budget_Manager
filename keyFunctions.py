import os 
import csv

def get_csv_location(target_name):
    current_directory = os.path.dirname(__file__)
   
    csv_path = os.path.join(current_directory, 'data/', 'auth.csv')
    return csv_path




def create_csv(location):
    # Sample data
    data = [['username', 'type', 'amount', 'category', 'date', 'description', 'institution']]

    # Create directory if it doesn't exist
    directory = os.path.dirname(location)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Writing data to a CSV file
    with open(location, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)

    print(f"CSV file created at '{location}'.")
    
def add_line_to_csv(location, new_data):
    with open(location, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(new_data)

    