def not_null(array):
    if (array == None):
        return "nullarray"
    else:
        for i in array:
            if (i == None):
                return "nullitem"
            else:
                pass

a = None
print(not_null(a))
            

        
