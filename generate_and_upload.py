import pandas as pd
from faker import Faker
import random
from datetime import datetime
from azure.storage.blob import BlobServiceClient
import io

# Initialize Faker and Azure Client
import os
fake = Faker()
CONNECTION_STRING = os.getenv('AZURE_STORAGE_CONNECTION_STRING', '')
if not CONNECTION_STRING:
    raise ValueError("AZURE_STORAGE_CONNECTION_STRING environment variable not set")
CONTAINER_NAME = "telemetry"

try:
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
except Exception as e:
    print(f"Error connecting to Azure: {e}")
    exit()

def generate_mock_data(num_rows=100):
    # 1. Generate Transactions
    tx_data = []
    destinations = ['Zimbabwe', 'Malawi', 'Mozambique', 'Lesotho', 'Somalia']
    statuses = ['Success', 'Success', 'Success', 'Failed', 'Pending'] # Biased towards Success
    
    for _ in range(num_rows):
        tx_id = f"TXN-{fake.uuid4()[:8].upper()}"
        sender_id = f"SND-{random.randint(10000, 99999)}"
        dest = random.choice(destinations)
        amount = round(random.uniform(200.00, 5000.00), 2)
        
        # Simulated exchange rates relative to ZAR
        rate_map = {'Zimbabwe': 1.0, 'Malawi': 98.4, 'Mozambique': 3.5, 'Lesotho': 1.0, 'Somalia': 31.2}
        
        tx_data.append({
            'transaction_id': tx_id,
            'sender_id': sender_id,
            'source_country': 'South Africa',
            'destination_country': dest,
            'amount_zar': amount,
            'exchange_rate': rate_map[dest],
            'status': random.choice(statuses),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
    
    # 2. Generate Corresponding UX Logs
    ux_data = []
    actions = ['app_open', 'rate_calculated', 'transfer_initiated', 'transfer_completed']
    devices = ['Android', 'Android', 'iOS', 'USSD'] # More Android users typical for market
    
    for tx in tx_data:
        session_id = f"SES-{fake.uuid4()[:8].upper()}"
        
        # Simulate a user flow journey based on the transaction status
        for action in actions:
            # If transaction failed/pending, maybe they didn't complete the final step in logs
            if tx['status'] == 'Failed' and action == 'transfer_completed':
                if random.random() > 0.5: continue 
                
            ux_data.append({
                'user_id': tx['sender_id'],
                'session_id': session_id,
                'device_type': random.choice(devices),
                'action': action,
                'timestamp': tx['timestamp']
            })
            
    return pd.DataFrame(tx_data), pd.DataFrame(ux_data)

def upload_to_azure(df, folder_name, file_prefix):
    # Convert DataFrame to CSV in memory string
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    
    # Create unique filename using timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    blob_name = f"{folder_name}/{file_prefix}_{timestamp}.csv"
    
    # Upload to Azure
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob_name)
    blob_client.upload_blob(csv_buffer.getvalue(), overwrite=True)
    print(f" Successfully uploaded {blob_name} to Azure Storage!")

if __name__ == "__main__":
    print("Generating mock fintech data...")
    transactions_df, ux_logs_df = generate_mock_data(150)
    
    print("Uploading files to Azure Data Lake...")
    upload_to_azure(transactions_df, "transactions", "mock_transactions")
    upload_to_azure(ux_logs_df, "ux-logs", "mock_ux_logs")
    print("Done!")