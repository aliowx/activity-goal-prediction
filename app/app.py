import json
import csv
from datetime import datetime

# Define the desired output columns
columns = [
    "id", "Question", "Options", "Answer", "Analysis", 
    "Category", "Subject", "Course_Stage", "Knowledge", 
    "Exam_Type", "Exam_Subject", "Exam_Stage", "Source", "Processing_Date"
]

# Function to process JSON and write to CSV
def process_json_to_csv(input_file, output_file):
    # Read JSON file
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Open CSV file for writing
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        
        # Process each question
        for item in data:
            # Ensure all required fields are present, use empty string if missing
            row = {col: item.get(col, '') for col in columns}
            # Convert Options list to string if it's a list
            if isinstance(row['Options'], list):
                row['Options'] = '\n'.join(row['Options'])
            writer.writerow(row)

# Example usage
if __name__ == "__main__":
    input_json = "input.json"  # Replace with your JSON file path
    output_csv = "output.csv"  # Output CSV file path
    process_json_to_csv(input_json, output_csv)
    print(f"CSV file '{output_csv}' has been generated successfully.")