import os
import datetime
import pandas as pd
from azure.storage.blob import BlobServiceClient
from database import get_daily_data

def generate_daily_report(df):
    if df.empty:
        return "No data available for the report."
    
    df['start_time'] = pd.to_datetime(df['start_time'])
    df['end_time'] = pd.to_datetime(df['end_time'])
    df['lunch_break'] = pd.to_timedelta(df['lunch_break'])
    # Calculates the total work duration for each row by subtracting start time and lunch break from end time.
    df['work_duration'] = df['end_time'] - df['start_time'] - df['lunch_break']
    df['date'] = df['start_time'].dt.date

    today_str = datetime.date.today().isoformat()
    report_lines = [f"Working Hours Report today ({today_str}):\n"]
    daily = df.groupby(['consultant_name', 'date'])['work_duration'].sum()
    for (consultant, date), duration in daily.items():
        total_seconds = int(duration.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes = remainder // 60
        report_lines.append(f"{consultant} on {date}: {hours}h {minutes}m")

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
    report_file = "consultant_daily_report.txt"
    raw_data = get_daily_data()
    df = pd.DataFrame(raw_data)
    # just to show columns
    print("DataFrame columns:", df.columns.tolist())

    report = generate_daily_report(df)
    # write to file
    with open(report_file, "w") as f:
        f.write(report)
    print(f"Report written to {report_file}")
    
    # upload_to_blob(report_file, report_file)
    # print("Report generated and uploaded.")