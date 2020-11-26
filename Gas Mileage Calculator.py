# To make a gas mileage calculator, print out to screen
# ask user for distance (in mileage), and gas (in gallons)
# execute calculation for gas mileage (gas/distance)
# display calc onscreen

# def MilesPerGallonCalculator():
#     try: 
#         mileage = int(input("How many miles did you travel?"))
#     except:
#         print ("Only the number of miles will do")
#         MilesPerGallonCalculator()
#     try:
#         gas = int(input("And how gallons of gas did you use?"))
#     except:
#         print ("Only the number of miles will do")
#         MilesPerGallonCalculator()
#     mpg = mileage/gas
#     print(f'Your averaging {mpg} miles per gallon')
#     print(f'The type for mileage is {mpg}')
# MilesPerGallonCalculator()

def GPMInput():
    mileage = (input("How many miles did you travel?"))
    gas = (input("And how gallons of gas did you use?"))
    return [mileage, gas]

MileageGas = GPMInput()
NumberOfGPMInputValues = len(MileageGas)
gas = MileageGas[1]
mileage = MileageGas[0]

GPM = mileage/gas
print(GPM)
print (NumberOfGPMInputValues)
