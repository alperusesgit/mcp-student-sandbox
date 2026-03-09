class DataProcessor:
    """Processes numerical data with a fixed multiplier."""
    
    MULTIPLIER = 1.15
    
    def __init__(self, logger=None):
        """Initialize the processor with an optional logger.
        
        Args:
            logger: Optional Logger instance for recording results.
        """
        self.logger = logger
    
    def process(self, data):
        """Process data by applying the multiplier.
        
        Args:
            data: List of numerical values to process.
            
        Returns:
            List of processed values.
        """
        return [value * self.MULTIPLIER for value in data]


class Logger:
    """Handles logging of processed data to file."""
    
    def __init__(self, filename="log.txt"):
        """Initialize the logger with a target file.
        
        Args:
            filename: Name of the file to log to.
        """
        self.filename = filename
    
    def log(self, data):
        """Append data to the log file.
        
        Args:
            data: Data to log.
        """
        with open(self.filename, "a") as f:
            f.write(str(data) + "\n")


class DataPipeline:
    """Orchestrates data processing with optional logging and output."""
    
    def __init__(self, processor, logger=None, verbose=False):
        """Initialize the pipeline.
        
        Args:
            processor: DataProcessor instance for processing data.
            logger: Optional Logger instance.
            verbose: If True, print results to stdout.
        """
        self.processor = processor
        self.logger = logger
        self.verbose = verbose
    
    def execute(self, data):
        """Execute the full pipeline: process, log, and optionally print.
        
        Args:
            data: Input data to process.
            
        Returns:
            List of processed values.
        """
        results = self.processor.process(data)
        
        if self.verbose:
            for value in results:
                print(f"Total: {value:.2f}")
        
        if self.logger:
            self.logger.log(results)
        
        return results


# Example usage
if __name__ == "__main__":
    processor = DataProcessor()
    logger = Logger("log.txt")
    pipeline = DataPipeline(processor, logger, verbose=True)
    
    results = pipeline.execute([10, 20, 30])
    print(f"Processed results: {results}")
