from pathlib import Path
from datetime import datetime as dt

root_dir=Path('files')
file_paths=root_dir.glob("**/*")

for path in file_paths:
  if path.is_file():
    print(path)
    stats=path.stat()
    modified=stats.st_mtime
    timestamp=dt.fromtimestamp(modified)
    modified_str=timestamp.strftime("%Y-%m-%d_%H:%M:%S")
    new_filename=modified_str + '-' + path.name
    print(new_filename)
    new_filepath=path.with_name(new_filename)
    path.rename(new_filepath)
