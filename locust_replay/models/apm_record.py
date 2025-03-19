from __future__ import annotations
from typing import Generator

from datetime import datetime
import csv
from pathlib import Path
from attrs import define, field, validators, fields_dict

def parse_timestamp(date_str: str) -> float:
    return datetime.strptime(date_str, "%b %d, %Y @ %H:%M:%S.%f").timestamp()


@define(kw_only=True, init=False)
class ApmRecord:
    timestamp: float = field(alias='timestamp', converter=parse_timestamp)
    _id: str = field(alias='_id')

    http_request_headers: str = field()
    http_request_method: str = field()
    http_response_headers: str = field()
    http_response_status_code: int = field()

    timestamp_us: int = field()
    
    url_domain: str = field()
    url_full: str = field()
    url_path: str = field()
    url_port: int = field()
    url_scheme: str = field()

    user_agent_device_name: str = field()
    user_agent_name: str = field()
    user_agent_original: str = field()

    def __init__(self, **kwargs):
        sanitized_kwargs = {}
        for key, value in kwargs.items():
            sanized_key = key.replace(".", "_").strip("@ ")
            if sanized_key not in fields_dict(self.__class__).keys():
                print(f"Skipping unknown attribute: {sanized_key}")
                continue
            sanitized_kwargs[sanized_key] = value
        self.__attrs_init__(**sanitized_kwargs)


    @classmethod
    def from_csv(cls: ApmRecord, csv_file: Path) -> Generator[ApmRecord, None, None]:
        with csv_file.open() as f:
            reader = csv.DictReader(f)
            for row in reader:
                yield cls(**row)
