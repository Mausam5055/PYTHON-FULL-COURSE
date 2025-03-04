# 3. Write a program to generate multiplication tables from 2 to 20 and 
# write it to the different files. Place these files in a folder for a 
# 13 – year old.


def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"
    
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)




for i in range(2, 21):
    generateTable(i)


    #as soon as we run this code 20 files will be created automatically
    #inside the tables folder which will contan the tables
    