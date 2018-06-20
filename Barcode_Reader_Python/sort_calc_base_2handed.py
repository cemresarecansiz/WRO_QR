exp_date = [1,1,7,6,3,9,10,2,8]
shelf_new  = sorted(exp_date)
print shelf_new
moves = {}
cont = 1
reps = 0
prev_processed = []
lastloc = None
check = False
curpro = 0
lastpro = 0
proreps = 0
for i in range(len(shelf_new)):
	curpro = shelf_new[i]

	if(curpro == lastpro):
		proreps += 1
	else:
		proreps = 0
	moves[i] = shelf_new.index(exp_date[i]) + proreps

	lastpro = curpro
print exp_date
print shelf_new
print moves
length = len(moves)
print('\n')
while(reps < length):
	if(reps != 0):
		curloc = min(moves, key=lambda x:abs(x-curloc))
	else:
		curloc = next(iter(moves.values()))
	while(cont == 1):
		check = curloc in prev_processed
		

		if(moves[curloc] in prev_processed):
			print curloc,
			moves.pop(curloc)
			print('\n=========================================\n' )
			cont = 0
			reps += 1
			continue
		else:
			if(curloc == moves[curloc]):
				cont = 0
				reps += 1
				moves.pop(curloc)
				print('\n=========================================' )
				print(str(curloc) + ' location correct!')
				print('=========================================' )
				continue
			print curloc,
		print " -> ",
		lastloc = curloc
		prev_processed.append(curloc)
		curloc = moves[curloc]
		moves.pop(lastloc)
		reps += 1
	cont = 1
