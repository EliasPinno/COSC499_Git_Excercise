# Primary entry point for the application

def getListFromInput(strInput) -> list:
    arr = strInput
    l = list(map(int,strInput.split(' '))) 
    return(l)

def sortList(l) -> list:
    return sorted(l)

def sortListReversed(l) -> list:
    return sorted(l, reverse=True)

if __name__ =="__main__":
    print("Enter your array: with each value seperated by spaces.")
    strInput = input()
    l = getListFromInput(strInput)
    # Sort forward
    lSorted = sortList(l)
    print(lSorted)
    # Sort backward
    lSortedReverse = sortListReversed(l)
    print(lSortedReverse)
    



