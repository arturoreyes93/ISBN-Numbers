def main():

	file = open('isbn.txt','r')

	isbn=[]

	for i in file:

            isbn.append(i)

	file.close()

	outfile = open('isbnOut.txt','w')

	original_isbn=isbn

	it=0

	for i in isbn:

            for j in i:

                if not(int(j)) and (i!='x' or i!='X'):

                    isbn.remove(j)

            if len(i)!=10:

                print(str(original_isbn[it]) + '  invalid')

                outfile.write(str(original_isbn[it]) + '  invalid')

	    elif len(i)==10:

                s1=[]
	        s2=[]

		for j in range(len(i)-1):

                    s1.append(i[0])

                    s1.append(s1[j]+i[j+1])

		for j in range(len(s1)-1):

                    s2.append(s1[0])

                    s2.append(s2[j]+s1[j+1])

	        if len(s2)==10 and s2[len(s2)-1]%11==0:

                    print(str(original_isbn[it]) + '  valid')

                    outfile.write(str(original_isbn[it]) + '  valid')

		else:

                    print(str(original_isbn[it]) + '  invalid')

                    outfile.write(str(original_isbn[it]) + '  invalid')

        it+=1

    outfile.close()


main()
