import os
import sys
from itertools import permutations,product,combinations


class PasswordGenerator:
    def __init__(self):
        self.outputFile = ""
        self.digits = None
        self.enableCaseSensitivity = False
        self.enableSpecialCharacters = False
        self.inputFile = ""
        self.parameters = None
        self.passwords = []

    def generateUniquePasswords(self):
        if self.parameters != None:
            passwords = list(permutations(self.parameters))
        else:
            for line in open(self.inputFile, "r"):
                passwords = []
                passwords.append(line)
            for i in passwords:
                password = ""
                for j in i:
                    password += j
                    if password not in self.passwords:
                        self.passwords.append(password)

        if self.enableCaseSensitivity:
            for p in range(len(self.passwords)):
                perms = list(map(''.join, product(*zip(self.passwords[p].upper(), self.passwords[p].lower()))))
                for i in perms:
                    self.passwords.append(i)

        if self.enableNumbers:
            nums = [1,2,3,4,5,6,7,8,9,0]
            for p in range(len(self.passwords)):
                perms = list(permutations(nums,int(self.digits)))
                for i in perms:
                    passwd = self.passwords[p]
                    for j in i:
                        passwd += str(j)
                    self.passwords.append(passwd)
                    
        if self.outputFile != "":
            out = open(self.outputFile, "+w")
            for password in self.passwords:
                out.write(password + "\n")

    def getCommandLineArguments(self):
        for i, arg in enumerate(sys.argv):
            if i > 0 and i % 2 != 0: #odd
                match arg:
                    case "-p":
                        params = sys.argv[i + 1]
                        self.parameters = params.split(",")
                    case "-n":
                        self.enableNumbers = True
                        self.digits = sys.argv[i + 1]
                    case "-i":
                        self.inputFile = sys.argv[i + 1]
                    case "-c":
                        self.enableCaseSensitivity = True
                    case "-s":
                        self.enableSpecialCharacters = True
                    case "-o":
                        self.outputFile = sys.argv[i + 1]
                    case "-h":
                        print("This tool is designed to take many different parameters and create a password list")
                        print("-n <number>: permutate <number> digits appened on potential passwords")
                        print("-c <null>: permutate potential passwords with case sensitivity")
                        print("Usage: main.py [OPTION] -p joe,jack,cat -o <outputFile>")
                        break
                    case _:
                        print("use -h for help")
                        break

if __name__ == "__main__":
    passwordGen = PasswordGenerator()
    passwordGen.getCommandLineArguments()
    passwordGen.generateUniquePasswords()
