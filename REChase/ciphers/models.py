from django.db import models
import datetime
# Create your models here.


def upload_location(instance, filename, **kwargs):
    file_path = 'ciphers/{stage}/{time}-{filename}'.format(
        stage=str(instance.id), time=str(datetime.datetime.now().strftime("%H%M%S%f")), filename=filename
    )
    print(file_path)
    return file_path


class Cipher(models.Model):
    #questionno
    question=models.TextField(blank=True)
    answer=models.CharField(max_length=256,blank=False)
    crossword = models.ImageField(
        upload_to=upload_location,
        null=True
    )
    # image2 = models.ImageField(upload_to=upload_location,
    #                            null=True,
    #                            blank=True,
    #                            )
    hint = models.FileField(upload_to=upload_location,
                            null=True,
                            blank=True
                            )
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    accuracy = models.FloatField(default=0)
    modal = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'Cipher question- {}'.format(self.id)

    def calcAccu(self):
        self.accuracy=round(self.correct / (float(self.correct + self.wrong)), 2) * 100

    def answered(self,right=1):
        if right:
            self.correct=self.correct+1
        else:
            self.wrong=self.wrong+1
        self.calcAccu()
        self.save()
