import csv
from math import floor, ceil
from pathlib import Path
from model import Element, LumberOption
import collections


STANDARD_LENGTHS = [3, 3.3, 3.6, 3.9, 4.2, 4.5, 4.8, 5.1, 5.4, 5.7, 6]
STANDARD_LENGTHS_BY_PRICES = {
    3: 100.0,
    3.3: 115,
    3.6: 130,
    3.9: 145,
    4.2: 160,
    4.5: 175,
    4.8: 190,
    5.1: 205,
    5.4: 220,
    5.7: 235,
    6: 250
}


def parse_dims(dims: [str]) -> [float]:
    return list(map(lambda dim: float(dim), dims))


home = str(Path.home())
with open("%s/objects.csv" % home, newline='') as csvfile:
    reader = csv.reader(csvfile)
    elements = list(map(lambda row: Element(*row[:2], *parse_dims(row[2:5])), reader))
    for el in filter(lambda e: e.is_5_by_10(), elements):
        print(el)
    lengths = set(el.len() for el in elements if el.is_5_by_10())
    elements_by_lengths = {}
    for el in elements:
        if el.is_5_by_10():
            elements_by_lengths.setdefault(el.len(), []).append(el)
    counts_by_lengths = {k: len(v) for k, v in elements_by_lengths.items()}
    counts_by_lengths = collections.OrderedDict(sorted(counts_by_lengths.items()))
    options = []
    options_by_length = {}
    for length, count in counts_by_lengths.items():
        length_options = []
        for s, p in STANDARD_LENGTHS_BY_PRICES.items():
            if s >= length:
                elements_per_piece = floor(s/length)
                waste_per_piece = s - (elements_per_piece * length)
                pieces_needed = ceil(count/elements_per_piece)
                waste_on_last_piece = ((count % elements_per_piece) * length) + waste_per_piece
                option = LumberOption(
                    elements_per_piece=elements_per_piece,
                    waste_per_piece=waste_per_piece,
                    waste_on_last_piece=waste_on_last_piece,
                    pieces_needed=pieces_needed,
                    standard_length=s,
                    price=p,
                    count_needed=count,
                    length_needed=length
                )
                options.append(option)
                length_options.append(option)
        options_by_length[length] = length_options
    for length in counts_by_lengths.keys():
        length_options = options_by_length[length]
        least_waste_per_piece = min(length_options, key=lambda opt: opt.waste_per_piece)
        least_total_waste = min(length_options, key=lambda opt: opt.waste_per_piece * (opt.pieces_needed - 1) + opt.waste_on_last_piece)
        print("Length: ", length)
        print("Best (comparing waste per piece): ", least_waste_per_piece)
        print("best (comparing total waste): ", least_total_waste)
        print("-----------------------------------------")
        score_by_option.setdefault()

    total_length = sum(elements_by_lengths.keys())
    print('Total length', total_length)
    score_by_piece_length = {}
    for option in options:
        score_by_piece_length.setdefault(option.standard_length, )

