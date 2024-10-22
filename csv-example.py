import csv

# Define a function to read the CSV file and return an iterable list
def read_csv_to_list(file_path):
    data_list = []
    
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        # Optionally skip the header if it exists
        # next(csv_reader, None)
        for row in csv_reader:
            data_list.append(row)
    
    return data_list

# Example usage
if __name__ == "__main__":
    file_path = 'data.csv'  # replace with your CSV file path
    data = read_csv_to_list(file_path)
    
    # Iterate over the list to print the rows
    for row in data:
        print(row)