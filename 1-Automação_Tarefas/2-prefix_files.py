from pathlib import Path

root_dir = Path('dados')
file_paths = root_dir.iterdir()
# print(list(file_paths))
for path in file_paths:
    # print(path.stem)
    # print(path.suffix)
    new_filename = f'old-{path.stem}{path.suffix}'
    print(new_filename)
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)