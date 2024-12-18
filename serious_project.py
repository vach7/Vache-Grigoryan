"""
    Designs a placement with a given Spec of IP
"""
import json
import math
import os, sys
import random


class Struct:

    ip_size: tuple
    cell_count: int
    cell_spec_path: str


class Cell:

    def __init__(self, size, name, conn_list):
        self.size = size
        self.name= name
        self.cell_connectivity= conn_list


def read_cells(path):
    # read json
    with open(path, 'rb') as f:
        data = json.load(f)
    my_list = []
    # return cell list [Cell]
    for cell in data['Cells']:
        #for k,v  in cell.items():
        x=Cell(size=tuple(cell["size"].split()),
             name=cell['name'],
             conn_list=cell["connects"]
             )
        my_list.append(x)

    return my_list


def logic(cells, maxx, maxy):
    list_1=[]

    index = 0

    while True:
        x = 0
        row =[]
        mincells = cells[index]
        while x <= maxx:
            row.append(mincells)
            x+=mincells.size[0]
            index += 1
            mincells = cells[index]

            if index == len(cells):
                break

        list_1.append(row)
    return list_1

     # return list of lists



cache = {}
def fibonacci(n):
    global cache
    if n in cache:
        return cache[n]
    if n == 1:
        cache[n] = 0
        return 0
    elif n == 2:
        cache[n] = 1
        return 1
    else:
        val = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = val
        return val


def create_json(cell_count, max_x, max_y):
    x, y = 0, 0
    area = max_x*max_y
    max_cell_area = area/cell_count
    name_template = "cell_{}"
    current_area = 0
    cell_conectivity = {name_template.format(k): list() for k in range(cell_count)}
    cells=[]
    for i in range(cell_count):
        cell_name = name_template.format(i)
        aprox_avg_side = int(round(math.sqrt(max_cell_area)))
        if current_area >= i*max_cell_area:
            length = aprox_avg_side - random.randint(1, aprox_avg_side)
            width = aprox_avg_side - random.randint(1, aprox_avg_side)
        else:
            length = aprox_avg_side + random.randint(1, aprox_avg_side)
            width = aprox_avg_side + random.randint(1, aprox_avg_side)
        current_area += length*width
        connects = cell_conectivity[cell_name]
        if len(connects)<4:
            for i in range(random.randint(1, 5-len(connects))):
                random_cell = name_template.format(random.randint(0, cell_count-1))
                connects.append(random_cell)
                cell_conectivity[random_cell].append(cell_name)
        cells.append({"name": cell_name, "size": f"{length} {width}", "connects": connects})
    with open("ankap.json", "wt") as file:
        json.dump({"Cells":cells}, file)






def main():
    create_json(100, 50, 250)
    # Get specs
    # parse  cell file
    # PLacement Logic
    # write into a file the result
    # run the checker

main()

