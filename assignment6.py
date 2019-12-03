### CMPT 120
### author Huy Nguyen

### Data Processing

### TOP LEVEL

def instructions():
    print ("WELCOME to the CMPT 120 Preferences and Similarities system!")
    print ("============================================================\n")
    print ("This system will process data from the file: IN_all_data.txt")
    print ("  (the file with that exact name needs to be in this folder!!!\n")
    print ("The file has answers of students opinions")
    print ("  (from 1 - strongly disagree to 5- strongly agree\n")
    print ("The system will produce:")
    print ("  - an output file with avgs per student: OUT_perstudent.csv")
    print ("  - several statistics\n")
    print ("You will also be able to check if paris of students are similar")
    print ("\nMaximum number of pairs ==> 5\n")
############
def list_of_strings():

    f = open("IN_all_data.txt","r")      
    lst1=[]            
    
    for lines in f:
        string = lines[0:len(lines)-1]                                                        
        lst1.append(string)          
    f.close()  

    print ("Initial processing ...")    
    print ("\n JUST TO TRACE, the list OF STRINGS is:\n")
    print(lst1)

#############
def student_per_line():
    f = open("IN_all_data.txt","r")      
    lst1=[]            
    
    for lines in f:
        string = lines[0:len(lines)-1]                                                        
        lst1.append(string)          
    f.close()
    print ("\n TRACE printing one STUDENT (name and LIST responses) per line\n")
    res = (f"{letters} -- {[*map(int,digits)]}" for letters, *digits in [i.split() for i in lst1])
    print(*res, sep = '\n')


def stats():
    f = open("IN_all_data.txt","r")      
    lst1=[]            
    
    for lines in f:
        string = lines[0:len(lines)-1]
        string = string.split()
        lst1.append(string)
    f.close()
    lst2 = [item[0] for item in lst1]
    print ("\n studs, nqns: " + str(len(lst2)) + " " + str(len(lst1[0])-1))
    print ("\nProcessing all students' responses ...\n")
    print ("\nAll students' responses have been processed ...\n")
    print ("\n SOME STATS!!")
    print (" ============ ")
    print ("\nThe input file had responses from: " + str(len(lst2)) + " students")
    print ("Each student responded to: " + str(len(lst1[0])-1) + " questions")

def average():
    f = open("IN_all_data.txt","r")      
    lst1=[]            
    responses = []
    
    for lines in f:
        line = lines.strip().split()
        nums = line[1:]
        nums = [float(i) for i in nums]
        responses.append(nums)
    averages = []
    for i in range(len(responses[0])):
        averages.append((responses[0][i]+responses[1][i]+responses[2][i])/3)
    maxAvg = max(averages)
    questionMax = []
    for i in range(len(averages)):
        if averages[i] == maxAvg:
            questionMax.append(i+1)
    mostAgreed = ''
    for i in questionMax:
        mostAgreed += str(i)+', '
    mostAgreed = mostAgreed[:-2]
    print('question num - average')
    for i in range(len(averages)):
        print('{:3d} - {:.2f}'.format(i+1,averages[i]))
    print('\nThe most agreed questions were: \n')
    print(mostAgreed)
    print("\nNOW... LET'S SEE SIMILARITIES BETWEEN PAIRS OF STUDENTS!!...")
    print("\n============================================================\n")
    f.close()

##############
nameList = [] 
digitList = []

def getList(filename):
    f = open(filename,"r") 
    line = f.readline()
    while line!='':
        data = line.split()
        currentDigitList = []
        for i in range(1,len(data)):
            currentDigitList.append(int(data[i]))
        nameList.append(data[0])
        digitList.append(currentDigitList)
        line = f.readline()

    f.close()

def similarity(lst1,lst2):
    size = len(lst1)
    count = 0
    for i in range(0,size):
        if lst1[i] == lst2[i]:
            count += 1
    return count 

def check_pairs():

    filename = "IN_all_data.txt"
    getList(filename)
    maxNumOfPairs = 5
    print("You can check up to",maxNumOfPairs,"pairs.\n")
  
    pair = 1 
    anotherPair = ""
  
    while pair <= 5 :
        first_pair = input(anotherPair + "Please provide the first name in the pair (or END to finish) ==>")
        if first_pair == "END":
            break
        
        second_pair = input("Please provide the second name in the pair ==>")
        if first_pair not in nameList or second_pair not in nameList:
            
            print("** Sorry! at least one name is not in the data")
        else: 
            name1 = nameList.index(first_pair)
            name2 = nameList.index(second_pair)
            list1 = digitList[name1]
            list2 = digitList[name2]

            count = similarity(list1,list2)
            print("TRACES similar",count)
      
            ratio = float(count)/len(list1)
            res = first_pair + " and " + second_pair

            if ratio >= 0.9:
                res += " really have a lot in common (>90%)!"
            elif ratio >= 0.5:
                res +=  " have abount half opinions in common!"
            elif count >= 2:
                res +=  " have just few opinions in common (<50%)!"
            elif count < 2:
                res +=  " have nothing in common!"
            print(res) 
  
        pair += 1 
        anotherPair = "Another pair? "
    print("\n***** Sorry you cannot check more pairs.. you reached the maximum: 5\n")

############## MAIN LEVEL
#GLOBAL VARIABLES
nameList = [] 
digitList = []
############
instructions()
list_of_strings()
student_per_line()
stats()
average()
check_pairs()
