#### Overview
- 自动化运维平台,智能化管理服务器及自定义流水线进行定制化的管理CI/CD
- 第二版计划集成spark, 以local方式提交spark任务,接管从文件向数据库导入资产



#### Architecture

| 组件                 | 版本   |
| -------------------- | ------ |
| Python               | 3.10.2 |
| Mysql                | 5.7.28 |
| Redis                | 5.0.8  |
| Mongodb              | 5.0.14 |
| Django               | 4.0.3  |
| Django RestframeWork | 3.13.1 |
| Celery               | 5.2.3  |
| Kubernetes           | 1.25   |



#### Features

1. 资产管理(CMDB)
2. 远程连接跳板机对已注册到资产管理的服务器发送命令进行管理(jumpserver)
3. Ansible集成, 支持playbook及role的模板定义. 模板文件集成git管理,代码托管在gitea平台,每次执行任务时自动从gitea平台下载对应git tag的模板代码执行ansible任务
4. Celery集成, 支持后台及并发执行ansible任务
5. 定时任务集成, 支持定时调度ansible任务
6. ansible任务执行结果及日志以websocket的方式实时返回
7. Kubernets资源管理
8. 自定义流水线支持自定义CI/CD,每条流水线按照stage拆分为不同阶段(例: 打包,测试环境发布,生产环境发布...)执行对应任务
9. CI/CD流水线任务通过celery后台运行及监控任务执行状态及报错



#### API Local Doc

[Codebook API.yaml](Codebook%20API.yaml)



#### API Web Doc

`http://127.0.0.1:8000/doc/swagger`
![img.png](img.png)
![img_1.png](img_1.png)
![img_2.png](img_2.png)
![img_3.png](img_3.png)![img_4.png](img_4.png)



#### API AuthToken

  POST request `http://127.0.0.1:8000/api/login/`
- body: {"username":"xxx", "password":"xxx"}
- response: { "token": "e059222ff3a4469c987a1fcddc0f90b0", "expired_time": "2023-01-28T16:33:14.886134+08:00"}



#### Configuration

settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xxx',
        'USER': 'xxx',
        'PASSWORD': 'xxx',
        'HOST': 'xxx',
        'PORT': '3306',
    }
}


from pathlib import Path
MEDIA_ROOT = Path("/tmp")
# ansible work dir
IAC_WORK_DIR = Path("/tmp/work")

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://host:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "password",
        }
    },
    # 提供给xadmin或者admin的session存储
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://host:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "password",
        }
    },
    "celery": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://host:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "password",
        }
    },
}

# celery
CELERY_RESULT_BACKEND = "django-cache"
CELERY_CACHE_BACKEND = "celery"
CELERY_BROKER_URL = "redis://:password@host:6379/1"
CELERY_TASK_ROUTES = {
    "iac.tasks.*" : {"queue": "iac-1"},
    "k8s.tasks.*" : {"queue": "k8s-1"},
}



CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": ["redis://:password@host:6379/0",],
        },
    },
}

# kubernetes模板执行目录
TEMPLATE_DIR = "/Users/zyc/PycharmProjects/codebook/k8s/k8s-files/template/hello-minikube"


MONGODB_DATABASES = {
    "name": "cmdb",
    "host": "host",
    "port": 27017,
    "tz_aware": True,
    "username": "user",
    "password": "password"
}

# 默认为当前项目根目录
JUMPSERVER_UPLOADS_DIR = BASE_DIR / "upload"

```



#### Create User

```python
python3 manage.py createsuperuser 
```



#### Start Celery

```shell
# 监听定时任务
celery -A codebox beat  -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

# 启动celery
celery -A codebox worker  -l INFO -Q iac-1  # ansible任务运行队列
celery -A codebox worker  -l INFO -Q k8s-1  # k8s任务运行队列

```