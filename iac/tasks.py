from celery import shared_task
from .models import Task,TaskState,Repository,Release,PeriodTask
from .runner import TaskRunner


@shared_task
def add(x, y):
    return x + y

@shared_task
def execute_task(task_id: int):
    instance = Task.objects.filter(pk=task_id).first()
    if instance and instance.state == TaskState.PENDING:
        TaskRunner(instance).execute()

@shared_task
def execute_period_task(period_task_id: int):
    period_task :PeriodTask = PeriodTask.objects.filter(pk=period_task_id,is_deleted=0,enabled=True).first()
    if period_task:
        instance = Task.objects.create(
            release=period_task.release,
            playbook=period_task.playbook,
            role=period_task.role,
            inventories=period_task.inventories,
            envvars=period_task.envvars,
            extravars=period_task.extravars,
            forks=period_task.forks,
            timeout=period_task.timeout,
            created_by=period_task.created_by,
            updated_by=period_task.updated_by,
            period=period_task,
        )
        instance.save()
        if instance and instance.state == TaskState.PENDING:
            execute_task.delay(instance.pk)
@shared_task
def sync_gitea_release(repository_id: int,user_id):
    instance = Repository.objects.filter(pk=repository_id).first()
    if not instance:
        return
    latest_release_instance: Release = Release.objects.filter(repository_id=repository_id).first()
    lower = None
    if latest_release_instance:
        lower = latest_release_instance.version
    try:
        for tag in instance.provider.tags(lower=lower):
            Release.objects.create(
                repository=instance,
                archive_url=tag.archive_url,
                commit=tag.commit,
                major=tag.version.major,
                minor=tag.version.minor,
                micro=tag.version.micro,
                created_by_id=user_id,
                updated_by_id=user_id,
            ).save()
    except (ValueError, Exception) as e:
        print(str(e))
        return str(e)

@shared_task
def sync_all_release(repository_id: int,user_id):
    for repository in Repository.objects.filter(pk=repository_id):
        if not repository:
            return
        sync_gitea_release.delay(repository.pk,user_id)