import os 

def get_csv_location(target_name):
    current_directory = os.path.dirname(__file__)
   
    csv_path = os.path.join(current_directory, 'data/', 'auth.csv')
    return csv_path