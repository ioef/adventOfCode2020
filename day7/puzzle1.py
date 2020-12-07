#!/usr/bin/env python3

with open("input", "r") as fileInput:
    lines = fileInput.readlines()
    bag_rules = [line.strip() for line in lines]


def number_of_bags(color):
    lines = [ line for line in bag_rules if color in line and
            not line.startswith(color)]

    allColors = []

    if len(lines) == 0:
        return []
    else:
        colors = [ line[:line.index(' bags')] for line in lines]
        colors = [ color for color in colors if color not in allColors ]

        for color in colors:
            allColors.append(color)
            color = number_of_bags(color)

            allColors += color
            uniqueBags = list(set(allColors))

    return uniqueBags

print(len(number_of_bags("shiny gold")))

