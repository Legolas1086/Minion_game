

def minion_game(string):
    # initiallising 2 variables to keep track of points
    k=0
    s=0

    #defining vowels
    vowels="AaEeIiOoUu"


    for i in range(len(string)):
        #checking if the character is vowel or consonents one by one
        if string[i] in vowels:
            #look at Readme file for explanation
            k=k+len(string)-i
        else:
            #look at readme file for explanation
            s=s+len(string)-i 
               
    #checking the winner
    if k>s:
        print("Kevin",k)
    elif k==s:
        print("Draw")    
    else:
        print("Stuart",s)            


if __name__ == '__main__':
    s = input()
    minion_game(s)