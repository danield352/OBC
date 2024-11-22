from pathlib import Path
from datetime import datetime

path  = Path('files', 'dados', 'b.txt')

print(path)

# print(path.stat())
stats = path.stat()
second_created = stats.st_ctime
date_created = datetime.fromtimestamp(second_created)
# print(date_created)
date_created_str = date_created.strftime('%Y-%m-%d_%H_%M_%S')
print(date_created_str)
