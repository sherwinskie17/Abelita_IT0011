# Function to convert date format
def convert_date(date_str):
    months = [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ]
    month, day, year = date_str.split('/')
    month_name = months[int(month) - 1]
    return f"{month_name} {int(day)}, {year}"

# Get input from user
date_input = input("Enter the date (mm/dd/yyyy): ")

# Convert the date and print the output
formatted_date = convert_date(date_input)
print(f"Date Output: {formatted_date}")