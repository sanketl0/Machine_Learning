import os
import fnmatch
from sys import *
import xlsxwriter

def excelcreater(name):
    workbook = xlsxwriter.Workbook(name)

    worksheet = workbook.add_chartsheet()

    workbook.write('A1','Name')
    workbook.write('B1','College')
    workbook.write('C1','Mail Id')
    workbook.write('D1','Mobile')

    workbook.close()


def main():
    print("marvellous infosystem")

    print("Application name :"+argv[0])

    if len(argv) !=2:
        print("error:invalid number of arguments")
        exit()

    if (argv[1]=="-h") or (argv[1]== "-H"):
        print("This script is used to create excel file write data into it")
        exit()

    if(argv[1]=="-u") or (argv[1]=="-U"):
        print("usages: Applicationname name of file")
        exit()

    try:
        excelcreater(argv[1])

    except Exception:
        print("Error : Invalid path")

if __name__ =="__main__":
    main()
    