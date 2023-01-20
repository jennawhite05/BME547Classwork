def interface():
    print("Blood calculator:")
    keep_running = True
    while keep_running:
        print("Options:")
        print("1-HDL")
        print("5-LDL")
        print("7-Cholesterol")
        print("9-Quit")
        choice = input("Select an option:")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            HDL_driver()
        elif choice == "5":
            LDL_driver()
        elif choice == "7":
            Cholesterol_driver()
    print("Program ending")

def Cholesterol_driver():
    Cholesterol_in = Cholesterol_input()
    Cholesterol_analy = Cholesterol_analysis(Cholesterol_in)
    Cholesterol_output(Cholesterol_in, Cholesterol_analy)

def Cholesterol_input():
    Cholesterol_value = input("Enter the Total Cholesterol result:")
    Cholesterol_value = int(Cholesterol_value)
    return Cholesterol_value

def Cholesterol_analysis(Cholesterol_int):
    if Cholesterol_int < 200:
        answer = "Normal"
    elif 200 <= Cholesterol_int <=239:
        answer = "Borderline High"
    else:
        answer = "High"
    return answer

def Cholesterol_output(Cholesterol_value, Cholesterol_analy):
    print("The Total Cholesterol result of {} is considered {}".format(Cholesterol_value, Cholesterol_analy))
    return

def LDL_driver():
    LDL_in = LDL_input()
    LDL_analy = LDL_analysis(LDL_in)
    LDL_output(LDL_in, LDL_analy)

def LDL_input():
    LDL_value = input("Enter the LDL result:")
    LDL_value = int(LDL_value)
    return LDL_value

def LDL_analysis(LDL_int):
    if LDL_int < 130:
        answer = "Normal"
    elif 130 <= LDL_int <= 159:
        answer = "Borderline High"
    elif 160 <= LDL_int <= 189:
        answer = "High"
    else:
        answer = "Very High"
    return answer

def LDL_output(LDL_value, LDL_analy):
    print("The LDL result of {} is considered {}".format(LDL_value, LDL_analy))
    return

def HDL_driver():
    HDL_in = HDL_input()
    HDL_analy = HDL_analysis(HDL_in)
    HDL_output(HDL_in, HDL_analy)

def HDL_input():
    HDL_value = input("Enter the HDL result:")
    HDL_value = int(HDL_value)
    return HDL_value

def HDL_analysis(HDL_int):
    if HDL_int >= 60:
        answer = "Normal"
    elif 40 <= HDL_int < 60:
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer

def HDL_output(HDL_value, HDL_analy):
    print("The HDL result of {} is considered {}".format(HDL_value, HDL_analy))
    return

interface()