set spark.sql.shuffle.partitions=8;

insert into table new_goldfish_dwd.dwd_alertmanager
select
    gu.id as user_id,
    gu.username,
    gu.mobile,
    gu.email,
    gap.id as project_id,
    gap.name as project_name,
    gap.role as project_role,
    ga.id as alertmanager_id,
    ga.receiver,
    ga.job,
    ga.fingerprint,
    ga.status,
    ga.alertname,
    ga.instance,
    ga.description,
    ga.summary,
    ga.severity,
    ga.groupkey,
    ga.start_time,
    ga.end_time
from new_goldfish_ods.`auth_user_rt` gu
left join new_goldfish_ods.alertmanager_project_rt gap
    on gu.id = gap.user_id
left join new_goldfish_ods.alertmanager_rt ga
    on gap.id = ga.project_id
;