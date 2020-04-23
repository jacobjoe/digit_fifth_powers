""" Digit fifth power """


# create a class
class Fifth:
    # create a method and passing parameters
    def digit_fifth_power(self, first, last):
        print("Numbers are")
        lst_3 = []
        for i in range(first, last):
            j = str(i)
            # empty list for storing separate each number as integer by converting them into string and integer
            lst_1 = []
            # empty list for append multiplied value taken from lst_1
            lst_2 = []
            a = int(j[0])
            lst_1.append(a)
            b = int(j[1])
            lst_1.append(b)
            c = int(j[2])
            lst_1.append(c)
            d = int(j[3])
            lst_1.append(d)
            e = int(j[4])
            lst_1.append(e)
            # for loop for multiplication calculation
            for k in lst_1:
                lst_2.append(k**5)
            # if condition for check the addition of multiplied value to the integer value
            if sum(lst_2) == i:
                print(i)
                # append to another list for calculate the sum
                lst_3.append(i)
        print("Sum of these numbers is", sum(lst_3))


# create object for class
fifth_powers = Fifth()
# call the method and passing argument(only five digits) by using the created object
fifth_powers.digit_fifth_power(10000, 100000)
