.. image:: https://i.insider.com/5481ff7669bedda4668b4568?width=1300&format=jpeg&auto=webp
    :alt: Tars from Interstellar

endurance_etl
#############

Polars and duckdb based json configured simple ETL pipelines

 <span style="color:red">WARNING: PLACEHOLDER FOR LATER DEVELOPMENT</span>

Introduction
************

Use endurance_etl to execute some simple ETL pipelines:

########
# json #
########
.. code-block:: python

    from endurance_etl import Tars

    CONFIG = "sample.json"
    # content =>
    {
        "sources": [
            {
                "name": "csv_file_source",
                "path": "csv_file_source.csv",
                # ...other_kwargs
            }
        ],
        "targets": [
            {
                "name": "csv_file_target",
                "source": "source/csv_file_source",
                "target": "csv_file_target.csv",
                "transformations": [
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

########
# yaml #
########
.. code-block:: python

    from endurance_etl import Tars

    CONFIG = "sample.yaml"
    # content =>
    sources:
        csv_file_source:
            path: "csv_file_source.csv"
            # ...other_kwargs

    targets:
        memory_target:
            source: "source/csv_file_source"
            target:
        csv_file_target:
            source: "source/csv_file_source"
            target: "csv_file_target.csv"
        excel_file_target:
            source: "target/memory_target"
            target: "excel_file_target.xlsx"

    tars = Tars.from_yaml(CONFIG)
    tars.do()
