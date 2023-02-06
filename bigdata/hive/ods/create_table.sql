use goldfish_ods;

create table `user`
(
    id          bigint,
    username    string,
    first_name  string,
    email       bigint
) comment '用户表'
    row format delimited fields terminated by '\t';


create table alertmanager_project
(
    id        bigint,
    name      string,
    role      string,
    user_id   bigint
) comment '交付项目表'
    row format delimited fields terminated by '\t';


create table alertmanager
(
    id            bigint,
    project_id    int,
    receiver      string,
    job           string,
    fingerprint   string,
    status        string,
    alertname     string,
    instance      string,
    description   string,
    summary       string,
    severity      string,
    groupkey      string,
    start_time    string,
    end_time      string
) comment '告警事件表'
    row format delimited fields terminated by '\t';