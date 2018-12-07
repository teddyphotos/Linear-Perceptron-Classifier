# This is a Classifier. Given a data set it will predict the label

# Imports
import random
import csv

# Take inputs
DataFileName = ""
inputs = []
labels = []


data = list(zip(inputs, labels))
# print(data)

# Now a function will create random weights and bias that will divide the plane
# For now I'm deciding the weights and bias
# Later we'll set this to random.randrange(some number)
weight1 = random.randrange(10)
weight2 = random.randrange(10)
bias = random.randrange(10)


def getweight1():
    return weight1


def getweight2():
    return weight2


def getbias():
    return bias


def setweight1(something):
    global weight1
    weight1 = something


def setweight2(something):
    global weight2
    weight2 = something


def setbias(something):
    global bias
    bias = something

# We will also define the learning rate here


lr = 0.1
# print("The initial equation of line was ", weight1, "x + ", weight2, "y + ", bias, " = 0")

# This line will divide the plane into  regions: Positive and Negative
# All the points where the equation of line gives a positive number lie in positive region
# All the points where the equation of line gives a negative number lie in negative region

# Next we have to define a classification criteria (Based on our data model)
# All points in positive region will be classified as 1
# All points in negative region will be classified as 0

# Now we have to make a function that will assign 0 or 1 to each point given its index
# This one will use the weights to assign


def assign(index):
    global weight1
    global weight2
    global bias
    w1 = weight1
    w2 = weight2
    b = bias
    x = inputs[index][0]
    y = inputs[index][1]
    calc = (w1*x)+(w2*y)+b
    if calc >= 0:
        # print("The assigned label was ", 1)
        return 1
    else:
        # print("The assigned label was ", 0)
        return 0

# We will also create a function that will also return its correct label


def tell(index):
    # print("The correct label is ", labels[index])
    return labels[index]

# Now we will create a function that will check if the assigned label matches the correct label
# It will take the index of the element, find its assigned value and then check the result
# It will return 1 or 0, which are represent to "Match" or "No Match"


def check(index1):
    assignedlabel = assign(index1)
    correctlabel = tell(index1)
    if assignedlabel == correctlabel:
        return True
    else:
        return False


# Next we need a function to modify weights and bias if the assigned label doesn't match correct label
# To do this, we first need some rules
# There can be 2 cases here
# Either a 1-labelled point(positive) is assigned 0(negative)
# Or a 0-labelled(negative) point is assigned 1(positive)

# For the 2nd Case:


def subtract(index):
    x = inputs[index][0]
    y = inputs[index][1]
    x = lr*x
    y = lr*y

    setweight1((getweight1() - x))
    setweight2((getweight2() - y))
    setbias((getbias() - lr*1))

# For the 1st Case:


def add(index):
    x = inputs[index][0]
    y = inputs[index][1]
    x = lr*x
    y = lr*y
    setweight1((getweight1() + x))
    setweight2((getweight2() + y))
    setbias((getbias() + lr*1))


# Now finally we need to run a loop over all the elements of the inputs list
# And for each unmatched element, we need to apply either case 1 or case 2 until that index
# is correctly classified


# It is case 1 if 1-labelled point is classified 0, i.e assign is 1
# It is case 2 if 0-labelled point is classified 1, i.e assign is 0

# We also need a variable that will tell if any changes were made to the weights
# This is needed because we need to be sure that previous points still satisfy the conditions when
# the weights change

def train():
    i = 0

    while i < len(inputs):
        if check(i):
            # print("Its a match and i is ", i)
            i += 1
        else:
            # print("Its not a match, Changing Values and re-running loop")
            if assign(i) == 1:
                while check(i) is False:
                    subtract(i)
            else:
                while check(i) is False:
                    add(i)
            i = 0


def predict():
    x = input("Enter the first attribute: ")
    y = input("Enter second attribute: ")
    x = float(x)
    y = float(y)
    calculation = (getweight1()*x)+(getweight2()*y)+(getbias())
    if calculation >= 0:
        print("1")
    else:
        print("0")


def start():
    global DataFileName
    global inputs
    global labels
    dinputs = []
    dlabels = []
    DataFileName = str(input("Please enter the name of the file containing the training set: "))

    with open(DataFileName, "r") as file:
        reader = csv.reader(file)
        for line in reader:
            x = float(line[0])
            y = float(line[1])
            label = int(line[2])
            sublist = (x,y)
            dinputs.append(sublist)
            dlabels.append(label)

    inputs = dinputs
    labels = dlabels


start()
print(inputs)
print(labels)
train()
print("The final equation of line is ", weight1, "x + ", weight2, "y + ", bias, " = 0")
predict()



