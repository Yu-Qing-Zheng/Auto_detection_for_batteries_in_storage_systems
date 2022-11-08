#-------
# 更新配置文件后于下一次检测生效。
#-------


# get_current_time()


fmt1 = "%Y-%m-%d %H:%M:%S"
fmt2 = "%H:%M:%S"
fmt3 = "%Y-%m-%d"

# diagnose_trigger_service
seconds_interval = 3600
# time_rigger()
specified_time = '23:00:00'

# Mongodb connecting
MONGO_HOST = 'dds-8vb381a9f7b950b43984-pub.mongodb.zhangbei.rds.aliyuncs.com'
MONGO_PORT = 3717
MONGO_DB_NAME = 'dems'
MONGO_USERNAME = 'root'
MONGO_PWD = 'TMRenergy!'
MONGO_AUTH_SOURCE = 'admin'

# energy_trigger
day_threshold = 7
day_interval = 2
threshold_factor = 0.8
restored_threshold_factor = 2
time_fill1 = ' 00:00:00'
time_fill2 = ' 23:59:59'
filename_energy_trigger = './median_max_energy.csv'
flag_for_override = -1
flag_for_normal = 0
flag_for_abnormal = 1
flag_for_threshold_calculating = 2

# maximum_energy_calculate & median_energy_calculate
max_forward_threshold = 500
max_reverse_threshold = 500

# query_all_plc
plc_csv_path = './plcid_list/'
plc_csv_file = 'plc_list.csv'
plc_query_control_file = 'last_update.txt'

# chatbot
energy_trigger_sender_webhook = 'https://oapi.dingtalk.com/robot/send?access_token=c8c02777586007e8ec0d1b175d8a3ca773fcf730b9d3a5dfde036935e3102d47'
energy_trigger_sender_secret = 'SECe5b022bf14b2440432177f5f040593c3d8c14467cfc59a52e6ee44fdc782c1d3'
bot_query_dayrange = 1
chatrobot_switch = 0

# dron (data reduction)
pack_num = 10
battery_num = 24
voltage_coefficient = 1000
threshold_for_rms = 3.5

# soc
model_path = './soc/'
model_file = '280Ahmodel.mat'
deltat = 60
numpoles = 1
SigmaX0 = [1e-6, 1e-8, 2e-4]
# SigmaX0 = [1e-6, 1e-6, 1e-6, 1e-8, 2e-4]
SigmaV = 2e-1
SigmaW = 2e-1

# soh
id_wls = 0
id_wtls = 1
id_rtls = 2
id_awtls = 3
precisionI = 2**10
m = 300
gamma = 1#-10**(-4)

# pic
figpath = './draw/fig/'
fontsize = 10

# diagnose_switch
diagnose_days_interval = 1

