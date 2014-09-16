#Christopher Pullen
#16-9-14
#development exercise3 converting height in inches to centimetres and stones into kg

inch=float(input("please enter the lenght in inces that you wish to be converted into centimetres:"))
stones=float(input("now please enter the mass of the person in stones:"))
centimetres=(inch*2.54)
kilograms=(stones*6.364)
print("the height of this person in cm is {0} and the mass of this person in kg is {1}" .format(centimetres,kilograms))
