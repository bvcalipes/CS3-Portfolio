class Patient:
    def __init__(self, name: str, bill_amount: float):
        self.__name = name
        self.__bill_amount = float(bill_amount)

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount: float):
        self.__bill_amount = float(bill_amount)

    def calculate_bill(self):
        return self.__bill_amount
        
    def display_patient_type(self):
        print ("Patient Type: Regular Patient")


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80  # 20% discount
    def display_patient_type(self):
        print ("Patient Type: Senior Citizen")


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85  # 15% discount
    def display_patient_type(self):
        print ("Patient Type: PhilHealth Member")


# Instantiate one object per class
regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000)
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)

# Display the original and final computed bills
patients = [regular_patient, senior_patient, philhealth_patient]

print("Hospital Billing System")
print("--------------------------------")
for patient in patients:
    print(f"Patient Name: {patient.get_name()}")
    print(f"Patient Type: {patient.display_patient_type()}")
    print(f"Original Bill: ₱{patient.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{patient.calculate_bill():,.2f}\n")
