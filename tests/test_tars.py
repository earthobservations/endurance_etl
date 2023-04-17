import json
from io import BytesIO

import pytest

from endurance_etl import Tars


@pytest.fixture
def tars_config():
    return {
        "sources": [
            {
                "name": "dwd_kl_1048",
                "path": "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/"
                        "kl/historical/tageswerte_KL_01048_19340101_20221231_hist.zip"
            }
        ],
        "targets": [
            {
                "name": "dwd_kl_1048_target3",
                "sources": ["targets/dwd_kl_1048_target2", "targets/dwd_kl_1048_target"],
                "path": "dwd_kl_1048_target2.csv",
                "transformations": [
                    {
                        "function": "lambda df: df + 1"
                    }
                ]
            },
            {
                "name": "dwd_kl_1048_target2",
                "source": "targets/dwd_kl_1048_target",
                "path": "dwd_kl_1048_target2.csv",
                "transformations": [
                    {
                        "function": "lambda df: df + 1"
                    }
                ]
            },
            {
                "name": "dwd_kl_1048_target",
                "source": "sources/dwd_kl_1048",
                "path": "dwd_kl_1048_target.csv",
                "transformations": [
                    {
                        "function": "lambda df: df + 1"
                    }
                ]
            },
        ]
    }


@pytest.fixture
def tars_config_json_str(tars_config):
    return json.dumps(tars_config)


def test_tars_config(tars_config):
    tars = Tars.from_dict(tars_config)
    assert tars.config == tars_config
    print(tars.dependency_tree)


def test_tars_config_from_json(tars_config_json_str, tars_config):
    json_bytes = bytes(tars_config_json_str, encoding="utf8")
    tars = Tars.from_json(json_bytes)
    assert tars.config == tars_config


def test_tars_config_from_json_path(tars_config, tmp_path):
    json_path = tmp_path / "test.json"
    json_path.write_text(json.dumps(tars_config))
    tars = Tars.from_json(json_path)
    assert tars.config == tars_config
