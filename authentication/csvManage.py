import csv

def write_to_csv(data, file_name):
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([data])
        
def csv_to_dict(file_name):
    newDict = {}
    with open(file_name, mode='r') as file:
        reader = file
        for row in reader:
            row = row.split(",")
            try:
                newDict[row[0]] = row[1]
            except:
                continue
    return newDict










