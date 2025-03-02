import re

input_file = "F://StudiaMag//2024Z/PB/phishsb/ml//datasets//adjusted//PhiUSIIL_Phishing_URL_Dataset_modified.csv"   # Change this to your actual file name
output_file = "F://StudiaMag//2024Z/PB/phishsb/ml//datasets//adjusted//PhiUSIIL_Phishing_URL_Dataset_clean.csv"

expected_fields = 38  # The required number of fields

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8", newline="") as outfile:
    for line in infile:
        line = re.sub(r";+$", "", line.strip())  # Remove trailing semicolons and strip spaces
        line = line.replace(";", ",")  # Convert semicolons to commas
        fields = line.split(",")  # Split line to count fields

        if len(fields) == expected_fields:  # Keep only valid lines
            outfile.write(line + "\n")

print("CSV file has been cleaned and saved as", output_file)