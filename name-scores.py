import time
import sys
import os.path

start = time.clock()

fname = "names.txt"

#Random name order 
#with open(fname) as f:
    #content = f.readlines()
    #random.shuffle(content)
    #for s in content:
    #    print s

if os.path.isfile(fname) == 0:
    print 'The txt file does not exist. It may have been removed.'
    sys.exit()

with open(fname) as f:
    content = f.readlines()
    #for s in content:
    #    print s
    count = 0
    for x in sorted(content):
        count += 1
        x = x.lower().rstrip('\n')
        #print x
        namelist = list(x)
            
        charnum = []
        for character in list(x):
            number = ord(character)-96
            #print number
            charnum.insert(0, number)
        #print charnum
        charnum = list(reversed(charnum))
        charcnumsum = sum(charnum)
        result = count * charcnumsum
        print str(count) + '. ' + x.title() + ' (' + str(count) + ' x ' + str(charcnumsum) + ') = ' + str(result)
        result += result
    print '\n#---------------------------------------------------------\nTotal of all the name scores in file = ' + str(result) + '\n---------------------------------------------------------#\n'

    
end = time.clock()
print 'Total execution time: ' + str(end - start) + ' sec'
