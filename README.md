![Tars from Interstellar](https://i.insider.com/5481ff7669bedda4668b4568?width=1300&format=jpeg&auto=webp)

# endurance_etl
Polars and duckdb based json configured simple ETL pipelines

 <span style="color:red">WARNING: PLACEHOLDER FOR LATER DEVELOPMENT</span>

# Introduction

Use endurance_etl to execute some simple ETL pipelines:

```python
import json
from endurance_etl import Tars

CONFIG = "sample.json"

with open(CONFIG) as f:
    print(json.load(f))

# Output:
{
    "SOURCES": [
        {
            "name": "csv_file_source",
            "path": "csv_file_source.csv",
            # ...other_kwargs
        }
    ],
    "TARGETS": [
        {
            "name": "csv_file_target",
            "source": "source/csv_file_source",
            "target": "csv_file_target.csv",
            "transforms": [
                {
                    "function": "lambda df: df + 1"
                }
            ]
            # ...other_kwargs
        }
    ]
}

tars = Tars.from_json(CONFIG)
tars.do()

```