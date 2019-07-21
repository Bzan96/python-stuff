'''
	Iirc Python can't return undeclared variables like JavaScript can.
	May have to double-check that.
'''

def checkCashRegister(price, cash, cid):
	unitsAmount = [0.01, 0.05, 0.1, 0.25, 1, 5, 10, 20, 100]
	
	totalCash = 0
	
	for money in list(cid):
		totalCash += money[1]
	
	remainingCash = totalCash-cash+price
	
	returnCash = cash
	cashInDrawer = cid
	change = []
	
	if(totalCash >= (price-cash) and cash >= price):
		returnCash = cash - price

	if(returnCash-totalCash == remainingCash):
		return {"status": "CLOSED", "change": cid}
		
	for i in range(len(unitsAmount)-1, -1, -1):
		count = 0
		while(returnCash >= unitsAmount[i] and cashInDrawer[i][1] > 0):
			returnCash -= unitsAmount[i]
			cashInDrawer[i][1] -= unitsAmount[i]
			count += 1
			
			cashInDrawer[i][1] = round(cashInDrawer[i][1], 2)
			returnCash = round(returnCash, 2)
			
		if(unitsAmount[i]*count > 0):
			change.append([cashInDrawer[i][0], unitsAmount[i]*count])
			count = 0
			
	if(returnCash > cashInDrawer[0][1]):
		return {"status": "INSUFFICIENT_FUNDS", "change": []}
		
	return {"status": "OPEN", "change": change}
	
	
	
print(checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]) )
##should return {status: "OPEN", change: [["QUARTER", 0.5]]}.
print(checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]) )
##should return {status: "OPEN", change: [["TWENTY", 60], ["TEN", 20], ["FIVE", 15], ["ONE", 1], ["QUARTER", 0.5], ["DIME", 0.2], ["PENNY", 0.04]]}.
print(checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]) )
##should return {status: "INSUFFICIENT_FUNDS", change: []}.
print(checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 1], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]) )
##should return {status: "INSUFFICIENT_FUNDS", change: []}.
print(checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]) )
##should return {status: "CLOSED", change: [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]}.