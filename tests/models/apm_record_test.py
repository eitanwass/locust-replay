from pathlib import Path
from locust_replay.models.apm_record import ApmRecord


def test_from_csv(resources: Path) -> None:
    csv_file = resources / "apm_records_sample.csv"
    records = list(ApmRecord.from_csv(csv_file))
    assert len(records) == 40
