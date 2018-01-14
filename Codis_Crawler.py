import pandas as pd
import calendar as cd

# =====主控台=======
#台中市，測站: 台中
yy=2017 #輸入想查詢的年份
Check=False #如果不想查詢整年份，改為False 
mm=5 #輸入想查詢的月份
dd=1 #輸入想查詢的日期
# =====End=========


#===改為正確日期================================================================
def DataTime_(yy,mm,dd):
    date_=[]
    for i in range(1,25):
        date_.append(str(yy)+"-"+str(mm)+"-"+str(dd)+", "+"%02d"%i+":"+"00")
    return date_
#==============================================================================

if(Check):
    for mm in range(12):
        mm+=1
        for dd in range(cd.mdays[mm]):
            dd+=1
            df=pd.read_html("http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467490&stname=%25E8%2587%25BA%25E4%25B8%25AD&datepicker="+ str(yy) +"-"+ str(mm) +"-"+ str(dd) )
            df[1][2:]
            data=df[1][2:]
            data.columns=['DataTime','StnPres','SeaPres','Temperature','DewPointTemperature','RelativeHumidity','WindSpeed','WindDirection','WSGust','WDGust','Precipitation','PrecpHour','SunShine','GloblRad','Visibility']
            data=data.fillna(0)
            data.DataTime=DataTime_(yy,mm,dd)
            data.to_csv("C:/Codis_Data/"+ str(yy) +"-"+ str("%02d"%mm) +"-"+ str("%02d"%dd) +".csv",index=False)
else:
    df=pd.read_html("http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467490&stname=%25E8%2587%25BA%25E4%25B8%25AD&datepicker="+ str(yy) +"-"+ str(mm) +"-"+ str(dd) )
    df[1][2:]
    data=df[1][2:]
    data.columns=['DataTime','StnPres','SeaPres','Temperature','DewPointTemperature','RelativeHumidity','WindSpeed','WindDirection','WSGust','WDGust','Precipitation','PrecpHour','SunShine','GloblRad','Visibility']
    data=data.fillna(0)
    data.DataTime=DataTime_(yy,mm,dd)
    data.to_csv("C:/Codis_Data/"+ str(yy) +"-"+ str("%02d"%mm) +"-"+ str("%02d"%dd) +".csv",index=False)