# Query request
filter_for_data_collection = {
            "$project": {
                "_id": 0,
                "PLC_id": 1,
                "time": 1,
                "data": {
                    "PCS电池电流": 1,
                    "1组1号电池电压": 1,
                    "1组2号电池电压": 1,
                    "1组3号电池电压": 1,
                    "1组4号电池电压": 1,
                    "1组5号电池电压": 1,
                    "1组6号电池电压": 1,
                    "1组7号电池电压": 1,
                    "1组8号电池电压": 1,
                    "1组9号电池电压": 1,
                    "1组10号电池电压": 1,
                    "1组11号电池电压": 1,
                    "1组12号电池电压": 1,
                    "1组13号电池电压": 1,
                    "1组14号电池电压": 1,
                    "1组15号电池电压": 1,
                    "1组16号电池电压": 1,
                    "1组17号电池电压": 1,
                    "1组18号电池电压": 1,
                    "1组19号电池电压": 1,
                    "1组20号电池电压": 1,
                    "1组21号电池电压": 1,
                    "1组22号电池电压": 1,
                    "1组23号电池电压": 1,
                    "1组24号电池电压": 1,
                    "1组电池温度1": 1,
                    "1组电池温度2": 1,
                    "2组1号电池电压": 1,
                    "2组2号电池电压": 1,
                    "2组3号电池电压": 1,
                    "2组4号电池电压": 1,
                    "2组5号电池电压": 1,
                    "2组6号电池电压": 1,
                    "2组7号电池电压": 1,
                    "2组8号电池电压": 1,
                    "2组9号电池电压": 1,
                    "2组10号电池电压": 1,
                    "2组11号电池电压": 1,
                    "2组12号电池电压": 1,
                    "2组13号电池电压": 1,
                    "2组14号电池电压": 1,
                    "2组15号电池电压": 1,
                    "2组16号电池电压": 1,
                    "2组17号电池电压": 1,
                    "2组18号电池电压": 1,
                    "2组19号电池电压": 1,
                    "2组20号电池电压": 1,
                    "2组21号电池电压": 1,
                    "2组22号电池电压": 1,
                    "2组23号电池电压": 1,
                    "2组24号电池电压": 1,
                    "2组电池温度1": 1,
                    "2组电池温度2": 1,
                    "3组1号电池电压": 1,
                    "3组2号电池电压": 1,
                    "3组3号电池电压": 1,
                    "3组4号电池电压": 1,
                    "3组5号电池电压": 1,
                    "3组6号电池电压": 1,
                    "3组7号电池电压": 1,
                    "3组8号电池电压": 1,
                    "3组9号电池电压": 1,
                    "3组10号电池电压": 1,
                    "3组11号电池电压": 1,
                    "3组12号电池电压": 1,
                    "3组13号电池电压": 1,
                    "3组14号电池电压": 1,
                    "3组15号电池电压": 1,
                    "3组16号电池电压": 1,
                    "3组17号电池电压": 1,
                    "3组18号电池电压": 1,
                    "3组19号电池电压": 1,
                    "3组20号电池电压": 1,
                    "3组21号电池电压": 1,
                    "3组22号电池电压": 1,
                    "3组23号电池电压": 1,
                    "3组24号电池电压": 1,
                    "3组电池温度1": 1,
                    "3组电池温度2": 1,
                    "4组1号电池电压": 1,
                    "4组2号电池电压": 1,
                    "4组3号电池电压": 1,
                    "4组4号电池电压": 1,
                    "4组5号电池电压": 1,
                    "4组6号电池电压": 1,
                    "4组7号电池电压": 1,
                    "4组8号电池电压": 1,
                    "4组9号电池电压": 1,
                    "4组10号电池电压": 1,
                    "4组11号电池电压": 1,
                    "4组12号电池电压": 1,
                    "4组13号电池电压": 1,
                    "4组14号电池电压": 1,
                    "4组15号电池电压": 1,
                    "4组16号电池电压": 1,
                    "4组17号电池电压": 1,
                    "4组18号电池电压": 1,
                    "4组19号电池电压": 1,
                    "4组20号电池电压": 1,
                    "4组21号电池电压": 1,
                    "4组22号电池电压": 1,
                    "4组23号电池电压": 1,
                    "4组24号电池电压": 1,
                    "4组电池温度1": 1,
                    "4组电池温度2": 1,
                    "5组1号电池电压": 1,
                    "5组2号电池电压": 1,
                    "5组3号电池电压": 1,
                    "5组4号电池电压": 1,
                    "5组5号电池电压": 1,
                    "5组6号电池电压": 1,
                    "5组7号电池电压": 1,
                    "5组8号电池电压": 1,
                    "5组9号电池电压": 1,
                    "5组10号电池电压": 1,
                    "5组11号电池电压": 1,
                    "5组12号电池电压": 1,
                    "5组13号电池电压": 1,
                    "5组14号电池电压": 1,
                    "5组15号电池电压": 1,
                    "5组16号电池电压": 1,
                    "5组17号电池电压": 1,
                    "5组18号电池电压": 1,
                    "5组19号电池电压": 1,
                    "5组20号电池电压": 1,
                    "5组21号电池电压": 1,
                    "5组22号电池电压": 1,
                    "5组23号电池电压": 1,
                    "5组24号电池电压": 1,
                    "5组电池温度1": 1,
                    "5组电池温度2": 1,
                    "6组1号电池电压": 1,
                    "6组2号电池电压": 1,
                    "6组3号电池电压": 1,
                    "6组4号电池电压": 1,
                    "6组5号电池电压": 1,
                    "6组6号电池电压": 1,
                    "6组7号电池电压": 1,
                    "6组8号电池电压": 1,
                    "6组9号电池电压": 1,
                    "6组10号电池电压": 1,
                    "6组11号电池电压": 1,
                    "6组12号电池电压": 1,
                    "6组13号电池电压": 1,
                    "6组14号电池电压": 1,
                    "6组15号电池电压": 1,
                    "6组16号电池电压": 1,
                    "6组17号电池电压": 1,
                    "6组18号电池电压": 1,
                    "6组19号电池电压": 1,
                    "6组20号电池电压": 1,
                    "6组21号电池电压": 1,
                    "6组22号电池电压": 1,
                    "6组23号电池电压": 1,
                    "6组24号电池电压": 1,
                    "6组电池温度1": 1,
                    "6组电池温度2": 1,
                    "7组1号电池电压": 1,
                    "7组2号电池电压": 1,
                    "7组3号电池电压": 1,
                    "7组4号电池电压": 1,
                    "7组5号电池电压": 1,
                    "7组6号电池电压": 1,
                    "7组7号电池电压": 1,
                    "7组8号电池电压": 1,
                    "7组9号电池电压": 1,
                    "7组10号电池电压": 1,
                    "7组11号电池电压": 1,
                    "7组12号电池电压": 1,
                    "7组13号电池电压": 1,
                    "7组14号电池电压": 1,
                    "7组15号电池电压": 1,
                    "7组16号电池电压": 1,
                    "7组17号电池电压": 1,
                    "7组18号电池电压": 1,
                    "7组19号电池电压": 1,
                    "7组20号电池电压": 1,
                    "7组21号电池电压": 1,
                    "7组22号电池电压": 1,
                    "7组23号电池电压": 1,
                    "7组24号电池电压": 1,
                    "7组电池温度1": 1,
                    "7组电池温度2": 1,
                    "8组1号电池电压": 1,
                    "8组2号电池电压": 1,
                    "8组3号电池电压": 1,
                    "8组4号电池电压": 1,
                    "8组5号电池电压": 1,
                    "8组6号电池电压": 1,
                    "8组7号电池电压": 1,
                    "8组8号电池电压": 1,
                    "8组9号电池电压": 1,
                    "8组10号电池电压": 1,
                    "8组11号电池电压": 1,
                    "8组12号电池电压": 1,
                    "8组13号电池电压": 1,
                    "8组14号电池电压": 1,
                    "8组15号电池电压": 1,
                    "8组16号电池电压": 1,
                    "8组17号电池电压": 1,
                    "8组18号电池电压": 1,
                    "8组19号电池电压": 1,
                    "8组20号电池电压": 1,
                    "8组21号电池电压": 1,
                    "8组22号电池电压": 1,
                    "8组23号电池电压": 1,
                    "8组24号电池电压": 1,
                    "8组电池温度1": 1,
                    "8组电池温度2": 1,
                    "9组1号电池电压": 1,
                    "9组2号电池电压": 1,
                    "9组3号电池电压": 1,
                    "9组4号电池电压": 1,
                    "9组5号电池电压": 1,
                    "9组6号电池电压": 1,
                    "9组7号电池电压": 1,
                    "9组8号电池电压": 1,
                    "9组9号电池电压": 1,
                    "9组10号电池电压": 1,
                    "9组11号电池电压": 1,
                    "9组12号电池电压": 1,
                    "9组13号电池电压": 1,
                    "9组14号电池电压": 1,
                    "9组15号电池电压": 1,
                    "9组16号电池电压": 1,
                    "9组17号电池电压": 1,
                    "9组18号电池电压": 1,
                    "9组19号电池电压": 1,
                    "9组20号电池电压": 1,
                    "9组21号电池电压": 1,
                    "9组22号电池电压": 1,
                    "9组23号电池电压": 1,
                    "9组24号电池电压": 1,
                    "9组电池温度1": 1,
                    "9组电池温度2": 1,
                    "10组1号电池电压": 1,
                    "10组2号电池电压": 1,
                    "10组3号电池电压": 1,
                    "10组4号电池电压": 1,
                    "10组5号电池电压": 1,
                    "10组6号电池电压": 1,
                    "10组7号电池电压": 1,
                    "10组8号电池电压": 1,
                    "10组9号电池电压": 1,
                    "10组10号电池电压": 1,
                    "10组11号电池电压": 1,
                    "10组12号电池电压": 1,
                    "10组13号电池电压": 1,
                    "10组14号电池电压": 1,
                    "10组15号电池电压": 1,
                    "10组16号电池电压": 1,
                    "10组17号电池电压": 1,
                    "10组18号电池电压": 1,
                    "10组19号电池电压": 1,
                    "10组20号电池电压": 1,
                    "10组21号电池电压": 1,
                    "10组22号电池电压": 1,
                    "10组23号电池电压": 1,
                    "10组24号电池电压": 1,
                    "10组电池温度1": 1,
                    "10组电池温度2": 1,
                },
                "record": {
                            "info": {
                                "快速充电中": 1,
                                "放电中": 1,
                                "充电完成": 1,
                                "放电完成": 1,
                            }
                },
            }
        }
# energy_calculation
filter_for_energy_calculation = {
            "$project": {
                "_id": 0,
                "PLC_id": 1,
                "time": 1,
                "data": {
                    "PCS电池电流": 1,
                    "正向有功总电能": 1,
                    "正向有功总电能2": 1,
                    "反向总有功电能": 1,
                    "反向总有功电能2": 1,
                },
            }
        }

# energy_trigger
filter_for_energy_threshold = {
            "$project": {
                "plc": 1,
                "time": 1,
                "median_max_forward": 1, 
                "median_max_reverse": 1, 
            }
        }
        
filter_for_energy_trigger = {
            "$project": {
                "plc": 1,
                "time": 1,
                "energy_flag": 1, 
            }
        }