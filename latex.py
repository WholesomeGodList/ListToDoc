import pylatex


def get_list_stats_latex(god_list: list):
    doc = pylatex.Document(default_filepath='output/')

    with doc.create(pylatex.Section('Tier Distribution')):
        doc.append('The tiers of the list')

        with doc.create(pylatex.Figure()) as plot:
            plot.add_image(filename='tier.png')

    with doc.create(pylatex.Section('Doujin Sources')):
        doc.append('What sites the doujins come from')

        with doc.create(pylatex.Figure()):
            plot.add_image(filename='source.png')

    with doc.create(pylatex.Section('Tags')):
        doc.append('How many of each tag')

        with doc.create(pylatex.Figure()):
            plot.add_image(filename='tags.png')