total = 0
count = 0
while True:
    numinput = raw_input('Enter a number: ')
    if numinput == 'done':						#repeatedly reads numbers until 'done' is entered
        break
    else:
        try:
            numinput = int(numinput)
            total = total + numinput			#runs a total on all numbers entered
            count = count + 1					#counts how many numbers are entered
        except:
            print 'Invalid input'				#error message if input is not 'done' or a number
print 'Total:', total, 'Count:', count, 'Average:', float(total) / count