print ("WElCOME TO THE PRUDENT HEALTH CARE CENTER")

file = "dic.txt"


def register(patient_id, first_name, last_name, address, gender, contact, patient_age):
    fw = open('dic.txt', "a")
    fw.write("%1s%20s%20s%20s%20s%20s%20s\n" % (patient_id, first_name, last_name, address, gender, contact, patient_age))
    fw.close()




textfile = "payment.txt"
def cost(invoice_id, treatment_id, Bill_amount):
    fw = open('payment.txt', "w")
    fw.write("%1s%20s%15s\n" % (invoice_id, treatment_id, Bill_amount))
    fw.close()



def payment():

    print ("welcome to payment process")
    print ("press enter to continue the payment process")
    invoice_id = raw_input("please enter your invoice id:")
    print (invoice_id)
    Bill_amount = raw_input(" Please enter bill amount:")
    print (Bill_amount)
    treatment_id =raw_input(" Please enter treatment id:")
    print (treatment_id)
    cost(invoice_id, treatment_id, Bill_amount )
    print("Thank you")




def st():
    users = open("payment.txt", 'r')
    extract = raw_input("Please input patient ID:")
    for each_line in users:
        (invoice_id, treatment_id, Bill_amount) = each_line.split()

    if (invoice_id == extract):
        print(invoice_id, treatment_id, Bill_amount)
    else:
        print ("error")


def registration():
    patient_id = raw_input("Enter patient_id:")
    print (patient_id)
    first_name =raw_input("Enter your first_name:")
    print (first_name)
    last_name = raw_input("Enter your last name:")
    print (last_name)
    address = raw_input("Enter your address:")
    print (address)
    gender = raw_input("Enter your gender: ")
    print (gender)
    contact = raw_input("Enter your contact number:")
    print (contact)
    patient_age = raw_input("date of birth:")
    print (patient_age)
    register(patient_id, first_name, last_name, address, gender, contact, patient_age)
    print("THANK YOU!!!")
    print("\nUser created!\n")


file = "appointment.txt"



def writes(appointment_id, select_doctor, doctor_time, status):
    fw = open('appointment.txt', "a")
    fw.write("%1s%20s%20s%10s\n" % (appointment_id, select_doctor, doctor_time,  status))
    fw.close()



def appointment():
    print("Book an appointment")
    appointment_id=raw_input("enter appointment id:")
    print (appointment_id)
    select_doctor = raw_input("enter name of Doctor:")
    print (select_doctor)
    doctor_time= raw_input("Select  appointment time")
    status = raw_input("enter status:")
    print (status)
    writes(appointment_id, select_doctor, doctor_time, status)


def history(treatment_id, complaint, treatment):
    fw = open('treatment.txt', "a")
    fw.write("%1s%20s%20s\n" % (treatment_id, complaint, treatment))
    fw.close()


def treatment():
    print ("press enter to start a patient treatment plan")
    treatment_id = raw_input("enter the treatement id:")
    print (treatment_id)
    complaint =raw_input("enter the complaint of patient:")
    print (complaint)
    treatment =raw_input(" write a treatment detail of a patient:")
    print (treatment)
    history(treatment_id, complaint, treatment)
    print ("patient treatment record have been saved")
    print ("Thank you for your treatment")



def users():
    print("Login Page")
    status = ""

while True:
    print("Are you \n1.Physician\n2.Accountant")
    status = raw_input("User")

    if status =="1":
        login =raw_input("enter your username:")
        password =raw_input("enter your password:")


        if (login, password) == ("a","a"):
            print ("welcome for process,you are physician")
        else:
            print("error")


        while True:
            users=raw_input("1.registration\n2.appointment\n3.treatment\n4.exist")
            if users=="1":
                registration()

            elif users=="2":
                appointment()


            elif users=="3":
                treatment()


            elif users == "4":
                exit()

            break

        else:
            print("wrong choice")

    elif status == "2":

        login = raw_input("enter your username:")
        password = raw_input("enter your password:")
        if (login, password) == ("a","a"):
            print ("welcome for process,you are Accountant")
        else:
            print("error")
        while True:
            users = raw_input("1.Invoicing\n2.Search patient\n3.exist")

            if users == "1":
                payment()


            elif users =="2":

                st()

                print ("Search the  payment detail of the patient")




            elif users == "2":
                print ("Quite")
                break


