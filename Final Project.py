class Patient:
    def __init__(self, pid=None, name=None, disease=None, gender=None, age=None):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def get_pid(self):
        return self.pid

    def get_name(self):
        return self.name
    def get_disease(self):
        return self.disease

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def set_pid(self, new_pid):
        self.pid = new_pid

    def set_name(self, new_name):
        self.name = new_name

    def set_disease(self, new_disease):
        self.disease = new_disease

    def set_gender(self, new_gender):
        self.gender = new_gender

    def set_age(self, new_age):
        self.age = new_age

    def __str__(self):
        print(f"pid: {self.pid}_name: {self.name}_disease: {self.disease}_gender: {self.gender}_age: {self.age}")

class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    def format_patient_info_for_file(self, patient):
        return f"{patient.get_pid()}_{patient.get_name()}_{patient.get_disease()}_{patient.get_gender()}_{patient.get_age()}"

    def enter_patient_info(self):
        pid = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        disease = input("Enter patient disease: ")
        gender = input("Enter patient gender: ")
        age = input("Enter patient age: ")
        return Patient(pid, name, disease, gender, age)

    def read_patients_file(self):
        try:
            with open("patients.txt", "r") as file:
                for line in file:
                    pid, name, disease, gender, age = line.strip().split("_")
                    patient = Patient(int(pid), name, disease, gender, int(age))
                    self.patients.append(patient)
        except FileNotFoundError:
            pass

    def search_patient_by_id(self):
        patient_id = input("Enter patient ID to search: ")
        for patient in self.patients:
            if patient.get_pid() == patient_id:
                self.display_patient_info(patient)
                return
        print("Can't find the patient...")

    def display_patient_info(self, patient):
        print("Patient Information:")
        print(f"ID: {patient.get_pid()}")
        print(f"Name: {patient.get_name()}")
        print(f"Disease: {patient.get_disease()}")
        print(f"Gender: {patient.get_gender()}")
        print(f"Age: {patient.get_age()}")

    def edit_patient_info_by_id(self):
        patient_id = int(input("Enter patient ID to edit: "))
        for patient in self.patients:
            if patient.get_pid() == patient_id:
                new_name = input("Enter new name: ")
                new_disease = input("Enter new disease: ")
                new_gender = input("Enter new gender: ")
                new_age = int(input("Enter new age: "))
                patient.set_name(new_name)
                patient.set_disease(new_disease)
                patient.set_gender(new_gender)
                patient.set_age(new_age)
                self.write_list_of_patients_to_file()
                print("Patient information updated.")
                return
        print("Cannot find the patient...")

    def display_patients_list(self):
        print("List of Patients:")
        for patient in self.patients:
            self.display_patient_info(patient)
            print("-" * 20)

    def write_list_of_patients_to_file(self):
        with open("patients.txt", "w") as file:
            for patient in self.patients:
                file.write(self.format_patient_info_for_file(patient) + "\n")

    def add_patient_to_file(self):
        new_patient = self.enter_patient_info()
        self.patients.append(new_patient)
        self.write_list_of_patients_to_file()
        print("New patient added.")

Patient =  Patient()
Patient.get_pid()