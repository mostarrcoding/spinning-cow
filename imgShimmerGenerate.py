import sys
import random

def generateIMGShimmer(mod, radii, colors):
	for x in range(101):
		for y in range(int(mod)+1):
			if x%int(mod) == y:
				# print(radii)
				# print(colors)
				print(str(x) + "%{box-shadow: 0px 0px " + str(radii.split(',')[y]) + "px " + str(colors.split(',')[y]) + ";}")
				
def generateRandomIMGShimmer(maxRadius, numColors):
	dataStrings = []
	for x in range(int(numColors)):
		dataStrings.append(str(random.randint(1, int(maxRadius))) + "px RGBA(" + str(random.randint(0,255)) + ", " + str(random.randint(0,255)) + ", " + str(random.randint(0,255)) + ", " + str(random.random()))
	returnString = ""
	for x in range(101):
		for y in range(int(numColors)+1):
			if x%int(numColors) == y:
				returnString += str(x) + "%{box-shadow: 0px 0px "  + dataStrings[y] + ");}\n"
	#print(returnString)
	return returnString

def main():
	#generateIMGShimmer(sys.argv[1], sys.argv[2], sys.argv[3])
	generateRandomIMGShimmer(sys.argv[1], sys.argv[2])
			
if __name__ == "__main__": main()

################################################################
# if x%4 == 0:
	# print(str(x) + "%{box-shadow: 0px 0px 1px black;}")
# elif x%4 == 1:
	# print(str(x) + "%{box-shadow: 0px 0px 5px red;}")
# elif x%4 == 2:
	# print(str(x) + "%{box-shadow: 0px 0px 10px green;}")
# elif x%4 == 3:
	# print(str(x) + "%{box-shadow: 0px 0px 20px yellow;}")