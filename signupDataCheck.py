import pandas as pd
import re

df = pd.read_csv (r'C:\Users\jcooke\PycharmProjects\signupCheck\signupData2.1.21.csv')
df = df.sort_values(['Country Code (URL)', 'Event Action'])

dropList = ['progDistColdInfoClick', 'progDistColdRegClick', 'progDistInvtInfoClick', 'progDistInvtRegClick', 'progMembInvtInfoClick', 'progMembInvtRegClick']

df = df[~df['Event Action'].isin(dropList)]


sorter = ['legacyDistColdView', 'legacyDistColdIntent', 'legacyDistColdSubmit', 'legacyDistColdVerify', 'legacyDistColdComplete'
    , 'legacyCustColdView', 'legacyCustColdSubmit', 'legacyCustColdVerify', 'legacyCustColdComplete'
    , 'legacyMembColdView', 'legacyMembColdIntent', 'legacyMembColdSubmit', 'legacyMembColdVerify', 'legacyMembColdComplete'
    , 'legacyDistInvtView', 'legacyDistInvtIntent', 'legacyDistInvtSubmit', 'legacyDistInvtVerify', 'legacyDistInvtComplete'
    , 'legacyCustInvtView', 'legacyCustInvtSubmit', 'legacyCustInvtVerify', 'legacyCustInvtComplete'
    , 'legacyMembInvtView', 'legacyMembInvtIntent', 'legacyMembInvtSubmit', 'legacyMembInvtVerify', 'legacyMembInvtComplete'
    , 'poCustColdView', 'poCustColdIntent', 'poCustColdComplete'
    , 'simpDistColdView', 'simpDistColdIntent', 'simpDistColdFindAff', 'simpDistColdNextBttn', 'simpDistColdFormStart', 'simpDistColdComplete'
    , 'simpCustColdView', 'simpCustColdIntent', 'simpCustColdFindAff', 'simpCustColdNextBttn', 'simpCustColdFormStart', 'simpCustColdContactMe', 'simpCustColdComplete'
    , 'simpMembColdView', 'simpMembColdIntent', 'simpMembColdFindAff', 'simpMembColdNextBttn', 'simpMembColdFormStart', 'simpMembColdComplete'
    , 'simpDistInvtLanding', 'simpDistInvtAccept',  'simpDistInvtView', 'simpDistInvtIntent', 'simpDistInvtSubmit', 'simpDistInvtComplete', 'simpDistInvtError'
    , 'simpCustInvtLanding', 'simpCustInvtAccept', 'simpCustInvtView', 'simpCustInvtIntent', 'simpCustInvtSubmit', 'simpCustInvtComplete', 'simpCustInvtError'
    , 'simpMembInvtLanding', 'simpMembInvtAccept', 'simpMembInvtView', 'simpMembInvtIntent', 'simpMembInvtSubmit', 'simpMembInvtComplete', 'simpMembInvtError'
    , 'progDistColdView', 'progDistColdIntent', 'progDistColdComplete'
    , 'progCustColdView', 'progCustColdIntent', 'progCustColdComplete'
    , 'progMembColdView', 'progMembColdIntent', 'progMembColdComplete'
    , 'progMembInvtView', 'progMembInvtIntent', 'progMembInvtComplete'
    , 'progDistInvtView', 'progDistInvtComplete'
    , 'progCustInvtView', 'progCustInvtComplete']

conv = ['legacyDistColdView', 'legacyDistColdIntent', 'legacyDistColdComplete'
    , 'legacyCustColdView', 'legacyCustColdComplete'
    , 'legacyMembColdView', 'legacyMembColdIntent', 'legacyMembColdComplete'
    , 'legacyDistInvtView', 'legacyDistInvtIntent', 'legacyDistInvtComplete'
    , 'legacyCustInvtView', 'legacyCustInvtComplete'
    , 'legacyMembInvtView', 'legacyMembInvtIntent', 'legacyMembInvtComplete'
    , 'poCustColdView', 'poCustColdIntent', 'poCustColdComplete'
    , 'simpDistColdView', 'simpDistColdIntent', 'simpDistColdComplete'
    , 'simpCustColdView', 'simpCustColdIntent', 'simpCustColdComplete'
    , 'simpMembColdView', 'simpMembColdIntent', 'simpMembColdComplete'
    , 'simpDistInvtLanding', 'simpDistInvtAccept',  'simpDistInvtView', 'simpDistInvtIntent',  'simpDistInvtComplete'
    , 'simpCustInvtLanding', 'simpCustInvtAccept', 'simpCustInvtView', 'simpCustInvtIntent', 'simpCustInvtComplete'
    , 'simpMembInvtLanding', 'simpMembInvtAccept', 'simpMembInvtView', 'simpMembInvtIntent',  'simpMembInvtComplete'
    , 'progDistColdView', 'progDistColdIntent', 'progDistColdComplete'
    , 'progCustColdView', 'progCustColdIntent', 'progCustColdComplete'
    , 'progMembColdView', 'progMembColdIntent', 'progMembColdComplete'
    , 'progMembInvtView', 'progMembInvtIntent', 'progMembInvtComplete'
    , 'progCustInvtView', 'progCustInvtComplete'
]


