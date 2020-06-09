import pylatex

doc = pylatex.Document(default_filepath='output/')


def section(title: str):
    doc.create(pylatex.Section(title))


def get_list_stats_latex():

    with section('Tier Distribution'):
        doc.append('The tiers of the list')

        with doc.create(pylatex.Figure()) as plot:
            plot.add_image(filename='tier.png')

    with section('Doujin Sources'):
        doc.append('What sites the doujins come from')

        with doc.create(pylatex.Figure()):
            plot.add_image(filename='source.png')

    with section('Tags'):
        doc.append('How many of each tag')

        with doc.create(pylatex.Figure()):
            plot.add_image(filename='tags.png')

    with section('Parodies'):
        doc.append('What each doujin is based on')

        with doc.create(pylatex.Figure()):
            plot.add_image(filename='parodies.png')
