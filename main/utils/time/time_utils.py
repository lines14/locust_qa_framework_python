import time
from datetime import UTC, date, datetime, timedelta, timezone

from resources.data.constants import TIME_DELTA


class TimeUtils:
    @staticmethod
    def to_utc(dt: datetime) -> datetime:
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone(timedelta(hours=TIME_DELTA)))

        return dt.astimezone(UTC)

    @staticmethod
    def now_local():
        """Current time-of-day in the test environment's business timezone (UTC+TIME_DELTA).

        ``datetime.now()`` is naive host-local time and differs between a dev
        machine (Almaty) and the CI runner (UTC). Values like delivery-period
        ``start_time`` are stored in business local time, so comparisons must be
        anchored to it explicitly. Returns a plain time-of-day (no date, no
        tzinfo) so callers can compare it against DB "Time" columns directly.
        """
        return datetime.now(timezone(timedelta(hours=TIME_DELTA))).time()

    @staticmethod
    def today() -> date:
        return date.today()

    @staticmethod
    def get_timestamp_after_seconds(seconds):
        return time.time() + seconds

    @staticmethod
    def timestamp_is_not_expired(timestamp):
        return time.time() < timestamp

    @staticmethod
    def wait_seconds(seconds):
        time.sleep(seconds)

    @staticmethod
    def get_perf_counter():
        return time.perf_counter()
