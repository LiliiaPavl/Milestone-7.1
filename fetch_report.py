import requests
import sys

def fetch_report(month, department):
    url = f'http://127.0.0.1:5000/birthdays?month={month}&department={department}'
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        return

    data = response.json()
    print(f"Report for {department} department for {month.capitalize()} fetched.")
    print(f"Total: {data['total']}")
    print("Employees:")
    for emp in data['employees']:
        print(f"- {emp['birthday']}, {emp['name']}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fetch_report.py <month> <department>")
        sys.exit(1)

    month = sys.argv[1].lower()
    department = sys.argv[2].capitalize()

    fetch_report(month, department)
