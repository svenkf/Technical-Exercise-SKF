import pandas as pd

# Initialize counters for total and failed samples by origin
total_samples_by_origin = {}
failed_samples_by_origin = {}
failed_samples_details = []

# Open the file and read line by line
with open('/mnt/c/Users/SvenK/Exercise/samples.txt', 'r') as file:
    # Skip the header
    header = file.readline().strip().split(',')
    
    for line in file:
        fields = line.strip().split(',')
        
        sample = fields[0]
        pct_covered_bases = float(fields[2])
        qc_pass = fields[5]
        
        # Determine the origin
        origin = sample[1]
        
        if origin not in total_samples_by_origin:
            total_samples_by_origin[origin] = 0
            failed_samples_by_origin[origin] = 0
        
        # 
        total_samples_by_origin[origin] += 1
        
        #check if the sample fails the criteria
        if pct_covered_bases < 95 or qc_pass == 'FALSE':
            failed_samples_by_origin[origin] += 1
            failed_samples_details.append(line.strip())

# to calculate the rates of failure by origin and write to a text file
with open('results.txt', 'w') as output_file:
    output_file.write("Failure rate by origin:\n")
    for origin in total_samples_by_origin:
        total = total_samples_by_origin[origin]
        failed = failed_samples_by_origin[origin]
        failure_rate = (failed / total) * 100
        output_file.write(f"Origin: {origin}, Failure Rate: {failure_rate:.2f}%\n")

    output_file.write("\nFailed samples details:\n")
    for detail in failed_samples_details:
        output_file.write(f"{detail}\n")
