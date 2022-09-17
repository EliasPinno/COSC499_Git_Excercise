# Primary entry point for the application

def getListFromInput(strInput) -> list:
    arr = strInput
    l = list(map(int,strInput.split(' '))) 
    return(l)

if __name__ =="__main__":
    print("Enter your array, with each value seperated by spaces.")
    strInput = input()
    getListFromInput(strInput)

