"""Lightweight refactored data processor module."""


class DataProcessor:
    """Clean processor for numerical data.

    This class centralizes logic for scaling numeric sequences and
    optionally delegating logging to an external object. Keeping the
    code here minimal makes it easy to maintain and test.
    """

    MULTIPLIER = 1.15

    def __init__(self, logger=None):
        """Initialize a processor instance.

        Args:
            logger: Optional object exposing a ``log`` method. It will be
                called with the list of processed values when ``process``
                is invoked.
        """
        self.logger = logger

    def process(self, data):
        """Apply the configured multiplier to each element in ``data``.

        Args:
            data: Iterable of numbers.

        Returns:
            A new list containing the scaled values.
        """
        results = [value * self.MULTIPLIER for value in data]
        if self.logger:
            # defer logging to external component if provided
            self.logger.log(results)
        return results

