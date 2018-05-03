import time

from composeexample.celeryconf import app

from myapp.models import Author


@app.task
def compute_job(pk):
    print("Start : %s" % time.ctime())
    time.sleep(3)
    author = Author.objects.get(pk=pk)
    stats = {}
    for letter in author.name:
        try:
            stats[letter] += 1
        except KeyError:
            stats[letter] = 1
    author.statistics = stats
    author.save()
    print("End : %s" % time.ctime())
