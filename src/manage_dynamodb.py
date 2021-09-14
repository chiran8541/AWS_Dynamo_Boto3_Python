from src.Client_Factory import DynamoDBClient
from src.dynamodb import DynamoDB

def get_dynamodb():
    dynamo_client = DynamoDBClient().get_client()
    dynamo = DynamoDB(dynamo_client)
    return dynamo


def create_dynamo_table():
    dynamo_client = DynamoDBClient().get_client()
    dynamo = DynamoDB(dynamo_client)

    table_name = 'Movies'
    """ :type : pyboto3.dynamodb """

    # defining aributes
    attribute_definitions = [
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        }
    ]
    #Key Schema definitions
    key_schema = [
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  # Sort key
        }
    ]

    initial_iops = {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }

    dynamo_create_table_response = dynamo.create_table(table_name, attribute_definitions, key_schema, initial_iops)
    print('created dynamo db with name: ' + table_name + ":" + str(dynamo_create_table_response))

def show_tables():
    response = get_dynamodb().describing_dynamo_table("Movies")
    print(response['Table']['TableStatus'],response['Table']['TableName'])

def update_tables():
    get_dynamodb().update_dynamo_table('Movies', 10, 10)

def delete_table():
    response = input('Are you willing to delete Y/N:  ')
    if response == 'Y':
        get_dynamodb().delete_dynamo_db('Movies')
        print('table deleted')
    else:
        print('okay , will not delete')
if __name__ == '__main__':
    #show_tables()
    #update_tables()
    #create_dynamo_table()
    delete_table()

