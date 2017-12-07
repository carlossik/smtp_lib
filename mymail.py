import pandas as pd
import MySQLdb
import csv
from sqlalchemy import create_engine
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.mime.application
import time
import settings



timestr = time.strftime("%A-%d%B%Y-%H%M%S")
filename = "Regression_test_resuls for " + " " + timestr+".xlsx"
job_ids = []
with open('C:\\Users\\carlos.attafuah\\Desktop\\Jmeter\\testdata_folder\\extract_job_details.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        id = str(row[1])
        job_ids.append(id)
def connect():
    timestr = time.strftime("%A-%d%B%Y-%H%M%S")
    conn = MySQLdb.connect(passwd="tli00eNND2ROLm:d,cq-", db="dspe", host="proteus.odin.tel-dev.io", port=3306,user="root")
    engine = create_engine('mysql+pymysql://root:tli00eNND2ROLm:d,cq-@proteus.odin.tel-dev.io:3306/dspe')
    sql = "select jt.job_id ,s.parent_platform as Vendor,jt.vendor_data_type,jt.id as TaskId,jt.create_time as CreatedTime,jt.job_start_time as StartedTime,jt.job_completion_time,j.status,jt.worker_path,jt.status_message from dspe.job_task jt left JOIN dspe.job j on jt.job_id = j.id left join dspe.job_config jc on jc.id = j.job_config_id left join dspe.seat s on s.id = jc.seat_id where jt.job_id in (%s)" % ",".join(
        map(str,job_ids))
    sql2 = "SELECT jc.id as jobConfigId, jtc.id as jobTaskConfigId, s.id as seat_id, s.platform_id, s.parent_platform, jtc.vendor_data_type, s.credential_type as type,s.data_storage_provider as provider,s.username,s.password,jc.enabled as config_enabled, s.enabled as seat_enabled, s.api_collector_version as default_or_not,jtc.job_task_type,jtc.write_to_kafka, jc.create_time as createTime, jc.update_time as UpdateTime,ss.bucket_name_pattern as bucket_pattern,ss.file_name_pattern,ss.file_name_pattern_regex,ss.folder_name_pattern FROM dspe.job_task_config jtc left join dspe.job_config jc on jc.id = jtc.job_config_id left join dspe.seat s on jc.seat_id = s.id LEFT JOIN dspe.seat_storage_config ss on ss.seat_id = s.id WHERE jtc.job_config_id in (%s)" % ",".join(map(str,job_ids))
    cur = conn.cursor()
    dframe = pd.read_sql(sql, engine)
    dframe2 = pd.read_sql(sql2,engine)

    with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
        myreport = dframe.to_excel(writer, sheet_name='Sheet1', index=None)

def send_report():
    # Create a text/plain message
    msg = email.mime.multipart.MIMEMultipart()
    msg['Subject'] = 'VIE Regression Test Results'
    msg['From'] = 'carlos.attafuah@theexchangelab.com'
    # The main body is just another attachment
    body = email.mime.text.MIMEText("""Please see the results of the test attached.""")
    msg.attach(body)
    #attachment
    fp = open(filename, 'rb')
    att = email.mime.application.MIMEApplication(fp.read(), _subtype="xlsx")
    fp.close()
    att.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(att)
    server = smtplib.SMTP('smtp.office365.com:587')
    server.starttls()
    server.login(settings.email,settings.password)
    recepient_list = ['carlossik@gmail.com','carlcraft.ltd@gmail.com','carlos.attafuah@theexchangelab.com','paavan.virdee@theexchangelab.com']
    server.sendmail('carlos.attafuah@theexchangelab.com', recepient_list, msg.as_string())
    server.quit()


connect()
send_report()

