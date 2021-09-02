import json


text_json = '''{
    "demo": "Processing JSON in Python",
    "instructor": "Andre",
    "duration": 5.0
}'''

print(text_json)    # Print variable
data = json.loads(text_json) # Load string variable into JSON dict
print()
print(data)

#instructor = data['instructor']
instructor = data.get('instructor', 'None found!') # Obtain value from instructor key. If none if found return default
print(instructor)

data['instructor'] = "Jeff" # Assign new value to instructor key
new_json = json.dumps(data) # Define new  variable containing the string value of the JSON Dict

print()
print(type(new_json)) # Show me this is a string
print(new_json)