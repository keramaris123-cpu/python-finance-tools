print(" ===Παρακολούθηση Εσόδων-Εξόδων=== ")

import json

FILENAME="expenses.json"

def load_expenses(filename=FILENAME):
    try:
        with open(filename,"r",encoding="utf-8") as file:
            data=json.load(file)
            print("Τα έξοδα σου φορτώθηκαν επιτυχώς!")
            return data
    except FileNotFoundError:
        print("Δε βρέθηκε το νέο αρχείο. Ξεκινάμε με νέα έξοδα.")
        return{}

def save_expenses(expenses_dict,filename=FILENAME):
    try:
        with open(filename,"w",encoding="utf-8") as file:
            json.dump(expenses_dict,file,indent=4,ensure_ascii=False)
            print("Οι αλλαγές αποθηκεύτηκαν επιτυχώς.")
    except Exception as e:
        print(f"Σφάλμα κατά την αποθήκευση: {e}")

def add_expense(expenses_dict,category,amount):
    if category in expenses_dict:
        expenses_dict[category]+=amount
    else:
        expenses_dict[category]=amount
    
    print(f"Προστέθηκαν {amount:.2f}€ στη κατηγορία {category}. ")
    save_expenses(expenses_dict)

def delete_expenses(expenses_dict,category):
    if category in expenses_dict:
        del expenses_dict[category]
        print (f"Η κατηγορία {category} διαγράφηκε επιτυχώς. ")
    else:
        print("Η κατηγορία δεν βρέθηκε. ")
    save_expenses(expenses_dict)

def get_total_expenses(expenses_dict):
    return sum(expenses_dict.values())

def subtract_amount(expenses_dict,category,amount):
    if category in expenses_dict:
        expenses_dict[category] -= amount
        if expenses_dict[category]<=0:
            del expenses_dict[category]
            print(f"Η κατηγορία {category} μηδενίστηκε και αφαιρέθηκε.")
            
        else:
            print(f"Αφαιρέθηκαν {amount:.2f} από τη κατηγορία {category}. Νέο υπόλοιπο: {expenses_dict[category]:.2f}€. ")
        save_expenses(expenses_dict)
    else:
        print(f"Η κατηγορία {category} δε βρέθηκε.")

expenses=load_expenses()

while True:
    print()
    print("1. Προσθήκη Εξόδου: ")
    print("2. Προβολή Εξόδων: ")
    print("3. Αναίρεση Εξόδων: ")
    print("4. Έξοδος απόν τη συνομιλία: ")

    try:
        choice=int(input("Επίλεξε έναν αριθμό (1-4). "))
    except ValueError:
        print("Μη έγκυρη καταχώρηση, παρακαλώ δώσε έναν αριθμό από το 1 εώς 4. ")
    
    if choice == 1:
        cat=input("Δώσε το όνομα της κατηγορίας: ")
        try:
            amt=float(input("Δώσε το ποσό (€): "))
            if amt<=0:
                print("Το ποσό πρέπει να είναι μεγαλύτερο απο 0! ")
            else:
                add_expense(expenses,cat,amt)
        except ValueError:
            print("Παρακαλώ δώσε έγκυρο αριθμό! ")

    elif choice == 2:
        print("== Τα έξοδα σου ==")
        if len(expenses)==0:
            print("Δεν έχεις Έξοδα! ")
        else:
            for cat,amt in expenses.items():
                print(f"*{cat}: {amt:.2f}€ ")

            total_sum=get_total_expenses(expenses)
            print("-------------")
            print(f"Τα συνολικά σας έξοδα είναι {total_sum:.2f}€ ")

    elif choice == 3:
        if len(expenses)<=0:
            print("Δεν υπάρχουν Έξοδα! ")
        else:
            cat_delete=input("Από ποια κατηγορία θέλεις να αφαιρέσεις το ποσό; ")
            if cat_delete in expenses:
                try:
                    amt=float(input("Ποιό είναι το ποσό που θέλεις να αφαιρέσεις; "))
                    if amt<=0:
                        print("Το ποσό πρέπει να είναι μεγγαλύτερο από 0.")
                    else:
                        subtract_amount(expenses,cat_delete,amt)
                except ValueError:
                    print("Παρακαλώ δώσε έγκυρο αριθμό.")
    elif choice == 4:
        print("Αντίο καλή συνέχεια!")
        break
    else :
        print("Μη έγκυρη επιλογή, προσπαθήστε ξανά.")



















