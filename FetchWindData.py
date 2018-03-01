import pandas as pd
from WindPy import *

def insertDataToBondYTM(time, worksheet):
    #建立wind连接
    w.start()

    #建立对应合约号和久期的dict
    durationDict = {'M1003983':'3M', 'M1003984':'6M', 'M1004093':'1Y', 'M1004094':'2Y', 'M1004095':'3Y', 'M1004096':'4Y',
                    'M1004097':'5Y', 'M1004098':'7Y', 'M1004099':'10Y', 'M1004122':'1M', 'M1004123':'3M', 'M1004124':'6M',
                    'M1004125':'9M', 'M1004126':'1Y', 'M1004127':'2Y', 'M1004128':'3Y', 'M1004129':'4Y', 'M1004130':'5Y',
                    'M1004131':'7Y', 'M1004132':'10Y', 'M1004136':'0Y', 'M1004677':'1M', 'M1004829':'2M', 'M1000155':'3M',
                    'M1000156':'6M', 'M1000157':'9M', 'M1000158':'1Y', 'M1000159':'2Y', 'M1000160':'3Y', 'M1000161':'4Y',
                    'M1000162':'5Y', 'M1000163':'6Y', 'M1000164':'7Y', 'M1000165':'8Y', 'M1004678':'9Y', 'M1000166':'10Y',
                    'M1000167':'15Y', 'M1000168':'20Y', 'M1000169':'30Y', 'M1004711':'40Y', 'M1000170':'50Y', 'M1004258':'0Y',
                    'M1004687':'1M', 'M1004259':'2M', 'M1004260':'3M', 'M1004261':'6M', 'M1004262':'9M', 'M1004263':'1Y',
                    'M1004264':'2Y', 'M1004265':'3Y', 'M1004266':'4Y', 'M1004267':'5Y', 'M1004268':'6Y', 'M1004269':'7Y',
                    'M1004270':'8Y', 'M1004688':'9Y', 'M1004271':'10Y', 'M1004272':'15Y', 'M1004273':'20Y', 'M1004274':'30Y',
                    'M1004275':'50Y', 'M1004138':'0Y', 'M1004685':'1M', 'M1000181':'3M', 'M1000182':'6M', 'M1000183':'9M',
                    'M1000184':'1Y', 'M1000185':'2Y', 'M1000186':'3Y', 'M1000187':'4Y', 'M1000188':'5Y', 'M1000189':'6Y',
                    'M1000190':'7Y', 'M1000191':'8Y', 'M1004686':'9Y', 'M1000192':'10Y', 'M1000193':'15Y', 'M1000194':'20Y',
                    'M1007661':'0Y', 'M1007662':'1M', 'M1007663':'3M', 'M1007664':'6M', 'M1007665':'9M', 'M1007666':'1Y',
                    'M1007667':'2Y', 'M1007668':'3Y', 'M1007669':'4Y', 'M1007670':'5Y', 'M1007671':'6Y', 'M1007672':'7Y',
                    'M1007673':'8Y', 'M1007674':'9Y', 'M1007675':'10Y', 'M1007676':'15Y', 'M1007677':'20Y'}

    #########SHIBOR3M############
    # 从wind获取利率互换
    windData = w.edb("M1003983, M1003984, M1004093, M1004094, M1004095, M1004096, M1004097, M1004098, "
                     "M1004099", time, time, "")

    index_i = 1

    #Wind数据整理
    timeList = [time.strftime('%Y-%m-%d') for time in windData.Times]
    print(windData)
    # 包装成DataFrame
    # df = pd.DataFrame([windData.Data], columns = windData.Codes, index = windData.Times)
    df = pd.DataFrame(index = timeList)
    for i in range(len(windData.Codes)):
        df[windData.Codes[i]] = windData.Data[0][i]
    print(df, len(df.index), len(df.columns))
    for i in range (0, len(df.index)):
        for j in range (0, len(df.columns)):
            print(i, j)
            print(df.iloc[i, j], df.index[i], df.columns[j])
            worksheet.write(index_i, 0, label='01')
            worksheet.write(index_i, 1, label=df.columns[j])
            worksheet.write(index_i, 2, label=durationDict[df.columns[j]])
            worksheet.write(index_i, 3, label=df.iloc[i, j])
            worksheet.write(index_i, 4, label=df.index[i])
            index_i += 1

    #########SHIBOR3M############
    # 从wind获取利率互换
    windData = w.edb("M1004122, M1004123, M1004124, M1004125, M1004126,"
                    "M1004127, M1004128, M1004129, M1004130, M1004131, M1004132", time, time, "")

     # Wind数据整理
    timeList = [time.strftime('%Y-%m-%d') for time in windData.Times]
    print(windData)
    # 包装成DataFrame
    # df = pd.DataFrame([windData.Data], columns = windData.Codes, index = windData.Times)
    df = pd.DataFrame(index=timeList)
    for i in range(len(windData.Codes)):
        df[windData.Codes[i]] = windData.Data[0][i]
    print(df, len(df.index), len(df.columns))
    for i in range(0, len(df.index)):
        for j in range(0, len(df.columns)):
            print(i, j)
            print(df.iloc[i, j], df.index[i], df.columns[j])
            worksheet.write(index_i, 0, label='06')
            worksheet.write(index_i, 1, label=df.columns[j])
            worksheet.write(index_i, 2, label=durationDict[df.columns[j]])
            worksheet.write(index_i, 3, label=df.iloc[i, j])
            worksheet.write(index_i, 4, label=df.index[i])
            index_i += 1

    #########中债国债数据导入############
    windData = w.edb("M1004136,M1004677,M1004829,M1000155,M1000156,M1000157,M1000158,M1000159,M1000160,M1000161,"
          "M1000162,M1000163,M1000164,M1000165,M1004678,M1000166,M1000167,M1000168,M1000169,M1004711,M1000170",
        time, time, "")
    # Wind数据整理
    timeList = [time.strftime('%Y-%m-%d') for time in windData.Times]
    # 包装成DataFrame
    # df = pd.DataFrame([windData.Data], columns = windData.Codes, index = windData.Times)
    df = pd.DataFrame(index=timeList)
    for i in range(len(windData.Codes)):
        df[windData.Codes[i]] = windData.Data[0][i]
    print(df, len(df.index), len(df.columns))
    for i in range(0, len(df.index)):
        for j in range(0, len(df.columns)):
            print(i, j)
            print(df.iloc[i, j], df.index[i], df.columns[j])
            worksheet.write(index_i, 0, label='02')
            worksheet.write(index_i, 1, label=df.columns[j])
            worksheet.write(index_i, 2, label=durationDict[df.columns[j]])
            worksheet.write(index_i, 3, label=df.iloc[i, j])
            worksheet.write(index_i, 4, label=df.index[i])
            index_i += 1

    #########中债国开债数据导入############
    windData = w.edb("M1004258,M1004687,M1004259,M1004260,M1004261,M1004262,M1004263,M1004264,M1004265,M1004266,"
                     "M1004267,M1004268,M1004269,M1004270,M1004688,M1004271,M1004272,M1004273,M1004274,M1004275",
                     time, time, "")
    # Wind数据整理
    timeList = [time.strftime('%Y-%m-%d') for time in windData.Times]
    # 包装成DataFrame
    # df = pd.DataFrame([windData.Data], columns = windData.Codes, index = windData.Times)
    df = pd.DataFrame(index=timeList)
    for i in range(len(windData.Codes)):
        df[windData.Codes[i]] = windData.Data[0][i]
    print(df, len(df.index), len(df.columns))
    for i in range(0, len(df.index)):
        for j in range(0, len(df.columns)):
            print(i, j)
            print(df.iloc[i, j], df.index[i], df.columns[j])
            worksheet.write(index_i, 0, label='03')
            worksheet.write(index_i, 1, label=df.columns[j])
            worksheet.write(index_i, 2, label=durationDict[df.columns[j]])
            worksheet.write(index_i, 3, label=df.iloc[i, j])
            worksheet.write(index_i, 4, label=df.index[i])
            index_i += 1

    #########中债进出口债数据导入############
    windData = w.edb("M1004138,M1004685,M1000181,M1000182,M1000183,M1000184,M1000185,M1000186,M1000187,M1000188,"
                     "M1000189,M1000190,M1000191,M1004686,M1000192,M1000193,M1000194", time, time, "")
    # Wind数据整理
    timeList = [time.strftime('%Y-%m-%d') for time in windData.Times]
    # 包装成DataFrame
    # df = pd.DataFrame([windData.Data], columns = windData.Codes, index = windData.Times)
    df = pd.DataFrame(index=timeList)
    for i in range(len(windData.Codes)):
        df[windData.Codes[i]] = windData.Data[0][i]
    print(df, len(df.index), len(df.columns))
    for i in range(0, len(df.index)):
        for j in range(0, len(df.columns)):
            print(i, j)
            print(df.iloc[i, j], df.index[i], df.columns[j])
            worksheet.write(index_i, 0, label='04')
            worksheet.write(index_i, 1, label=df.columns[j])
            worksheet.write(index_i, 2, label=durationDict[df.columns[j]])
            worksheet.write(index_i, 3, label=df.iloc[i, j])
            worksheet.write(index_i, 4, label=df.index[i])
            index_i += 1

    #########中债农发行债数据导入############
    windData = w.edb("M1007661,M1007662,M1007663,M1007664,M1007665,M1007666,M1007667,M1007668,M1007669,M1007670,"
                     "M1007671,M1007672,M1007673,M1007674,M1007675,M1007676,M1007677", time, time, "")
    # Wind数据整理
    timeList = [time.strftime('%Y-%m-%d') for time in windData.Times]
    # 包装成DataFrame
    # df = pd.DataFrame([windData.Data], columns = windData.Codes, index = windData.Times)
    df = pd.DataFrame(index=timeList)
    for i in range(len(windData.Codes)):
        df[windData.Codes[i]] = windData.Data[0][i]
    print(df, len(df.index), len(df.columns))
    for i in range(0, len(df.index)):
        for j in range(0, len(df.columns)):
            print(i, j)
            print(df.iloc[i, j], df.index[i], df.columns[j])
            worksheet.write(index_i, 0, label='05')
            worksheet.write(index_i, 1, label=df.columns[j])
            worksheet.write(index_i, 2, label=durationDict[df.columns[j]])
            worksheet.write(index_i, 3, label=df.iloc[i, j])
            worksheet.write(index_i, 4, label=df.index[i])
            index_i += 1

    w.stop()

    return worksheet


import datetime

yesterday = str((datetime.datetime.today() +  datetime.timedelta(days = -1)).strftime('%Y-%m-%d'))
print(yesterday)

import xlwt
workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet')
#worksheet.write(0, 0, label = 'Row 0, Column 0 Value')
worksheet.write(0, 0, label = 'BONDYTMTYPE')
worksheet.write(0, 1, label = 'BONDID')
worksheet.write(0, 2, label = 'BONDDURATION')
worksheet.write(0, 3, label = 'BONDYTM')
worksheet.write(0, 4, label = 'TIMESTAMP')

worksheet = insertDataToBondYTM(yesterday, worksheet)
workbook.save('D:\Excel_Workbook.xls')