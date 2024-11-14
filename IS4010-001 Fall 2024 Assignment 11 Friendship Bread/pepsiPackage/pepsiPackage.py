
#Pepsi Package

def remove_pepsi_rows(self):
        anomalies = self.df[self.df['Item'] == 'Pepsi']
        self.df = self.df[self.df['Item'] != 'Pepsi']
        self.save_to_csv(anomalies, 'dataAnomalies.csv')