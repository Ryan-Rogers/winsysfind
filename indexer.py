import json
import time
import os


def index():
    indexed_files = list()
    folders_skipped = 0
    start_time = time.time()

    queue = ['/']
    while queue:
        folder_path = queue.pop(0)
        try:
            with os.scandir(folder_path) as folder:
                if str(len(queue)).endswith('000'):
                    print(f'Queue at ~{len(queue)}')

                for path in folder:
                    if path.is_dir():
                        queue.append(f'{folder_path}{path.name}/')
                    else:
                        indexed_files.append(f'{folder_path}{path.name}')
        except PermissionError:
            folders_skipped += 1
        except KeyboardInterrupt:
            print('Breaking')
            break

    print(f'{folders_skipped} folders skipped')
    print(f'{len(indexed_files)} files indexed')
    print(f'{int(time.time() - start_time)} seconds')

    return indexed_files

if __name__ == '__main__':
    indexed_files = index()
    with open('index.json', 'w') as index_file:
        index_file.write(json.dumps(indexed_files))
