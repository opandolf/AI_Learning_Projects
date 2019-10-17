def triplearray_to_string(array, array_char, line_char, col_char):
    return(str(array_char).join(str(line_char).join(str(col_char).join(str(x) for x in y) for y in z) for z in array))

def doublearray_to_string(array,line_char,col_char):
    return (str(line_char).join(str(col_char).join(str(x) for x in y) for y in array))

def array_to_string(array, char):
    return(str(char).join(str(x) for x in array))