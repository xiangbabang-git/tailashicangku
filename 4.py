import pymysql
import re

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')
cur = db.cursor()

f = open('dict.txt')
args_list = []
for line in f:
    result = re.findall(r"(\S+)\s+(.*)", line)




bie ta ma gei wo lai zhe tao 
yao lai jiu lai chun jie tao 

