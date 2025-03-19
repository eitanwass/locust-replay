from locust_replay.replay_user import ReplayUser, HttpUser


class SampleReplayUser(ReplayUser):
    records_csv = "./tests/resources/apm_records_sample.csv"
