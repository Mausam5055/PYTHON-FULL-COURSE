#           ---------MATCH CASE--------

# Python 3.10 introduced the match statement, which is similar to 
# the switch statement found in other programming languages. 

# The basic syntax of the match statement involves matching a 
# variable against several cases using the case keyword.

                # def http_status(status):
                # match status:
                # case 200:
                # return "OK"
                # case 404:
                # return "Not Found"
                # case 500:
                # return "Internal Server Error"
                # case _:
                # return "Unknown status"
                # # Usage
# print(http_status(200)) # Output: OK
# print(http_status(404)) # Output: Not Found
# print(http_status(500)) # Output: Internal Server Error
# print(http_status(403)) # Output: Unknown status


def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
             return "Not Found"
        case 500:
             return "Internal Server Error"
        case _:
               return "Unknown status"
         
# # Usage
print(http_status(200)) # Output: OK
# print(http_status(404)) # Output: Not Found
# print(http_status(500)) # Output: Internal Server Error
# print(http_status(403)) # Output: Unknown status

# see all the "print" statements above by commenting out one by one