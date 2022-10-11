#!"E:\computer stuff\python\python.exe"

from imgShimmerGenerate import *
import cgi
import cgitb

cgitb.enable()

def transformToPrint(str):
	return "print(\"" + str + "\")\n"

originalTextFile = open("SpinningCowFramework.html", "r")
cgiText = ""
f = originalTextFile.readlines()
for x in f:
	cgiText += transformToPrint(x.rstrip().replace("\"", "\\\""))

ranArray = generateRandomIMGShimmer(200, 7).split('\n')
for line in ranArray:
	#print(line)
	cgiText += transformToPrint(line)
cgiText += 	transformToPrint("}")
firstColorString = "RGB(" + str(random.randint(0,255)) + ", " + str(random.randint(0,255)) + ", " + str(random.randint(0,255)) + ")"
secondColorString = "RGB(" + str(random.randint(0,255)) + ", " + str(random.randint(0,255)) + ", " + str(random.randint(0,255)) + ")"
cgiText += transformToPrint("@keyframes backgroundColorChange{0%{background-color: " + firstColorString + "}") + transformToPrint("50%{background-color: " + secondColorString + "}") + transformToPrint("100%{backgroundcolor: " + firstColorString + "}") + transformToPrint("}")

cgiText += transformToPrint("</style></head><body><a href=\\\"http://www.starrandco.zenfolio.com\\\"><img src=\\\"hiCows.jpg\\\"></a></body></html>")
#################
print("Content-type: text/html\r\n\r")
print(cgiText)
#################


#print(cgiText.split("<!--")[0])
#print(cgiText.split("<!--")[1])
#print(cgiText.split("<!--")[2])

#cgiArray = cgiText.split("<!--sub-->")

# @keyframes backgroundColorChange{
	# 0%{background-color: #D5D2FD;}
	# 50%{background-color: #FAFDD2;}
	# 100%{background-color: #D5D2FD;}
# }

