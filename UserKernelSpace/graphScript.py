import pandas as pd
import matplotlib.pyplot as plt
import sys

def readIn(userfile, kernelfile):
    try: 
        with open(userfile) as f:
            userlines = f.readlines()
        userlines = [int(line) for line in userlines]

        with open(kernelfile) as f:
            kernellines = f.readlines()
        kernellines = [int(line) for line in kernellines]

        return userlines, kernellines
    except Exception as e:
        print("failed to read file ", e)

def plot(userdata, kerneldata):
    plt.plot(userdata, marker='o', color="#33B", label="user space")
    plt.plot(kerneldata, marker='o', color="#B33", label="kernel space")

    title_string = "CPU0 Time spent in User space vs Kernel space"

    plt.title(title_string)
    plt.xlabel('', fontsize=14)
    plt.ylabel('Time',fontsize=14)
    plt.grid(True)

    plt.legend(fontsize=14)

    save_fig = './graph-image-script.png'
    print("drawing")
    plt.savefig(save_fig)

    plt.show()

def main():
    print("hello")
    user = str(sys.argv[1])
    kernel = str(sys.argv[2])
    plt.ion
    while True:
        userdata, kerneldata = readIn(user, kernel)
        plot(userdata, kerneldata)

main()
