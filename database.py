def create_patient_entry(patient_name, patient_mrn, patient_age):
    new_patient = [patient_name, patient_mrn, patient_age, []]
    return new_patient

def main_driver():
    db = []
    db.append(create_patient_entry("Ann Ables", 1, 34))
    db.append(create_patient_entry("Bob Boyles", 2, 45))
    db.append(create_patient_entry("Chris Chou", 3, 52))
    print(db)
    add_test_to_patient(db, 1, "HDL", 120)
    add_test_to_patient(db, 2, "LDL", 99)
    add_test_to_patient(db, 2, "HDL", 100)
    add_test_to_patient(db, 3, 'HDL', 117)
    room_numbers = ["103", "232", "333"]
    print(db)
    print_directory(db, room_numbers)
    testresult = get_test_result(db, 2, 'LDL')
    print(testresult)

def print_directory(db, room_numbers):
    for i, patient in enumerate(db):
        print("Patient {} is in room {}".format(patient[0], room_numbers[i]))
    for patient, rn in zip(db, room_numbers): #look into zip function
        print("Patient {} is in room {}".format(patient[0], rn))

def get_patient_entry(db, mrn_to_find):
    for patient in db:
        if patient[1] == mrn_to_find:
            return patient
    return False

def add_test_to_patient(db, mrn_to_find, test_name, test_value):
    patient = get_patient_entry(db, mrn_to_find)
    if patient == False:
        print("Bad entry")
    else:
        patient[3].append([test_name, test_value])
    return 

# def get_test_result(db, mrn)
    #receive medical record number 2 and  test name LDL, return test value

def get_test_value(tests_list, test_name):
    for test in tests_list:
        if test[0]==test_name:
            test_value= test[1]
    return test_value

def get_test_result(db, mrn, test_name):
    patient = get_patient_entry(db, mrn)
    test_result = get_test_value(patient[3], test_name)
    return test_result


if __name__ == "__main__":
    main_driver()