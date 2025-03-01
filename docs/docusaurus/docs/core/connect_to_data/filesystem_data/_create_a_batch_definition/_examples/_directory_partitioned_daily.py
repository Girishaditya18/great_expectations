# <snippet name="docs/docusaurus/docs/core/connect_to_data/filesystem_data/_create_a_batch_definition/_examples/_directory_partitioned_daily.py - full example">
import great_expectations as gx

context = gx.get_context()

data_source_name = "my_filesystem_data_source"
data_asset_name = "my_directory_data_asset"
file_data_asset = context.data_sources.get(data_source_name).get_asset(data_asset_name)

# <snippet name="docs/docusaurus/docs/core/connect_to_data/filesystem_data/_create_a_batch_definition/_examples/_directory_partitioned_daily.py - add Batch Definition">
batch_definition_name = "yellow_tripdata_sample_daily"
batch_definition_column = "pickup_datetime"

batch_definition = file_data_asset.add_batch_definition_daily(
    name=batch_definition_name, column=batch_definition_column
)
# </snippet>

# <snippet name="docs/docusaurus/docs/core/connect_to_data/filesystem_data/_create_a_batch_definition/_examples/_directory_partitioned_daily.py - retrieve and verify Batch">
batch = batch_definition.get_batch(
    batch_parameters={"year": "2019", "month": "01", "day": "01"}
)
print(batch.head())
# </snippet>
# </snippet>
