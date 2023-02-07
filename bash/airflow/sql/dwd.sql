set spark.sql.shuffle.partitions=8;

insert into table goldfish_dwd.dwd_alertmanager
select
    gu.id as user_id,
    gu.username,
    gu.first_name,
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
from goldfish_ods.`user` gu
left join goldfish_ods.alertmanager_project gap
    on gu.id = gap.user_id
left join goldfish_ods.alertmanager ga
    on gap.id = ga.project_id
;