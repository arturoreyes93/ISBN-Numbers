#  File: ISBN.py

#  Description: reads a text file with isbn numbers and creates another text file with the isbn numbers saying if they are valid or invalid

#  Student Name: Arturo Reyes Munoz

#  Student UT EID: ar48836

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 04/01

#  Date Last Modified: 04/02

def clean_up(x):

	X=x

	if X[len(x)-1]=='\n':

		X.remove(X[len(X)-1])

	if X[len(X)-1]==('X' or 'x'):

			X[len(X)-1]=10

	for j in X:

		if j=='-':

			X.remove(j)

	for j in X:
			if j=='X':
				X.remove(j)

	for j in X:
			if j=='x':
				X.remove(j)

	return X

def valid(string_l):

	s0=string_l
	s1=[]
	s2=[]

	for i in range(len(s0)):

		s0[i]=int(s0[i])

	s1.append(s0[0])

	for j in range(len(s0)-1):

		s1.append(s1[j]+s0[j+1])

	s2.append(s1[0])

	for j in range(len(s1)-1):

		s2.append(s2[j]+s1[j+1])

	if len(s2)==10 and (s2[9]%11)==0:

		return True	

	else:

		return False


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

		string_list=[]

		for j in i:

			string_list.append(j)

		string_list=clean_up(string_list)

		if len(string_list)!=10:

			result = str(original_isbn[it]).rstrip()+' invalid\n'
			
			outfile.write(result)

		elif len(string_list)==10:

			if valid(string_list):

				result = str(original_isbn[it]).rstrip()+' valid\n'
				
				outfile.write(result)

			else:
				result = str(original_isbn[it]).rstrip()+' invalid\n'
				
				outfile.write(result)


		it+=1

	outfile.close()


main()