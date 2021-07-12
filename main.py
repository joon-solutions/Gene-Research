import pandas as pd

def check(row):
    return list(row['Log₂ fold change'])[0] > 0.5 and list(row['P-value'])[0] < 0.05


class Gene():
    def __init__(self) -> None:
        cols = [3, 9, 11]
        self.df_U1T1 = pd.read_excel ('U1_vs_T1.xlsx', sheet_name='Sheet1', usecols=cols)
        self.df_U20T76 = pd.read_excel ('U20_vs_T76.xlsx', sheet_name='U20_vs_T76', usecols=cols)
        self.df_U1T76 = pd.read_excel ('U1_vs_T76.xlsx', sheet_name='Sheet1', usecols=cols)
        self.df_U1U20 = pd.read_excel ('U1_vs_U20.xlsx', sheet_name='Sheet1', usecols=cols)
    
    def main(self):
        name = input("Please insert name: ")
        row_U1T1 = self.df_U1T1.loc[self.df_U1T1['KEGG Gene ID'] == name]
        row_U20T76 = self.df_U20T76.loc[self.df_U20T76['KEGG Gene ID'] == name]
        row_U1T76 = self.df_U1T76.loc[self.df_U1T76['KEGG ID'] == name]
        row_U1U20 = self.df_U1U20.loc[self.df_U1U20['KEGG Gene ID'] == name]

        if len(row_U1T1) == 0 or len(row_U20T76) == 0 or len(row_U1T76) == 0 or len(row_U1U20) == 0:
            # print("Aborted, lack of data!")
            return "No, non-significance"

        if check(row_U1T1):
            if check(row_U20T76):
                if check(row_U1T76):
                    if not check(row_U1U20):
                        return "Medium: MOA or Process-related"
                    else:
                        return "MOA-related"
                else:
                    if not check(row_U1U20):
                        return "MOA-related, but effect is age-dependent"
                    else:
                        return "Inconclusive"
            else:
                if check(row_U1T76):
                    if not check(row_U1U20):
                        return "MOA-related, but effect is age-dependent"
                    else:
                        return "Inconclusive"
                else:
                    if not check(row_U1U20):
                        return "MOA-related, but effect is age-dependent"
                    else:
                        return "Inconclusive"
        else:
            if not check(row_U20T76):
                if check(row_U1T76):
                    if check(row_U1U20):
                        return "Age-related, but effect can be treatment-dependent"
                    else:
                        return "Inconclusive"
                else:
                    if check(row_U1U20):
                        return "Age related"
                    else:
                        return "Inconclusive"
            else:
                return "Inconclusive"


gene_research = Gene()
print(gene_research.main())
