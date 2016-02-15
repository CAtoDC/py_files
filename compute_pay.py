'''Function to compute pay based on a 40 hour week'''

def computePay(hours, rate):

	pay = float(hours) * float(rate)
	ot_rate = rate * 1.5

	if hours > 1 and hours < 41:
		ot_hours = 0
		
	elif hours > 40:
		ot_hours = hours - 40

	ot_pay = float(ot_hours) * float(ot_rate)
	total_pay = pay + ot_pay
	return total_pay

print("Total pay is: ", "{:,.2f}".format(computePay(40, 75)))