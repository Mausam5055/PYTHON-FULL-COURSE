# ---------FORMAT METHOD (STRINGS)-------

# Formats the values inside the string into a desired output.
# template.format(p1,p2...)

# Syntax:
# "{} is a good {}".format("harry", "boy") #1.
# "{} is a good {o}".format("harry", "boy") #2.
# # output for 1: harry is a good boy 
# # output for 2: boy is a good harry

a = "{0} is a good {1}".format("harry","boy")
print(a)

#in the 1st bracket we will get harry and in the second bracket we
#will get boy as an output

#but if we want "boy" in the 1st bracket and "harry " in the second 
#then we write the above copde as:

a = "{1} is a good {0}".format("harry","boy")
print(a)