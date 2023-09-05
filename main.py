from tabulate import tabulate
import pandas as pd


def init_data():
    df = pd.read_csv('data.csv')
    data = df.to_dict(orient='records')
    return data


def predicted_species(data):
    small_area_list = []
    big_area_list = []

    for entry in data:
        if 'species' not in entry:
            entry['species'] = ''
        else:
            if entry['species'] == 'small-leaf':
                small_area_list.append(
                    round(entry['width'] * entry['length'], 2))

            if entry['species'] == 'big-leaf':
                big_area_list.append(
                    round(entry['width'] * entry['length'], 2))

    small_area_avg = round(sum(small_area_list) / len(small_area_list), 2)
    big_area_avg = round(sum(big_area_list) / len(big_area_list), 2)
    mid_area_close = round((small_area_avg + big_area_avg) / 2, 2)

    newData = []
    for entry in data:
        if pd.isna(entry['length']):
            entry['length'] = 1

        if pd.isna(entry['width']):
            entry['width'] = 1

        width = entry['width']
        length = entry['length']

        area = width * length
        if area <= mid_area_close:
            entry['species'] = "small-leaf"
        elif area == mid_area_close:
            entry['species'] = "medium-leaf"
        else:
            entry['species'] = "big-leaf"

    return newData


def main():
    data = init_data()
    predicted_species(data)
    print(tabulate(data, headers="firstrow", tablefmt='fancy_grid') + "\n")


if __name__ == "__main__":
    main()
