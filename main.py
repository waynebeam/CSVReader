import re

with open("test_data.csv", "r") as f:
  header_data = f.readline()
  body_data = f.readlines()

headings = header_data.split(",")
entries = [line.split(",") for line in body_data]


def clean_headings(original_headings):
  for i in range(len(original_headings)):
    original_headings[i] = clean_strings(original_headings[i])


def clean_strings(input_string):
  input_string = input_string.strip()
  in_quotes_pattern = re.compile(r"\"(.+)\"")
  result = in_quotes_pattern.search(input_string)
  if result:
    output_string = result.group(1)
  else:
    output_string = input_string

  return output_string


list_of_processed_entries = []
clean_headings(headings)

for line in entries:
  processed_entry = {}
  for i, heading in enumerate(headings):
    processed_entry[heading] = clean_strings(line[i])
  list_of_processed_entries.append(processed_entry)



