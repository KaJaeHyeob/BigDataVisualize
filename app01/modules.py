import os
import csv
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from django.conf import settings
from django.urls import path
from .models import FileRequest, ImageResponse


matplotlib.use('Agg')
matplotlib.style.use('ggplot')


def visualizing():
    fileList = os.listdir(settings.MEDIA_ROOT + 'file/')

    with open(settings.MEDIA_ROOT + 'file/' + fileList[0], mode='rb') as csvFile:
        fileDB = FileRequest.objects.all().order_by('-time')
        path = 'image/' + fileDB[0].title + '.jpg'

        reader = pd.read_csv(csvFile)
        fig = sns.pairplot(reader, hue='Species')
        fig.savefig(settings.MEDIA_ROOT + path)

        image = ImageResponse(imagePath=path, title=fileDB[0].title)
        image.save()

