from pathlib import Path
from locust import HttpUser, task

from locust_replay.models.apm_record import ApmRecord



class ReplayUser(HttpUser):
    records_csv: Path | str = None

    def __init__(self,*args, **kwargs):
        print(self.records_csv)
        if self.records_csv is None:
            raise ValueError("records_csv is required")

        self.source = self.records_csv if isinstance(self.records_csv, Path) else Path(self.records_csv)
        self.records = list(ApmRecord.from_csv(self.source))

        self.tasks = {self.replay: 1}
        super().__init__(*args, **kwargs)
    
    def replay(self):
        for record in self.records:
            self.client.request(
                method=record.http_request_method,
                url=record.url_full,
                headers=record.http_request_headers,
                name=record.url_full,
            )
