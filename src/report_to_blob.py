import os
import datetime
import pandas as pd
from azure.storage.blob import BlobServiceClient
from database import get_daily_data
from dotenv import load_dotenv

load_dotenv()

def generate_daily_report(df, today_str):
    if df.empty:
        return "No data available for the report."

    df['start_time'] = pd.to_datetime(df['start_time'])
    df['end_time'] = pd.to_datetime(df['end_time'])
    df['lunch_break'] = pd.to_timedelta(df['lunch_break'])
    df['work_duration'] = df['end_time'] - df['start_time'] - df['lunch_break']
    df['date'] = df['start_time'].dt.date

    report_lines = [f"Working Hours Report today ({today_str}):\n"]
    daily = df.groupby(['consultant_name', 'date'])['work_duration'].sum()
    for (consultant, date), duration in daily.items():
        total_seconds = int(duration.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes = remainder // 60
        report_lines.append(f"{consultant} on {date}: {hours}h {minutes}m")

    report_lines.append("\nCumulative working hours grouped by customer for all consultants:")
    customer_grouped = df.groupby(['customer_name'])['work_duration'].sum()
    for customer, duration in customer_grouped.items():
        total_seconds = int(duration.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes = remainder // 60
        report_lines.append(f"{customer}: {hours}h {minutes}m")

    return "\n".join(report_lines)

def upload_to_blob(file_path, blob_name):
    connection_string = os.environ.get("AZURE_STORAGE_CONNECTION_STRING")
    container_name = os.environ.get("AZURE_CONTAINER_NAME")
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    print(f"Uploaded {blob_name} to Azure Blob Storage.")

if __name__ == "__main__":
    today = datetime.date.today()
    today_str = today.isoformat()

    raw_data = get_daily_data()
    df = pd.DataFrame(raw_data)
    print("DataFrame columns:", df.columns.tolist())

    report = generate_daily_report(df, today_str)
    file_name = f"{today_str}_consultant_daily_report.txt"

    with open(file_name, "w") as f:
        f.write(report)
    print(f"Report written to {file_name}")

    upload_to_blob(file_name, file_name)
    print("Report generated and uploaded.")
