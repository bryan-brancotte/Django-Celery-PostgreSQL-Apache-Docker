import json

from django.db import models
from django.urls import reverse

from composeexample import settings


class Author(models.Model):
    name = models.CharField(max_length=200)
    __original_name = None
    statistics_str = models.TextField(
        default='{}',
        blank=True,
        null=True,
    )

    def get_absolute_url(self):
        return reverse('myapp:author-detail', kwargs={'pk': self.pk})

    def _get_statistics(self):
        return json.loads(self.statistics_str)

    def _set_statistics(self, command):
        self.statistics_str = json.dumps(command)

    statistics = property(_get_statistics, _set_statistics)

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super(Author, self).__init__(*args, **kwargs)
        self.__original_name = self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Author, self).save(force_insert=force_insert, force_update=force_update, using=using,
                                 update_fields=update_fields)
        if self.__original_name != self.name:
            from myapp import tasks
            if settings.CELERY_ENABLED:
                tasks.compute_job.delay(pk=self.pk)
            else:
                tasks.compute_job(pk=self.pk)
