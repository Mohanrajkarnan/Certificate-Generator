from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.storage.blob import BlobServiceClient, BlobClient
from settings import  AZURE_SUBSCRIPTION_ID

credential = AzureCliCredential()


# ****************** RESOURCE GROUP CLIENT BEGIN **********************************

# resource_client = ResourceManagementClient(credential, AZURE_SUBSCRIPTION_ID)
# rg_result = resource_client.resource_groups.list()
# for item in rg_result:
#     print(item.properties)

# ****************** RESOURCE GROUP CLIENT ENDS **********************************



# ****************** STORAGE MANAGEMENT CLIENT BEGIN **********************************

storage_client = StorageManagementClient(credential, AZURE_SUBSCRIPTION_ID)
list_of_acc = storage_client.storage_accounts.list()

# for acc in list_of_acc:
#     print("***********")
#     print(acc)
#     print("***********")
    


# blob_service_client
# blob_service_client = BlobServiceClient(
#     account_url= 'https://covidreportingaccount.blob.core.windows.net/',
#     credential= credential
# )

blob_service_client = BlobServiceClient.from_connection_string(
    "DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=covidreportingaccount;" \
    "AccountKey=vtydr9yslqZQuyo+vLyP813lOH30wAPdWn1FXsg2WxVooWDVS5G+VsFbfZDHHsHhtIxc2qNfOhYz+AStLBgZZA==;" \
    "BlobEndpoint=https://covidreportingaccount.blob.core.windows.net/;FileEndpoint=https://covidreportingaccount.file.core.windows.net/" \
    ";QueueEndpoint=https://covidreportingaccount.queue.core.windows.net/;TableEndpoint=https://covidreportingaccount.table.core.windows.net/"
    )


print("************************Done**********************")
container_client = blob_service_client.get_container_client(container="population")
for blob_list in container_client.list_blob_names():
    print("***********")
    print(blob_list)
    print("***********")

# ******************STORAGE MANAGEMENT CLIENT ENDS **********************************
