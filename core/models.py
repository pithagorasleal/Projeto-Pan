from django.db import models

# Create your models here.

class Step(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

class Process(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

class ProcessStepConfig(models.Model):
    step = models.ForeignKey(Step, on_delete=models.PROTECT)
    process = models.ForeignKey(Process, on_delete=models.PROTECT)
    time = models.IntegerField()
    order = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.process, self.step)
