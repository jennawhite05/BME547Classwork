def create_patient_entry(first_name, last_name, patient_mrn, patient_age):
    # new_patient = [patient_name, patient_mrn, patient_age, []]
    new_patient = {"First Name": first_name,
                   "Last Name": last_name,
                   "Patient MRN": patient_mrn,
                   "Patient Age": patient_age, "Tests": []}
    return new_patient


def main_driver():
    db = {}
    db[1] = (create_patient_entry("Ann", "Ables", 1, 34))
    db[2] = (create_patient_entry("Bob", "Boyles", 2, 45))
    db[3] = (create_patient_entry("Chris", "Chou", 3, 52))
    print(db)
    full_name = get_full_name(db[1])
    print(full_name)
    print_database(db)
    add_test_to_patient(db, 1, "HDL", 120)
    add_test_to_patient(db, 2, "LDL", 99)
    add_test_to_patient(db, 2, "HDL", 100)
    add_test_to_patient(db, 3, 'HDL', 117)
    room_numbers = ["103", "232", "333"]
    print(db)
    print_directory(db, room_numbers)
    testresult = get_test_result(db, 2, 'HDL')
    print(testresult)


def get_full_name(patient):
    full_name = patient['First Name'] + " " + patient['Last Name']
    return full_name


def print_database(db):
    for patient in db.values():
        mrn = patient['Patient MRN']
        full_name = get_full_name(patient)
        age = patient['Patient Age']
        print("MRN: {}, Full Name: {}, Age: {}".format(mrn, full_name, age))


def print_directory(db, room_numbers):
    for i, patient in enumerate(db.values()):
        print("Patient {} is in room {}"
              .format(get_full_name(patient), room_numbers[i]))
    # for patient, rn in zip(db, room_numbers):  # look into zip function
    #     print("Patient {} is in room {}".format(get_full_name(patient), rn))


def get_patient_entry(db, mrn_to_find):
    patient = db.get(mrn_to_find)
    if patient is None:
        return False
    return patient


def add_test_to_patient(db, mrn_to_find, test_name, test_value):
    patient = get_patient_entry(db, mrn_to_find)
    if patient is False:
        print("Bad entry")
    else:
        patient['Tests'].append([test_name, test_value])
    return

# def get_test_result(db, mrn)
    # receive medical record number 2 and  test name LDL, return test value


def get_test_value(tests_list, test_name):
    for test in tests_list:
        if test[0] == test_name:
            test_value = test[1]
    return test_value


def get_test_result(db, mrn, test_name):
    patient = get_patient_entry(db, mrn)
    test_result = get_test_value(patient['Tests'], test_name)
    return test_result


if __name__ == "__main__":
    main_driver()
