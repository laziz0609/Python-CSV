import csv

input_path = "students.csv"
output_path = "rating.csv"


with open(input_path) as f:
    reader = csv.DictReader(f, fieldnames=["name", "score"])
    next(reader)
    
    data = list(reader)
    
    data = sorted(data, key=lambda item: item["score"], reverse=True)
    
    for i in range(len(data)):
        data[i]['sn'] = i + 1
        

with open(output_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["sn", "name", "score"])
    
    writer.writeheader()

    # Write all the data rows
    writer.writerows(data)