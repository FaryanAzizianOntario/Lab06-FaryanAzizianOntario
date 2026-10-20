# Part 1 - a menu-driven text interface (TUI) for a simple "piggy bank".
#
# This is a terminal program: it shows a menu, reads a choice, does something, and
# loops until the user quits. The menu loop is written for you - fill in the three
# TODO branches. Keep the exact wording shown (the tests look for it).

def main():
    balance = 0.0

    while True:
        print("1) Deposit")
        print("2) Withdraw")
        print("3) Balance")
        print("4) Quit")
        choice = input("\nChoice: ").strip()

        # if choice == "1":
        #     inp = float(input("Amount: "))
        #     balance += inp
        #     print(f"\nNew balance: {balance:.2f}\n")

        # elif choice == "2":
        #     inp = float(input("Amount: "))

        #     if(inp > balance):
        #         print("\nInsufficient funds\n")

        #     else:
        #         balance -= inp
        #         print(f"\nNew balance: {balance:.2f}\n")

        # elif choice == "3":
        #     print(f"\nCurrent balance: {balance:.2f}\n")

        # elif choice == "4":
        #     print("Goodbye")
        #     break

        # else:
        #     print("\nInvalid choice\n")

        match choice:
            case "1":
                inp = float(input("Amount: "))
                balance += inp
                print(f"\nNew balance: {balance:.2f}\n")

            case "2":
                inp = float(input("Amount: "))
                
                if(inp > balance):
                    print("\nInsufficient funds\n")
                
                else:
                    balance -= inp
                    print(f"\nNew balance: {balance:.2f}\n")

            case "3":
                print(f"\nCurrent balance: {balance:.2f}\n")

            case "4":
                print("Goodbye")
                break

            case _:
                print("\nInvalid choice\n")




if __name__ == "__main__":
    main()
