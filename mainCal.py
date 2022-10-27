def addition():
    add1 = input('Nbrs 1: ')
    add2 = input('Nbrs 2: ')

    sum = float(add1) + float(add2)

    print("l'addition :",add1,"+",add2,"=",sum)

def soustraction():
    sous1 = input('Nbrs 1: ')
    sous2 = input('Nbrs 2: ')

    sous = float(sous1) - float(sous2)

    print("la soustraction :",sous1,"-",sous2,"=",sous)

def mutiplication():
    multi1 = input('Nbrs 1: ')
    multi2 = input('Nbrs 2: ')

    multi = float(multi1) * float(multi2)

    print("la mutiplication :",multi1,"X",multi2,"=",multi)

def division():
    div1 = input('Nbrs 1: ')
    div2 = input('Nbrs 2: ')

    div = float(div1) / float(div2)

    print("la division :",div1,"/",div2,"=",div)

def menu():
    print("Quel operation ?")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("q. Exit")

   

def app(choix):
    if choix == "1":
        addition()
    elif choix == "2":
        soustraction()
    elif choix == "3":
        mutiplication()
    elif choix == "4":
        division()
    elif choix == "q":
        return
    else:
        print("pas bon")

def main(): 
    menu()
    app(choix = input("Quel operation ?"))

if __name__ == '__main__':
    main()