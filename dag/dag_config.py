from datetime import datetime, timedelta
import pytz

origin_run_date = datetime.now(pytz.timezone('Asia/Shanghai'))
run_date = origin_run_date.strftime("%Y%m%d")
bizdate = run_date
yesterday = (origin_run_date + timedelta(days=-1)).strftime("%Y%m%d")
print(run_date,bizdate,yesterday)
