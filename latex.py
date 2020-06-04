import pylatex


def get_list_stats_latex(god_list: list):
	doc = pylatex.Document(default_filepath='output/')

	with doc.create(pylatex.Section('Tier Distribution')):
		doc.append('The tiers of the list')
