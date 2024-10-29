from pyarrow.csv import open_csv
import pyarrow as pa
import pyarrow.parquet as pq

mmap = pa.memory_map("airports.csv")
reader = open_csv(mmap)

# Open parquet file for writing with same schema as the CSV file
with pq.ParquetWriter("airports.parquet", reader.schema) as writer:
    while True:
        try:
            batch = reader.read_next_batch()
            writer.write_batch(batch)
        except StopIteration:
            break

# Load data directly from Parquet
reloaded_data = pq.read_table("airports.parquet")
print(reloaded_data)
print(reloaded_data.schema)
