use goldfish_app;

create table goldfish_app.app_alertmanager_user_result
(
    user_id                      bigint,
    username                     string,
    job                          string,
    job_cnt                      bigint,
    dt                           string
) comment '告警用户|项目|事件表'
    row format delimited fields terminated by '\t';


create table goldfish_app.app_alertmanager_job_status_result
(
    job                          string,
    status                       string,
    alertname                    string,
    status_cnt                   bigint,
    dt                           string
) comment '告警状态统计表'
    row format delimited fields terminated by '\t';

create table goldfish_app.app_alertmanager_job_result
(
    job                          string,
    job_cnt                      bigint,
    dt                           string
) comment '告警状态统计表'
    row format delimited fields terminated by '\t';

use new_goldfish_app;
create table new_goldfish_app.app_alertmanager_user_result
(
    user_id                      bigint,
    username                     string,
    job                          string,
    job_cnt                      bigint,
    dt                           string
) comment '告警用户|项目|事件表'
    row format delimited fields terminated by '\t';


create table new_goldfish_app.app_alertmanager_job_status_result
(
    job                          string,
    status                       string,
    alertname                    string,
    status_cnt                   bigint,
    dt                           string
) comment '告警状态统计表'
    row format delimited fields terminated by '\t';

create table new_goldfish_app.app_alertmanager_job_result
(
    job                          string,
    job_cnt                      bigint,
    dt                           string
) comment '告警状态统计表'
    row format delimited fields terminated by '\t';