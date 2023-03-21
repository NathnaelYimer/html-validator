"""
                                                HTML Validator 
                                    Section 1
       Group Members
Amanuel Yihune - UGR/8408/13
Surafel Workayehu - UGR/9701/13
Nathnael Yimer - UGR/6855/13
Yonas Engdu - UGR/4575/13
Yohannes Desta - UGR/1364/13
Abdi Firomsa - UGR/8420/13

"""

class Stack:

    def __init__(self):
        self.list=[]
    
    def pop(self):
        return self.list.pop()
    
    def push(self,data):
        self.list.append(data)
    
    def peek(self):
        return self.list[-1]
    
    def length(self):
        return len(self.list)
    
    def isEmpty(self):
        if len(self.list):
            return False
        else:
            return True

def isValid(filePath):
    try:
        file = open(filePath, "r")
    except:
        print("please enter a valid file path with extension")
    emptyElements = ["area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr"]
    flagForOpening = False
    flagForClosing = False
    flag = False
    openingTag = ""
    closingTag=""
    container = Stack()
    for lineNum,lineContent in enumerate(file):
        for char in lineContent:
            if char == "<":
                flag = True
                flagForOpening = True
            elif char =="/" and flag:
                flagForOpening = False
                flagForClosing = True
            elif (char ==">" or char==" ") and flag:
                if flagForOpening:
                    if openingTag not in emptyElements:
                        container.push(openingTag+str(lineNum+1))
                    openingTag = ""
                    flagForOpening = False
                elif flagForClosing:
                    if container.peek()[:-1] == closingTag:
                        container.pop()
                        closingTag=""
                        flagForClosing=False
                    else:
                        print("the opening tag <"+container.peek()[:-1]+"> at line number", container.peek()[-1], "isn't closed")
                        print("it's Invalid!")
                        return False
                    flagForClosing = False
            elif flagForOpening:
                openingTag = openingTag + char
            elif flagForClosing:
                closingTag = closingTag + char
    if container.isEmpty():
        print("Valid")
        return True


"""Bonus: official HTML5 specifications has 15 empty elements,
                if the user wants he/she can add more elements"""

