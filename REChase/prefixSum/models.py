from django.db import models


class PrefixSum(models.Model):
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    accuracy = models.FloatField(default=0)
    modal = models.TextField(null=True, blank=True)
    modal1 = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'That question regarding prefix sum encoding'

    def calcAccu(self):
        self.accuracy = round(self.correct / (float(self.correct + self.wrong)), 2) * 100

    def answered(self, right=1):
        if right:
            self.correct = self.correct + 1
        else:
            self.wrong = self.wrong + 1
        self.calcAccu()
        self.save()


class Used(models.Model):
    word = models.CharField(max_length=12, unique=True)
