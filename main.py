import requests

import latex
import plotter

api = "https://wholesomelist.com/api/list"


def main():
	r = requests.get(api)
	god_list = r.json()['table']

	plotter.create_tier_graph(god_list)


if __name__ == "__main__":
	main()
