import csv
import os
from abc import ABC, abstractmethod
 
class Read(ABC):

    def __init__(self, dataset):
        self.dataset = os.getcwd() + dataset
        super().__init__()
    
    @abstractmethod
    def read(self):
        fields = [] 
        rows = []
        with open(self.dataset, 'r') as csvfile: 

            csvreader = csv.reader(csvfile) 
            fields = next(csvreader) 
  
            for row in csvreader: 
                rows.append(row) 

        for row in rows[:csvreader.line_num]: 
            n = 0
            for col in row: 
                print(fields[n]+": "+col), 
                n = n + 1
            print('\n') 