import os
import pandas as pd
df=pd.read_csv("E:\Report_Generation\I380_V3_HIL_2LiDAR_Missed_Recordings\I380_V3_HIL_2LiDAR_Missed_Recordings_playlist.csv")
drive_id=df[df.columns[0]]
aws_GT_prefix="s3://magna-elec-adas-v2-l2g8810-lidar-exida-exchange-test/In/"
aws_GT_postfix="/OD_Automatic/1.1/"
GT_old_path = []
for i in drive_id:
    if os.path.exists(os.path.join(aws_GT_prefix,i)):
        if os.path.exists(os.path.join(aws_GT_prefix,i,aws_GT_postfix)):
            GT_old_path.append(i)
print(len(GT_old_path))