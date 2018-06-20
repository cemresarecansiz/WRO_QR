import sort_date
exp_date , dates_orig = sort_date.calcDate()
shelf_back = exp_date[:]
try:
    expired = exp_date.count(-1)
    for i in range(expired):
        shelf_back.pop(shelf_back.index(-1))

    shelf_new  = sorted(shelf_back)
    for i in range(expired):
        shelf_new.append(-1)
except ValueError:
    print('')
exp_date.append(None)
shelf_new.append(None)
repeats = 0
correct_locs = []
temp = None
moved_item = None
moved_item_loc = None


print "\n\n\n//////////////////////////////////////////////////////////////////////////////"
print("                  {}               ".format(exp_date))
print("                  {}               ".format(shelf_new))
print "/////////////////////////////////////////////////////////////////////////////\n\n\n"

def backArray(myArray):
    global shelf_back
    shelf_back = []
    for i in range(len(myArray)):
        shelf_back.append(myArray[i])

def eqArray(myArray):
    global exp_date
    exp_date = []
    for i in range(len(myArray)):
        exp_date.append(myArray[i])


def place():
    global exp_date
    global shelf_new
    global repeats
    global shelf_back
    repeats += 1
    backArray(exp_date)
    
    if (exp_date[len(exp_date)-1] != None):
        empty_loc = exp_date.index(None)
        moved_item_loc = exp_date.index(shelf_new[empty_loc])
        reps=0
        while True:
            reps += 1
            if(moved_item_loc in correct_locs):
                exp_date.pop(moved_item_loc)
                moved_item_loc = exp_date.index(shelf_new[empty_loc]) + reps
                continue
            break
        eqArray(shelf_back)
        moved_item = exp_date[moved_item_loc]
        if(exp_date[moved_item_loc] != shelf_new[moved_item_loc]):
            exp_date[moved_item_loc] = None
            exp_date[empty_loc] = moved_item
            correct_locs.append(empty_loc)
            

            print "        Moved item {0} to location {1}. Location {2} is now empty!".format(moved_item,empty_loc + 1, moved_item_loc + 1)
            print "============================================================================"
        else:
            print "      Leaving item {0} in location {1}. Location {2} is still empty!".format(moved_item, moved_item_loc + 1,empty_loc + 1)
            print "============================================================================"
            correct_locs.append(moved_item_loc)
        place()
    else:
        return
    



while True:
    if(repeats < len(exp_date)):
        for i in range(len(exp_date)):
            if(exp_date[len(exp_date)-1] == None):
                if(exp_date[i] == shelf_new[i]):
                    continue
                else:
                    exp_date[len(exp_date)-1] = exp_date[i]
                    print '\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
                    print '     TEMP IS EMPTY, MOVING {0} FROM LOCATION {1} TO THE TEMP'.format(exp_date[i],i+1)
                    print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
                    print "============================================================================"
                    exp_date[i] = None


    else:
        break
    place()

try:
    print('***********************************************************************************')
    print('          The last {} items have expired, throwing them away.'.format(len(exp_date)-shelf_new.index(-1)-1))
    print('***********************************************************************************')
except ValueError:
    print("                              No items have expired")
    print('***********************************************************************************')
