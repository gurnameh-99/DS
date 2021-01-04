
from sys import stdin

def checkRedundantBrackets(expression) :
    st = []  
  
    
    for ch in expression:  
        if (ch == ')'):  
            top = st[-1]  
            st.pop()  
   
            flag = True
  
            while (top != '('):  
    
                if (top == '+' or top == '-' or
                    top == '*' or top == '/'):  
                    flag = False
   
                top = st[-1]  
                st.pop() 
                
            if (flag == True): 
                return True
  
        else: 
            st.append(ch) 
    return False
            
#main
expression = stdin.readline().strip()

if checkRedundantBrackets(expression) :
	print("true")

else :
	print("false")
