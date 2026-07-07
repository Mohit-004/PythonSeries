patients = []


def add_patient():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    disease = input("Enter Disease: ")

    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "disease": disease
    }

    patients.append(patient)
    print("Patient Added Successfully.\n")


def view_patients():
    if len(patients) == 0:
        print("No Patients Available.\n")
        return

    print("\n------ Patient List ------")

    for patient in patients:
        print(f"ID       : {patient['id']}")
        print(f"Name     : {patient['name']}")
        print(f"Age      : {patient['age']}")
        print(f"Disease  : {patient['disease']}")
        print("--------------------------")


def search_patient():
    name = input("Enter Patient Name: ").lower()

    for patient in patients:
        if patient["name"].lower() == name:
            print("\nPatient Found")
            print(patient)
            return

    print("Patient Not Found.\n")


def update_disease():
    patient_id = input("Enter Patient ID: ")

    for patient in patients:
        if patient["id"] == patient_id:
            patient["disease"] = input("Enter New Disease: ")
            print("Disease Updated Successfully.\n")
            return

    print("Patient Not Found.\n")


def discharge_patient():
    patient_id = input("Enter Patient ID: ")

    for patient in patients:
        if patient["id"] == patient_id:
            patients.remove(patient)
            print("Patient Discharged Successfully.\n")
            return

    print("Patient Not Found.\n")


def count_patients():
    print(f"Total Patients: {len(patients)}\n")


while True:

    print("====== HOSPITAL MANAGEMENT ======")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Update Disease")
    print("5. Discharge Patient")
    print("6. Count Patients")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        view_patients()

    elif choice == "3":
        search_patient()

    elif choice == "4":
        update_disease()

    elif choice == "5":
        discharge_patient()

    elif choice == "6":
        count_patients()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.\n")