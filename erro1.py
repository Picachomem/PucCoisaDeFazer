def notNull(array):
    if array==None:
        print "nullarray"
    else:
        for i in array:
            if i==None:
                print "nullitem"
            else:
                pass

notNull(None)
notNull([None])
        
