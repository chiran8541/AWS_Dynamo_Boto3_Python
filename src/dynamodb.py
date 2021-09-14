

class DynamoDB:
    def __init__(self, client):
        self._client = client
        """ :type : pyboto3.dynamodb """


    def create_table(self, table, attribute_definitions, key_schema, iops):
        print('Creating dynamodb...')
        return self._client.create_table(
            TableName=table,
            AttributeDefinitions=attribute_definitions,
            KeySchema=key_schema,
            ProvisionedThroughput=iops
        )

    def describing_dynamo_table(self, table_name):
        print('describing the current dynamo table..')
        return self._client.describe_table(TableName=table_name)

    def update_dynamo_table(self, table_name, read_capacity, write_capacity):
        print('updating the dynamo table')
        return self._client.update_table(
            TableName=table_name,
            ProvisionedThroughput={
                'ReadCapacityUnits': read_capacity,
                'WriteCapacityUnits': write_capacity
            }
        )
    def delete_dynamo_db(self, table):
        print('deleting the dynamo table')
        return self._client.delete_table(TableName=table)