sorterIndex = dict(zip(sorter, range(len(sorter))))
df['eventRank'] = df['Event Action'].map(sorterIndex)
df.sort_values(['Country Code (URL)', 'eventRank'], ascending = [True, True], inplace = True)
df.drop('eventRank', 1, inplace = True)


cntry = df.groupby('Country Code (URL)')['Event Action'].apply(list)
cntryDf = cntry.reset_index()
eventAction = cntryDf['Event Action']


cntryUsed = "MX"
cntryDict = dict(cntry)
print(cntryUsed)
print("sorter total: ",len(sorter))
print("minus events in cntry: -",len(cntryDict[cntryUsed]))
print("equals missing cntry values: =",len((set(sorter).difference(cntryDict[cntryUsed]))))
print(cntryUsed, ": Missing Values:", (set(sorter).difference(cntryDict[cntryUsed])))
result = []

for k in cntryDict:
   x = {'Country':[k], 'Missing':[(set(sorter).difference(cntryDict[k]))]}
   result.append(x)
cntryDf = pd.DataFrame(result)

cntryDf['Country'] = cntryDf['Country'].str[0]
#cntryDf['Event Action'] = str(cntryDf2['Event Action'])
cntryDf['Missing'] = cntryDf['Missing'].str[0]
cntryDf.to_csv("cntryDf1.csv")

cntryDf['eventAction'] = eventAction


convResult = []
for l in cntryDf['eventAction']:
    y = [x for x in l if x in conv]
    convResult.append(y)
convEvents = convResult
cntryDf['convEvents'] = convEvents

convMissResult = []
for k in cntryDict:
   x = {'convMiss':[(set(conv).difference(cntryDict[k]))]}
   convMissResult.append(x)
convMiss = pd.DataFrame(convMissResult)
convMiss.to_csv('more.csv')

cntryDf['convMiss'] = convMiss

convEventDat = []
for e in cntryDf['convEvents']:
    x = str(e).split(",")
    convEventDat.append(x)
convEventDat = pd.DataFrame(convEventDat)
print(convEventDat)


# legacy conversions

lgcyConvView = []
lgcyConvComplete = []
for i,j in convEventDat.iterrows():
    lgcyConvView.append([])
    lgcyConvComplete.append([])
    for e in j:
        x = re.match(".*legacy.*View.*", str(e))
        x = bool(x)
        lgcyConvView[-1].append(x)
        y = re.match(".*legacy.*Complete.*", str(e))
        y = bool(y)
        lgcyConvComplete[-1].append(y)
lgcyConvView = pd.DataFrame(lgcyConvView)
lgcyConvComplete = pd.DataFrame(lgcyConvComplete)
resultDataView = lgcyConvView.any(axis=1)
resultDataCmplt = lgcyConvComplete.any(axis=1)
viewCmplt = pd.DataFrame(resultDataView)
viewCmplt['cmplt'] = resultDataCmplt
viewCmplt = pd.DataFrame(viewCmplt.all(axis=1))
viewCmplt.columns = ['lgcyViewCmplt']
viewCmplt['lgcyViewCmplt'] = (viewCmplt['lgcyViewCmplt'] == True).astype(int)
print(convEventDat)

test = []
trial = []
test = pd.DataFrame({'events' : test,
                     'country' : trial})
for i, j in convEventDat.iterrows():
    test.append([])
    for e in j:
        x = re.match(".*legacy.*View.*", str(e))
        x = bool(x)
        if x == True:
            test[-1].append(e)
            trial[-1].append(j)

lgcyViews = pd.DataFrame(test)
print(test)

cntryDf['lgcyViewCmplt'] = viewCmplt['lgcyViewCmplt']
cntryDf.to_csv("cntryDf.csv")





#lgcyConv = [[re.match(".*simp.*View.*", str(i)) for i in l] for l in convEventDat]
'''
lgcyConv = []
for o in convEventDat:
    lgcyConv.append([])
    for i in range(o):
        i = re.match(".*simp.*View.*", str(i))
        i = bool(x)
        lgcyConv[-1].append(i)
print(lgcyConv)
lgcyConv = pd.DataFrame(lgcyConv)'''
lgcyConvView.to_csv('lgcyConvView.csv')
lgcyConvComplete.to_csv('lgcyConvComplete.csv')


cntryDf.to_csv('cntryDf.csv')

