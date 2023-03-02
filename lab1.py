import requests

url = input('Write here a URL: ')

try:
    with requests.get(url) as response:
        print("\n1) All Response Headers\n")
        y = 1
        for header in response.headers:
            print(f"{y}. " + header + " : " + response.headers[header])
            y+=1

        print("\n2) Other Questions\n")

        if "Server" in response.headers:
            print("2.a) The software used by the web server is: " + response.headers["Server"] + "\n")
        else:
            print("2.a) Can't find the software used by the web server\n")
    
        if "Set-Cookie" in response.headers:
            print("2.b) The website uses cookies\n")
            print("2.c) Here are the names of the Cookies and their Expring Dates:\n")
           
            mylist = response.headers["Set-Cookie"].split(",")

            # Με την προηγούμενη εντολή χωρίσαμε το περιεχόμενο κείμενο της κεφαλίδας Set-Cookie σε λίστα,
            # όπου τα στοιχεία της χωρίζονται με τον χαρακτήρα ','. Έτσι, όπως φαίνεται και στον κώδικα παρακάτω,
            # στα ζυγά στοιχεία της λίστας περιέχονται τα ονόματα των Cookies ενώ στα μονά οι ημερομηνίες λήξης τους.
            # Το τελευταίο if είναι διορθωτικό, ώστε σε περίπτωση που κάποιο Cookie δεν έχει ημερομηνία λήξης, να μην
            # χαλάει η σειρά.

            i = 0
            for element in mylist:
                element = element.strip()
                if i % 2 == 0:
                    print("Name: " + element[0:element.find("=")])
                if i % 2 == 1:
                    print("Expiring Date: " + element[0:element.find(";")] + "\n")
                if i % 2 == 0 and "Expires" not in element and "expires" not in element:
                    i+=1
                    print("Expiring Date: unknown\n")
                i+=1
        else:
            print("2.b) The website does not use cookies\n")
except:
    print("\nSomething went wrong.\n")