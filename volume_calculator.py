shape = input("What shape should we calculate the volume of? (Sphere, Cylinder, Triangular Prism, Rectangular Prism, Cube: ")

if shape == "Sphere":
	radiusS = input("What is the sphere's radius?: ")
	partOf = input("What part of the total volume would you want me to calculate?: ")
	VolumeS = 4 / 3 * 3.14 * radiusS * radiusS * radiusS * partOf
	print("The " +str(shape) + "'s volume is " + str(VolumeS))

if shape == "Cylinder":
	radiusC = input("What is the radius of the base?: ")
	heightC = input("What is the height of the cylinder?: ")
	partOf = input("What part of the total volume would you want me to calculate?: ")
	VolumeC = 3.14 * radiusC * radiusC * heightC * partOf
	print("The " +str(shape) + "'s volume is " + str(VolumeC))

if shape == "Triangular Prism":
	baseLength = input("What is the length of the base side?: ")
	baseHeight = input("What is the height of the base?: ")
	shapeHeight = input("What is the height of the shape ")
	partOf = input("What part of the total volume would you want me to calculate?: ")
	VolumeTP = baseLength * baseHeight / 2 * shapeHeight * partOf
	print("The " +str(shape) + "'s volume is " + str(VolumeTP))
