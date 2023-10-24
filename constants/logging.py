from typing import Final, Protocol

DEFAULT_FORMATTER: Final[str] = '%(asctime)s - %(message)s'


class LoggingStream(Protocol):
    def flush(self):
        pass

    def write(self):
        pass

    def close(self):
        pass
