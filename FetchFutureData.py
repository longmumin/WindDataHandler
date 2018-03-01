from WindPy import *
import pandas as pd

# contractCodeList = ['CU.SHF','AL.SHF','ZN.SHF','PB.SHF','NI.SHF','SN.SHF','AU.SHF',
#                     'AG.SHF','RB.SHF','WR.SHF','HC.SHF','FU.SHF','BU.SHF','RU.SHF',
#                     'WH.CZC','PM.CZC','CF.CZC','SR.CZC','TA.CZC','OI.CZC','RI.CZC',
#                     'MA.CZC','FG.CZC','RS.CZC','RM.CZC','ZC.CZC','JR.CZC','LR.CZC',
#                     'SF.CZC','SM.CZC','CY.CZC','AP.CZC','C.DCE','CS.DCE','A.DCE',
#                     'B.DCE','M.DCE','Y.DCE','P.DCE','FB.DCE','BB.DCE','JD.DCE',
#                     'I.DCE','V.DCE','PP.DCE','J.DCE','JM.DCE','I.DCE','IF.CFE',
#                     'IC.CFE','IH.CFE','TF.CFE','T.CFE']

contractCodeList = ['CU.SHF']

#建立wind连接
w.start()

for contractCode in contractCodeList:
    windData1 = w.wset("futurecc","startdate=2018-01-01;enddate=2018-02-28;wind_code=" + contractCode)
    print(windData1.Data[2])
    contractList = windData1.Data[2]
    df = pd.DataFrame()
    for contract in contractList:
        #print(type(contract))
        windData2 = w.wsd(str(contract),
              "sccode,mfprice,contractmultiplier,ltdated,ddate,changelt,"
              "punit,margin,lasttrade_date,lastdelivery_date,contract_issuedate",
              "2018-01-30", "2018-02-28", "")
        print(windData2.Data, windData2.Codes)
        columns = ["sccode,mfprice,contractmultiplier,ltdated,ddate,changelt,"
              "punit,margin,lasttrade_date,lastdelivery_date,contract_issuedate"]

        contractData = []
        for i in range(len(windData2.Data)):
            contractData.append(windData2.Data[i])
        print(len(contractData),len(contractList),len(windData2.Data))
        df = pd.DataFrame(contractData, index=contractList, columns=columns)

print(df)

# windData2 = w.wsd("CU1803.SHF", "sccode,mfprice,contractmultiplier,ltdated,ddate,changelt,"
#                                 "punit,margin,lasttrade_date,lastdelivery_date,contract_issuedate", "2018-01-30", "2018-02-28", "")
#
#
# print(windData2.Data)

w.stop()

