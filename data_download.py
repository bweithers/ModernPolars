from pathlib import Path
from zipfile import ZipFile
import requests

data_dir = Path("./data/") # replace this with a directory of your choice
print(data_dir.absolute())
dest = data_dir / "flights.csv.zip"

if not dest.exists():
    r = requests.get(
        "https://transtats.bts.gov/PREZIP/On_Time_Reporting_Carrier_On_Time_Performance_1987_present_2022_1.zip",
        verify=False,
        stream=True,
    )

    data_dir.mkdir(exist_ok=True)
    with dest.open("wb") as f:
        for chunk in r.iter_content(chunk_size=102400):
            if chunk:
                f.write(chunk)

    with ZipFile(dest) as zf:
        zf.extract(zf.filelist[0].filename, path=data_dir)

extracted = data_dir / "On_Time_Reporting_Carrier_On_Time_Performance_(1987_present)_2022_1.csv"