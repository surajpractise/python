import datetime

normal_time = "4/21/2021 4:55:13 PM"

def time24convert(normal_time):
    in_time = datetime.datetime.strptime(normal_time, "%I:%M:%S %p")
    out_time = datetime.datetime.strftime(in_time, "%H:%M:%S")
    print("out_time:",out_time)
    return out_time

def datetime_epoch(normal_time):
    date = normal_time.split(" ")[0]
    time = normal_time.split(" ")[1]+" "+normal_time.split(" ")[2]
    time = time24convert(time)
    month = int(date.split("/")[0])
    day = int(date.split("/")[1])
    year = int(date.split("/")[2])
    hr = int(time.split(":")[0])
    min = int(time.split(":")[1])
    sec = int(time.split(":")[2])
    epoch_convert_time = datetime.datetime(year,month,day,hr,min,sec).timestamp()
    epoch_time = str(epoch_convert_time)
    epoch_time1=epoch_time[0:10]#'1619047513 converting float to string
    print("epoch_time1:",epoch_time1)
    datetime_time = datetime.datetime.fromtimestamp(int(epoch_time1))
    print("in date format:",datetime_time)
datetime_epoch(normal_time)
