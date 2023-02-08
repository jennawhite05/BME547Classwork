
# functions should only do one thing, no ands or thens
def diagnosisinput():
    print("Day One Dosing Guidelines")
    print("")
    print("Choose diagnosis")
    print("1 - Acute otitis media")
    print("2 - Acute bacterial sinusitis")
    print("3 - Community-acquired pneumonia")
    print("4 - Pharyngitis/tonsilitis")
    diagnosis = int(input("Enter a number: "))
    return diagnosis


def weightinput():
    print("PATIENT WEIGHT")
    print("Enter patient weight followed by units of kg of lb.")
    print("Examples: 63.5 lb         21.0 kg")
    weight_input = input("Enter weight: ")
    return weight_input


def parsingweight(weight_input):
    weight_data = weight_input.split(" ")
    weight = float(weight_data[0])
    units = weight_data[1]
    if units == "lb":
        weight = weight/2.505
    return weight


def calculatingdosage(diagnosis, weight):
    dosages_mg_per_kg = [30, 10, 10, 12]
    dosage_mg_per_kg = dosages_mg_per_kg[diagnosis-1]
    dosage_mg_first_day = weight * dosage_mg_per_kg
    return dosage_mg_first_day


def dosageoutput(weight, dosage_mg_first_day):
    print("CORRECT DOSAGE")
    print("For a patient weighing {:.1f} kg,".format(weight))
    print(" the correct dosage is {:.1f} mg the first day"
          .format(dosage_mg_first_day))


if __name__ == '__main__':
    diagnosis = diagnosisinput()
    weightin = weightinput()
    weight = parsingweight(weightin)
    firstdaydose = calculatingdosage(diagnosis, weight)
    dosageoutput(weight, firstdaydose)
