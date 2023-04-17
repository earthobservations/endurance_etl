import json
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from diskcache import Cache

cache = Cache()


@dataclass
class Source:
    name: str
    path: str

    def __str__(self):
        return f"Source({self.name})"

    def read(self):
        pass

    @staticmethod
    @cache.memoize
    def _read(self):
        pass


@dataclass
class Target:
    name: str
    source: str | list[str]
    target: str | None
    transformation: list[dict]

    def __str__(self):
        return f"Target({self.name})"

    def write(self):
        pass

    def _prepare(self):
        pass


class Tars:

    @classmethod
    def from_json(cls, p: str | bytes | BytesIO | Path) -> "Tars":
        try:
            with Path(p).open() as f:
                d = json.load(f)
        except (TypeError, FileNotFoundError):
            try:
                p.seek(0)
                p = p.read()
            except:
                pass
            d = json.loads(p)
        return cls.from_dict(d)

    @classmethod
    def from_yaml(cls, p: str | Path) -> "Tars":
        import yaml
        try:
            from yaml import CLoader as Loader
        except ImportError:
            from yaml import Loader
        with Path(p).open() as f:
            d = yaml.load(f, Loader=Loader)
        return cls.from_dict(d)

    @classmethod
    def from_dict(cls, d: dict) -> "Tars":
        return cls(d)

    # @classmethod
    # def _parse_config(cls, config: dict) -> dict:
    #     config = config.copy()
    #     config_parsed = {
    #         "sources": {},
    #         "targets": {}
    #     }
    #     sources = config["sources"][:]
    #     for source in sources:
    #         s = Source(**source)
    #         config_parsed[sources][s.name] = s
    #     targets = config["targets"][:]
    #
    #
    # @classmethod
    # def _build_dependency_tree(cls, config: dict) -> dict:
    #     dtree = {}
    #
    #     for target in config["target"]:
    #         target_name = target["name"]
    #         try:
    #             sources = target["sources"]
    #         except KeyError:
    #             sources = [target["source"]]
    #         for source in sources:
    #             source_type, source_name = source.split("/")
    #             if source_type == "source":
    #                 continue
    #             dtree[target_name] = source_name
    #
    #     return dtree

    def __init__(self, config: dict):
        self.sources = {}
        self.targets = {}
        self.config_raw = config
        self.config_parsed = self._parse_config(config)
        self.dependency_tree = self._build_dependency_tree(config)

    def do(self):
        for target in self.config["targets"]:
            source_level, source_name = target["source"].split("/")


