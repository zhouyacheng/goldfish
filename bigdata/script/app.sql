set spark.sql.shuffle.partitions=8;

insert into goldfish_app.app_alertmanager_user_result
select
    user_id,
    username,
    job,
    count(job) as job_cnt,
    date(start_time) as dt
from goldfish_dwd.dwd_alertmanager
group by user_id,username,job,date(start_time)
order by user_id,job,dt
;


insert into goldfish_app.app_alertmanager_job_status_result
select
    job,
    status,
    alertname,
    count(job) as job_cnt,
    date(start_time) as dt
from goldfish_dwd.dwd_alertmanager
group by job,status,alertname,date(start_time)
order by job,dt
;


insert into goldfish_app.app_alertmanager_job_result
select
    job,
    count(job) as job_cnt,
    date(start_time) as dt
from goldfish_dwd.dwd_alertmanager
group by job,date(start_time)
order by job,dt
;