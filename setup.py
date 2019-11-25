"""=================================================
            Setup file for Git Automatter 
================================================="""

# Import Statements
import os


# Print Welcome message
print("""
Welcome to Git Automatter Setup
This file will install Git Automatter in your machine and let you use the program as terminal command
""")


# Setup Method
def setup():

    # Make Git automatter file as executable
    print("Giving execute permision to user...")
    os.system('chmod +x gitter')
    print("Permisson granted successfully...\n")

    # Move the log file to /bin
    print("Adding 'gitter' command to your terminal...")
    os.system('sudo cp gitter /bin')
    print("Command added successfully...\n")
    

    # Printing Get Started message
    print("""
    Hurray...! The installation was completed successfully :)
    Close this Installation window and open a new one to use Git Automatter

    Run 'gitter --help' to read the user manual.
    """)

# Print conformation prompt
choice = input("Do you want to continue? [Y/n]")

# Decission making for the choice
if (choice == "Y" or choice == "Yes" or choice == "YES" or choice == "" or choice == "y"):

    # Call the setup function
    setup()

else:

    # Print Abort and exit the program
    print("Abort.")