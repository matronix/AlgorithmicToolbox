# Uses python3
import sys

def get_change(m):
    #write your code here
    runningTotal = 0
    denominationTotal = 0
    denominationList=[1, 5, 10]
    coinCtr=0
    while m-runningTotal > 0 :
        try:
            currentDenomination = denominationList.pop()
        except IndexError:
            return coinCtr
        denominationTotal=0
        while denominationTotal<= m-runningTotal:
            if denominationTotal+currentDenomination >m-runningTotal:
                break
            else:
                coinCtr += 1
                denominationTotal += currentDenomination
            #print("Denomination Total:%i\n"%(denominationTotal))
        runningTotal = runningTotal+denominationTotal
        #print("Running Total:%i\n"%(runningTotal))
    return coinCtr


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
