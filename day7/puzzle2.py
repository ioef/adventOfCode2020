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


def bag_count(color):
    rule = None
    for line in bag_rules:
        if line.startswith(color):
            rule = line
    if "no" in rule:
        return 1
    else:
        index = rule.find('contain')
        rule = rule[index+8:].split()

        i = 0
        total = 0
        while i < len(rule):
            count = rule[i]
            color = rule[i+1] + ' ' + rule[i+2]
            total += int(count) * bag_count(color)
            i += 4
    return total + 1

print(bag_count('shiny gold') - 1)
