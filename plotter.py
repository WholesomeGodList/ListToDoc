import matplotlib.pyplot as plt

def create_tier_graph(god_list: list):
	labels = 'S', 'A', 'B', 'C', 'D'
	tier_counts = [0, 0, 0, 0 ,0]

	for entry in god_list:
		if entry['tier'] == 'S':
			tier_counts[0] += 1
		elif entry['tier'] == 'A':
			tier_counts[1] += 1
		elif entry['tier'] == 'B':
			tier_counts[2] += 1
		elif entry['tier'] == 'C':
			tier_counts[3] += 1
		elif entry['tier'] == 'D':
			tier_counts[4] += 1

	fig1, ax1 = plt.subplots()

	ax1.pie(tier_counts, labels=labels, autopct='%1.1f%%',
	        shadow=True, startangle=90)
	ax1.axis('equal')

	plt.savefig('output/plot.png')
