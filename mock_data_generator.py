"""
Mock Data Generator for RemitGuard Pipeline
Generates transaction and UX event log datasets and uploads them to Azure Blob Storage.
"""

import os
import json
import csv
from io import StringIO
from datetime import datetime, timedelta
import random
from faker import Faker
import pandas as pd
from azure.storage.blob import BlobServiceClient


# Configuration
AZURE_STORAGE_CONNECTION_STRING = os.getenv('AZURE_STORAGE_CONNECTION_STRING', '')
if not AZURE_STORAGE_CONNECTION_STRING:
    raise ValueError("AZURE_STORAGE_CONNECTION_STRING environment variable not set")
TRANSACTIONS_CONTAINER = 'transactions'
UX_LOGS_CONTAINER = 'ux-event-logs'
NUM_TRANSACTIONS = 1000
NUM_UX_EVENTS = 5000


class MockDataGenerator:
    """Generates mock transaction and UX event log data."""
    
    def __init__(self):
        self.fake = Faker()
        self.destinations = ['Zimbabwe', 'Malawi', 'Mozambique', 'Botswana', 'Namibia']
        self.device_types = ['Android', 'iOS', 'USSD']
        self.actions = ['app_open', 'rate_calculated', 'transfer_initiated', 'transfer_completed']
        self.statuses = ['Success', 'Failed', 'Pending']
    
    def generate_transactions(self, num_records=NUM_TRANSACTIONS):
        """Generate mock transaction data."""
        transactions = []
        base_time = datetime.now() - timedelta(days=30)
        
        for i in range(num_records):
            transaction = {
                'transaction_id': f'TXN-{datetime.now().strftime("%Y%m%d")}-{i:06d}',
                'sender_id': f'USR-{random.randint(1000, 9999)}',
                'source_country': 'South Africa',
                'destination_country': random.choice(self.destinations),
                'amount_zar': round(random.uniform(100, 50000), 2),
                'exchange_rate': round(random.uniform(0.05, 0.15), 4),
                'status': random.choice(self.statuses),
                'timestamp': (base_time + timedelta(seconds=random.randint(0, 86400 * 30))).isoformat()
            }
            transactions.append(transaction)
        
        return pd.DataFrame(transactions)
    
    def generate_ux_event_logs(self, num_records=NUM_UX_EVENTS):
        """Generate mock UX event log data."""
        ux_events = []
        base_time = datetime.now() - timedelta(days=30)
        
        for i in range(num_records):
            event = {
                'user_id': f'USR-{random.randint(1000, 9999)}',
                'session_id': f'SESSION-{self.fake.uuid4()}',
                'device_type': random.choice(self.device_types),
                'action': random.choice(self.actions),
                'timestamp': (base_time + timedelta(seconds=random.randint(0, 86400 * 30))).isoformat()
            }
            ux_events.append(event)
        
        return pd.DataFrame(ux_events)
    
    def dataframe_to_csv(self, df):
        """Convert DataFrame to CSV string."""
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        return csv_buffer.getvalue()
    
    def dataframe_to_json(self, df):
        """Convert DataFrame to JSON string."""
        return df.to_json(orient='records', indent=2)


class AzureBlobUploader:
    """Handles uploading files to Azure Blob Storage."""
    
    def __init__(self, connection_string):
        """Initialize blob service client."""
        if not connection_string:
            raise ValueError(
                'AZURE_STORAGE_CONNECTION_STRING environment variable is not set. '
                'Please configure your Azure Storage connection string.'
            )
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    
    def ensure_container_exists(self, container_name):
        """Create container if it doesn't exist."""
        try:
            self.blob_service_client.create_container(name=container_name)
            print(f"✓ Container '{container_name}' created successfully")
        except Exception as e:
            if 'ContainerAlreadyExists' in str(e):
                print(f"✓ Container '{container_name}' already exists")
            else:
                raise
    
    def upload_blob(self, container_name, blob_name, data, content_type='text/csv'):
        """Upload data to blob storage."""
        try:
            container_client = self.blob_service_client.get_container_client(container=container_name)
            container_client.upload_blob(name=blob_name, data=data, overwrite=True)
            print(f"✓ Uploaded: {blob_name} to container '{container_name}'")
            return True
        except Exception as e:
            print(f"✗ Error uploading {blob_name}: {str(e)}")
            return False
    
    def upload_transactions(self, df):
        """Upload transactions dataset in CSV format."""
        self.ensure_container_exists(TRANSACTIONS_CONTAINER)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        csv_data = df.to_csv(index=False)
        blob_name = f'transactions_{timestamp}.csv'
        return self.upload_blob(TRANSACTIONS_CONTAINER, blob_name, csv_data, 'text/csv')
    
    def upload_ux_logs(self, df):
        """Upload UX event logs dataset in JSON format."""
        self.ensure_container_exists(UX_LOGS_CONTAINER)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        json_data = df.to_json(orient='records', indent=2)
        blob_name = f'ux_events_{timestamp}.json'
        return self.upload_blob(UX_LOGS_CONTAINER, blob_name, json_data, 'application/json')


def main():
    """Main execution function."""
    print("=" * 60)
    print("RemitGuard Pipeline - Mock Data Generator")
    print("=" * 60)
    
    try:
        # Generate mock data
        print("\n[1/3] Generating mock datasets...")
        generator = MockDataGenerator()
        
        transactions_df = generator.generate_transactions(NUM_TRANSACTIONS)
        ux_logs_df = generator.generate_ux_event_logs(NUM_UX_EVENTS)
        
        print(f"✓ Generated {len(transactions_df)} transaction records")
        print(f"✓ Generated {len(ux_logs_df)} UX event records")
        
        # Save locally for reference
        print("\n[2/3] Saving datasets locally...")
        transactions_csv = 'transactions_local.csv'
        ux_logs_json = 'ux_events_local.json'
        
        transactions_df.to_csv(transactions_csv, index=False)
        ux_logs_df.to_json(ux_logs_json, orient='records', indent=2)
        
        print(f"✓ Saved local copy: {transactions_csv}")
        print(f"✓ Saved local copy: {ux_logs_json}")
        
        # Upload to Azure Blob Storage
        print("\n[3/3] Uploading to Azure Blob Storage...")
        if not AZURE_STORAGE_CONNECTION_STRING:
            print("⚠ Warning: AZURE_STORAGE_CONNECTION_STRING not set. Skipping cloud upload.")
            print("  To enable uploads, set the AZURE_STORAGE_CONNECTION_STRING environment variable.")
        else:
            uploader = AzureBlobUploader(AZURE_STORAGE_CONNECTION_STRING)
            uploader.upload_transactions(transactions_df)
            uploader.upload_ux_logs(ux_logs_df)
        
        print("\n" + "=" * 60)
        print("✓ Mock data generation completed successfully!")
        print("=" * 60)
        
        # Display sample data
        print("\nSample Transactions:")
        print(transactions_df.head(3).to_string())
        print("\nSample UX Events:")
        print(ux_logs_df.head(3).to_string())
        
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        raise


if __name__ == '__main__':
    main()
