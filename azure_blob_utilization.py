# azure_blob_utilization.py

from azure.storage.blob import BlobServiceClient
import os

def list_containers_and_sizes(account_url, credential):
    blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)
    containers = blob_service_client.list_containers()

    for container in containers:
        print(f"Container: {container['name']}")
        container_client = blob_service_client.get_container_client(container['name'])
        blobs = container_client.list_blobs()

        total_size = 0
        folder_sizes = {}

        for blob in blobs:
            total_size += blob.size
            folder = os.path.dirname(blob.name)
            if folder not in folder_sizes:
                folder_sizes[folder] = 0
            folder_sizes[folder] += blob.size

        print(f"Total Size: {total_size} bytes")
        for folder, size in folder_sizes.items():
            print(f"Folder: {folder}, Size: {size} bytes")

if __name__ == "__main__":
    account_url = os.getenv("AZURE_STORAGE_ACCOUNT_URL")
    credential = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")
    list_containers_and_sizes(account_url, credential)
