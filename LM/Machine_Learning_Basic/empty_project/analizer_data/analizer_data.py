import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns


from loger import logger

class AnalaizerData():
    def __init__(self, dataset):
        self.dataset = dataset

        self.report_foldet = "data_report"
        if not os.path.exists(self.report_foldet):
            logger.debug (f'Folder "{self.report_foldet}" has been created in {os.getcwd()}')
            os.makedirs(self.report_foldet)

        self.first_five_lines = self.dataset.head()
        self.rows, self.columns = self.dataset.shape
        self.missing_values = self.dataset.isnull().sum()

        self.indexList = self.dataset.keys()

        print(f'{self.missing_values}\n',
              f'{self.rows}\n',
              f'{self.columns}\n',
              f'{self.first_five_lines}\n',
              f'{self.indexList}\n')

        self.create_image_1()
    
    def create_image_1(self):
        print(self.dataset.keys())
        plt.style.use('seaborn-v0_8')
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))

        # Гистограмма с seaborn
        sns.histplot(data=self.dataset, x='total_bill', bins=20, ax=axes[0], kde=True)
        axes[0].set_title('Распределение total_bill (Seaborn)')
        axes[0].set_xlabel('Total Bill')
        axes[0].set_ylabel('Частота')


        # Гистограмма с matplotlib
        axes[1].hist(self.dataset['total_bill'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
        axes[1].axvline(self.dataset['total_bill'].mean(), color='red', linestyle='--', linewidth=2, label=f'Среднее: {self.dataset["total_bill"].mean():.2f}')
        axes[1].axvline(self.dataset['total_bill'].median(), color='green', linestyle='--', linewidth=2, label=f'Медиана: {self.dataset["total_bill"].median():.2f}')
        axes[1].set_title('Распределение total_bill (Matplotlib)')
        axes[1].set_xlabel('Total Bill')
        axes[1].set_ylabel('Частота')
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)
        plt.tight_layout()

        fig.savefig(os.path.join(self.report_foldet,"1_img.png"))
        plt.close(fig)
