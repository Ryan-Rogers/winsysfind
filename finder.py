import json
import sys

max_results = 100


def find(index, term):
    results_found = 0
    results = list()
    for path in index:
        if term in path:
            results_found += 1
            if results_found < max_results:
                results.append(path)
    print(f'{results_found} results found')
    return results

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide a search time as a command-line arg')
        sys.exit(1)
    else:
        term = sys.argv[1]

    with open('index.json', 'r') as index_file:
        index = json.load(index_file)
        print(find(index, term))
