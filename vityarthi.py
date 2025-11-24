# Simple Patient Appointment and Emergency Resource Tracker

# Sample data stores
appointments = {}  # patient_name -> appointment_date
emergency_resources = {
    "medicines": {"Paracetamol": 10, "Insulin": 5},
    "organs": {"Kidney": 1, "Liver": 0}
}

def schedule_appointment(patient_name, date):
    if patient_name in appointments:
        print(f"Appointment already scheduled for {patient_name} on {appointments[patient_name]}")
    else:
        appointments[patient_name] = date
        print(f"Appointment scheduled for {patient_name} on {date}")

def view_appointments():
    if not appointments:
        print("No appointments scheduled.")
    else:
        print("Scheduled Appointments:")
        for patient, date in appointments.items():
            print(f"{patient}: {date}")

def update_resource(resource_type, resource_name, quantity):
    if resource_type in emergency_resources and resource_name in emergency_resources[resource_type]:
        emergency_resources[resource_type][resource_name] += quantity
        print(f"Updated {resource_name} quantity to {emergency_resources[resource_type][resource_name]}")
    else:
        print(f"{resource_name} not found in {resource_type} resources.")

def view_resources():
    print("Emergency Resources:")
    for r_type, items in emergency_resources.items():
        print(f"\n{r_type.capitalize()}:")
        for name, qty in items.items():
            print(f"{name}: {qty}")

# Sample usage
schedule_appointment("John Doe", "2025-12-01")
schedule_appointment("Jane Smith", "2025-12-03")
view_appointments()

update_resource("medicines", "Paracetamol", -2)
update_resource("organs", "Liver", 1)
view_resources()
