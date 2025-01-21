import pandas as pd
import dask.dataframe as dd
from dask.distributed import Client
import logging
import os

# Setup logging for the script
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Dask client for parallel processing
client = Client()

def process_chunk(chunk):
    """
    Function to process a chunk of data.
    - Clean data (e.g., remove NaN values, handle outliers)
    - Transform data (e.g., adding new columns, changing data types)
    """
    logger.info(f"Processing chunk with shape: {chunk.shape}")
    
    # Example: Drop rows with NaN values in specific columns
    chunk = chunk.dropna(subset=['column_to_check'])

    # Example: Add a new column based on existing data
    chunk['new_column'] = chunk['existing_column'] * 2  # Transformation example
    
    # Example: Change data type for memory efficiency
    chunk['id_column'] = chunk['id_column'].astype('category')
    
    return chunk

def process_data(input_file, output_file):
    """
    Main function to process the data.
    - Read data in chunks or as a whole using Dask if it's a large dataset
    - Apply transformations on each chunk
    - Save the output in Parquet format
    """
    if os.path.exists(output_file):
        logger.info(f"Output file {output_file} already exists. Skipping processing.")
        return

    # Reading data with Dask (scalable and handles large datasets)
    logger.info(f"Reading input file {input_file}")
    ddf = dd.read_csv(input_file)  # Dask dataframe
    
    # Applying transformations on chunks
    logger.info("Applying transformations...")
    transformed_ddf = ddf.map_partitions(process_chunk)  # map_partitions applies function to each partition in parallel
    
    # Write the output to Parquet (efficient format for large data)
    logger.info(f"Saving the transformed data to {output_file}")
    transformed_ddf.to_parquet(output_file, write_options={'compression': 'snappy'})
    logger.info("Data processing complete and saved to Parquet.")

def main():
    input_file = 'data/raw_data.csv'
    output_file = 'data/processed_data.parquet'
    
    try:
        process_data(input_file, output_file)
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
