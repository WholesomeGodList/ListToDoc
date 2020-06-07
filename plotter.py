import matplotlib.pyplot as plt


def create_tier_graph(god_list: list):
    labels = 'S', 'A', 'B', 'C', 'D'
    tier_counts = [0, 0, 0, 0, 0]

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

    plt.savefig('output/tier.png')


def create_source_graph(god_list: list):
    labels = 'nhentai.net', 'imgur.com', 'Other'
    source_counts = [0, 0, 0]

    for entry in god_list:
        if 'nhentai.net' in entry['link']:
            source_counts[0] += 1
        elif 'imgur.com' in entry['link']:
            source_counts[1] += 1
        else:
            source_counts[2] += 1

    fig1, ax1 = plt.subplots()

    ax1.pie(source_counts, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    plt.savefig('output/source.png')


def create_tag_graph(god_list: list):
    tags_and_counts = {}

    for entry in god_list:
        for tag in entry['tags']:
            if tag in tags_and_counts.keys():
                tags_and_counts[tag] += 1
            else:
                tags_and_counts[tag] = 1

    tags_and_counts = sorted(tags_and_counts.values(), reverse=True)
    fig1, ax1 = plt.subplots()

    names = list(tags_and_counts.keys())
    values = list(tags_and_counts.values())

    ax1.bar(names, values)

    plt.savefig('output/tags.png')
