# ----------TRY WITH FINALLY-------

# Python offers a ‘finally’ clause which ensures execution of a piece of 
# code inspective of the exception.
#                 try:
#                       # Some Code
#                 except:
#                       # Some Code
#                 finally:
#                       # Some Code # Executed regardless of error!


def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

        
    except Exception as e:
        print(e) 
        return


    finally:
        print("Hey I am inside of finally")


main()

#the code isnide "finally" clause will always run 
#even if the input is invalid or valid it doesnt 
#matter ....

#NOTES: the 'finally' clause is always wriiten inside a "function"
#in above the "finally" clause is written inside def main() function.