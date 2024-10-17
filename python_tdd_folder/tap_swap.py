array_to_be_swapped = [1, 2, 3, 4, 5, 6]
#get_swapped_elements(array_to_be_swapped)


def get_swapped_elements(array_to_be_swapped):
	for swapp in range(0, len(array_to_be_swapped)- 1, 2):
		temp = array_to_be_swapped[swapp]
		array_to_be_swapped[swapp] = array_to_be_swapped[swapp + 1]
		array_to_be_swapped[swapp + 1] = temp
	return array_to_be_swapped
		
	    
    