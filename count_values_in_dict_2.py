counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
	counts[name] = 1
else:
	counts[name] = counts[name] + 1
print(counts)
