from WindPy import *
import pandas as pd
from django.db import connection

# contractCodeList = ['CU.SHF','AL.SHF','ZN.SHF','PB.SHF','NI.SHF','SN.SHF','AU.SHF',
#                     'AG.SHF','RB.SHF','WR.SHF','HC.SHF','FU.SHF','BU.SHF','RU.SHF',
#                     'WH.CZC','PM.CZC','CF.CZC','SR.CZC','TA.CZC','OI.CZC','RI.CZC',
#                     'MA.CZC','FG.CZC','RS.CZC','RM.CZC','ZC.CZC','JR.CZC','LR.CZC',
#                     'SF.CZC','SM.CZC','CY.CZC','AP.CZC','C.DCE','CS.DCE','A.DCE',
#                     'B.DCE','M.DCE','Y.DCE','P.DCE','FB.DCE','BB.DCE','JD.DCE',
#                     'I.DCE','V.DCE','PP.DCE','J.DCE','JM.DCE','I.DCE','IF.CFE',
#                     'IC.CFE','IH.CFE','TF.CFE','T.CFE']

def insertDataToFutureInfo():
    contractCodeList = ['CU.SHF']

    #建立wind连接
    w.start()

    for contractCode in contractCodeList:
        windData1 = w.wset("futurecc","startdate=2018-01-01;enddate=2018-02-28;wind_code=" + contractCode)
        print(windData1.Data[2])
        contractList = windData1.Data[2]
        fields = ["sccode","mfprice","contractmultiplier","ltdated","ddate","changelt",
               "punit","margin","lasttrade_date","lastdelivery_date","contract_issuedate"]

        df = pd.DataFrame(index = fields)
        for contract in contractList:
            #print(type(contract))
            windData2 = w.wsd(str(contract),
              "sccode,mfprice,contractmultiplier,ltdated,ddate,changelt,"
              "punit,margin,lasttrade_date,lastdelivery_date,contract_issuedate",
              "2018-01-30", "2018-02-28", "")
            #print(windData2.Data, windData2.Codes)

            contractData = []
            for i in range(len(windData2.Data)):
                contractData.append(windData2.Data[i][len(windData2.Data[i])-1])
            print(len(contractData),len(contractList),len(windData2.Data), contractData)
            df[contract] = contractData
            #df = pd.DataFrame(contractData, index=contractList, columns=columns)

    print(df)

    # 建立数据库连接
    cursor = connection.cursor()

    for i in range(0, len(df.columns)):
        cursor.execute("INSERT INTO fut_contract_info(contractid, sccode, mfprice, contractmultiplier, ltdated, ddated, changelt, punit,"
            "marign, lastdelivery_date, lasttrade_date) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (df.columns[i], df.iloc[0, i], df.iloc[1, i], df.iloc[2, i], df.iloc[3, i], df.iloc[4, i], df.iloc[5, i], df.iloc[6, i],
            df.iloc[7, i], df.iloc[8, i], df.iloc[9, i], df.iloc[10, i]))


    w.stop()


def insertDataToFutureDatabase():
    w.start()

    windData1 = w.wsd("CU1803.SHF",
                      "open,high,low,close,settle,volume,"
                      "oi,amt,chg,chg_settlement,oi_chg,pre_settle,dealnum,",
                      "2017-01-30", "2018-02-28", "")
    print(windData1)

    timeList = [time.strftime('%Y-%m-%d') for time in windData1.Times]
    print(len(windData1.Data), len(windData1.Data[0]), len(windData1.Times))
    df = pd.DataFrame(index=timeList, columns=windData1.Fields)
    for i in range(0, len(windData1.Data)-1):
        df[windData1.Fields[i]] = windData1.Data[i]

    print(df.fillna(''))



    w.stop()

insertDataToFutureDatabase()