def read_file(filename):
    in_file = open(filename, "r")
    first_line = in_file.readline()
    patient_data = first_line.strip("\n").split("=")
    patient_id = int(patient_data[1])
    in_file.close()
    return patient_id


def test_read_file():
    # from module import read_file
    filename = "my_test_data.txt"
    answer = read_file(filename)
    expected = 50
    assert answer == expected
