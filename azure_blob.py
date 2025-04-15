from azure.storage.blob import BlobServiceClient

def upload_to_azure(file_path, connection_string, container_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_path)
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)
    print(f"Uploaded {file_path} to Azure")