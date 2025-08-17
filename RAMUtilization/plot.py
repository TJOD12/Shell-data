import matplotlib.pyplot as plt
import sys

"""readLines

Read the data written by the shell script and then call plot

arguments:
    totalFile (str): File containing the total RAM memory (only written to 1 line)
    usedFile (str): File containing the RAM being used each 2 second interval
"""
def readLines(totalFile, usedFile):
    try: 
        with open(usedFile) as f:
            lines = f.readlines()
        print("lines:",lines)
        usedList = [int(line) for line in lines]

        with open(totalFile) as f:
            line = f.readline()
        print("total: ", line)
        total = int(line)

        plot(usedList, total)
    except Exception as e:
        print("Error opening file: %s " % e)

"""plot

Plot the graph

arguments:
    usedData (int[]): List of used RAM recorded by shell script
    totalData (int): Total RAM recorded by shell script
"""
def plot(usedData, totalData):
    plt.plot(usedData, marker='o', color="#33B", label="used RAM")
    plt.plot(totalData, marker='o', color="#B33", label="total RAM")

    title_string = "Comparison of total RAM to RAM in use at 2 second intervals"

    plt.title(title_string)
    plt.xlabel('', fontsize=14)
    plt.ylabel('Time',fontsize=14)
    plt.grid(True)

    plt.legend(fontsize=14)

    save_fig = './graph-free-script.png'
    print("drawing")
    plt.savefig(save_fig)

    plt.show()

"""main
Parse the arguments passed by the shell script and pass them to readlines

"""
def main():
    total = str(sys.argv[1])
    used = str(sys.argv[2])
    readLines(total, used)

main()



