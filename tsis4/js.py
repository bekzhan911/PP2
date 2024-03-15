import json

# Read data from the JSON file
try:
    with open("C:/Users/Red/Desktop/pp2/tsis4/sample-data.json", 'r') as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
    exit()

# Extract relevant information (modify as needed based on your actual JSON structure)
interfaces = data.get("interfaces", [])

# Print the header
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

# Print interface details
for interface in interfaces:
    dn = interface.get("DN", "")
    description = interface.get("Description", "")
    speed = interface.get("Speed", "")
    mtu = interface.get("MTU", "")
    print("{:<50} {:<20} {:<10} {:<6}".format(dn, description, speed, mtu))

# Optional: Calculate the total number of interfaces
total_interfaces = len(interfaces)
print("\nTotal interfaces:", total_interfaces)
