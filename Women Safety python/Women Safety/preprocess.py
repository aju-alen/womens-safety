import pandas as pd
import os
# df=pd.read_csv("mhealth_raw_data.csv")
# print(df.head(10))
# print(df["Activity"])
for i in os.listdir('MHEALTHDATASET/'):
  if i not in ('README.txt'):
    print(i)
df = pd.DataFrame()
#loop to combine all data
for i in range(1,11):
    df1 = pd.read_csv(f'MHEALTHDATASET/mHealth_subject{i}.log', header=None, sep='\t')
    df1 = df1.loc[:, [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]]
    

    df1 = df1.rename(columns={
        0:"acx",1:"acy",2:"acz",3:"ecl1",4:"ecl2",5:"alax",6:"alay",7:"alaz",8:"glax",9:"glay",10:"glaz",11:"mglax",12:"mglay",13:"mglaz",14:"arax",15:"aray",16:"araz",17:"grax",18:"gray",19:"graz",20:"mgrax",21:"mgray",22:"mgraz",23:"label"
        })

    # df1['subject'] = 'subject'+str(i)
    # df = pd.concat([df,df1])
print(df1)
df1.to_csv('dataset.csv',index = False)