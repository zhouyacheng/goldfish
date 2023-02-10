use goldfish_dwd;

create table dwd_alertmanager
(
    user_id                      bigint,
    username                     string,
    first_name                   string,
    email                        string,
    project_id                   bigint,
    project_name                 string,
    project_role                 string,
    alertmanager_project_id      bigint,
    receiver                     string,
    job                          string,
    fingerprint                  string,
    status                       string,
    alertname                    string,
    instance                     string,
    description                  string,
    summary                      string,
    severity                     string,
    groupkey                     string,
    start_time                   string,
    end_time                     string
) comment '告警用户|项目|事件表'
    row format delimited fields terminated by '\t';


use new_goldfish_dwd;

create table new_goldfish_dwd.dwd_alertmanager
(
    user_id                      bigint,
    username                     string,
    mobile                       string,
    email                        string,
    project_id                   bigint,
    project_name                 string,
    project_role                 string,
    alertmanager_project_id      bigint,
    receiver                     string,
    job                          string,
    fingerprint                  string,
    status                       string,
    alertname                    string,
    instance                     string,
    description                  string,
    summary                      string,
    severity                     string,
    groupkey                     string,
    start_time                   string,
    end_time                     string
) comment '告警用户|项目|事件表'
    row format delimited fields terminated by '\t';