# Object names have to be rewritten as strings in Python, else it doesn't work

import math

def orbitalPeriod(arr):
	GM = 398600.4418
	earthRadius = 6367.4447
	updatedArr = []
	
	for i in range(len(arr) ):
		for item in arr[i].items():
			if(item[0] == "name"):
				name = item[1]
			elif(item[0] == "avgAlt"):
				avgAlt = item[1]
		
		time = round(2*math.pi*math.sqrt((math.pow(earthRadius + avgAlt, 3) )/GM) )
		updatedArr.append({"name": name, "orbitalPeriod": time})
		
	return updatedArr
	
		
		
print(orbitalPeriod([{"name": "sputnik", "avgAlt": 35873.5553}]) )
## should return [{name: "sputnik", orbitalPeriod: 86400}].
print(orbitalPeriod([{"name": "iss", "avgAlt": 413.6}, {"name": "hubble", "avgAlt": 556.7}, {"name": "moon", "avgAlt": 378632.553}]) )
## should return [{name : "iss", orbitalPeriod: 5557}, {name: "hubble", orbitalPeriod: 5734}, {name: "moon", orbitalPeriod: 2377399}]