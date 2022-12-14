
# coding: utf-8

# In[1]:


#测试脚本
import json
import time

import requests
from lxml import etree

url = "https://blog.csdn.net/m0_57011777/article/details/125365301"
header = {"User-Agent": 
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"}
html1 = requests.get(url, headers=header).text
##print(html1)
page_list = etree.HTML(html1)
option = page_list.xpath('//*[@id="articleContentId"]/text()')
print(option)


# In[100]:


#测试脚本
import json
import time

import requests
from lxml import etree

url = "https://gdp.gotohui.com/data-3412"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
html1 = requests.get(url, headers=header).text
##print(html1)
page_list = etree.HTML(html1)
option = page_list.xpath('//table[@class="ntable table-striped table-hover"]/tr/td/text()')
data1=page_list.xpath('//table[@class="ntable table-striped table-hover"]/tr/td[1]/text()')
data2=page_list.xpath('//table[@class="ntable table-striped table-hover"]/tr/td[2]/text()')
data3=page_list.xpath('//table[@class="ntable table-striped table-hover"]/tr/td[3]/text()')
data4=page_list.xpath('//table[@class="ntable table-striped table-hover"]/tr/td[4]/text()')
data=pd.DataFrame()
data['year']=data1
data['GDP']=data2
data['Ratio']=data3
data['perGDP']=data4
data

#https://www.cnblogs.com/xxingrui/p/14928381.html
#https://blog.csdn.net/qq_51754979/article/details/123262172
#https://blog.csdn.net/weixin_45723705/article/details/115280916


# In[1]:


###异步加载爬虫####
import requests
from lxml import etree
import os
headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46"}
list1=[]
file=r'D:\异步加载爬虫'
url='https://www.hippopx.com/'
html=requests.get(url,headers=headers)
selector=etree.HTML(html.text)
imgs=selector.xpath('//*[@id="flow"]/li/figure/a/img')
for img in imgs:
    photo=img.get('src')
    list.append(photo)
for item in list1:
    print(item)
    data=requests.get(item,headers=headers)
    fp= open(file+'/'+item.split('/')[-1],'wb')
    fp.write(data.content)
    fp.close()
##https://zhuanlan.zhihu.com/p/335834494


# In[1]:


###异步加载json####
import urllib.request
import urllib.parse
import urllib.error
import json
import pandas as pd 

url = 'https://movie.douban.com/j/new_search_subjects?'
headers = {
        'Accept': 'text/html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46'
}

# 循环次数自己设置，这里循环三次，爬取前60个电影数据
for p in range(0,3):
    page = p * 20
    params = {'sort':'U', 'range':'0,10', 'tags':'', 'start':str(page)}
    params_encode = urllib.parse.urlencode(params).encode('utf-8')

    try:
        request = urllib.request.Request(url, data=params_encode, headers=headers)
        with urllib.request.urlopen(request) as response:
            data_empty=pd.DataFrame()
            data_list=json.loads(response.read().decode('utf-8'))
            print(data_list)
            print('---'*20)

    except urllib.error.HTTPError as e:
        print(e)
    except urllib.error.URLError as e:
        print(e)


# In[103]:


###异步加载json####
import urllib.request
import urllib.parse
import urllib.error
import json
import pandas as pd 

url = 'https://movie.douban.com/j/new_search_subjects?'
headers = {
        'Accept': 'text/html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46'
}

# 循环次数自己设置，这里循环二次，爬取前60个电影数据
for p in range(0,2):
    page = p * 20
    params = {'sort':'U', 'range':'0,10', 'tags':'', 'start':str(page)}
    params_encode = urllib.parse.urlencode(params).encode('utf-8')

    try:
        request = urllib.request.Request(url, data=params_encode, headers=headers)
        with urllib.request.urlopen(request) as response:
            data_empty=pd.DataFrame()
            data_list=json.loads(response.read().decode('utf-8'))
            #print(data_list)
            #print('---'*20)
            print(type(data_list))
            print(data_list.keys())

    except urllib.error.HTTPError as e:
        print(e)
    except urllib.error.URLError as e:
        print(e)

my_d_key=set(data_list['data'][1].keys())
col=my_d_key
my_d2=[]
for i in range(0,len(data_list['data'])):
    my_d1=data_list['data'][i]
    my_d2.append(my_d1)
#print(my_d2[1]['directors'],len(my_d2))
df2=[]
for i in range(0,len(my_d2)):
    df1=[]
    for j in col:
        df=str(my_d2[i][j])
        #print(df)
        df1.append(df)
    #print(df1)
    df2.append(df1)
f1=pd.DataFrame(df2)
f1.columns=col
f1


# In[101]:


#df = pd.DataFrame({"col1": data_list['data'][1].keys(), "col2": data_list['data'][1].values()})
#print(df)
#set(data_list['data'][1].keys())
my_d_key=set(data_list['data'][1].keys())
col=my_d_key
my_d2=[]
for i in range(0,len(data_list['data'])):
    my_d1=data_list['data'][i]
    my_d2.append(my_d1)
#print(my_d2[1]['directors'],len(my_d2))
df2=[]
for i in range(0,len(my_d2)):
    df1=[]
    for j in col:
        df=str(my_d2[i][j])
        #print(df)
        df1.append(df)
    #print(df1)
    df2.append(df1)
f1=pd.DataFrame(df2)
f1.columns=col
f1


# In[ ]:


#获取网页表单数据
import pandas as pd
df=pd.read_html("https://gdp.gotohui.com/data-3412")
df


import pandas as pd

df = pd.DataFrame()
url_list = ['https://www.espn.com/nba/salaries/_/seasontype/4']
for i in range(2, 13):
    # %s 表示把URL变量转换为字符串
    url = 'https://www.espn.com/nba/salaries/_/page/%s/seasontype/4' % i
    url_list.append(url)
    # 遍历网页中的table读取网页表格数据
for url in url_list:
    df = df.append(pd.read_html(url), ignore_index=True)
    # 列表解析：遍历 dataframe 第3列并且用$开头
df = df[[x.startswith('$') for x in df[3]]]
df.to_csv('Salary.csv', header=['RK', 'NAME', 'TEAM', 'SALARY'], index=False)

#https://blog.csdn.net/qq_40478273/article/details/103980288
#   https://www.codenong.com/cs106086967/


# In[ ]:


#完整爬取网页数据
'''
import datetime
import re

import openpyxl
import requests
from lxml import etree


def get_url_html(url):
    """
    定义一个函数, 新建一个空变量html_str， 请求网页获取网页源码，如果请求成功，则返回结果，如果失败则返回空值
    url: 入参参数, 指的是我们普通浏览器中的访问网址
    """
    html_str = ""
    try:
        """获取网页请求之后，返回的网页源码，类似于在浏览器中右击选择网页源码, 使用三方库etree把网页源码字符串转换成HTML格式"""
        r = requests.get(url, timeout=200).text
        html_str = etree.HTML(r)
    except Exception as e:
        print(e)
    return html_str


def get_page_total(html_str):
    """
    定义一个函数, 新建一个变量pages初始值为0， 在网页源码中匹配出总页数的数值，如果匹配成功返回结果，如果失败则返回0
    html_str: 入参参数, 指的是网页源码，HTML格式的
    """
    pages = 0
    try:
        """查找网页源码中的xpath，找到总页数所在的xptah位置，并获取它的文本，举例子：页/78页，然后通过正则匹配出78这两个数字"""
        pages_str = html_str.xpath('//div[@class="contentshow"]//div[@class="box"]//div[@class="page"][2]//div[@class="goTextInput"]/text()')
        pages = re.findall("\d+", pages_str[1])[0]
    except Exception as e:
        print(e)
    return pages


def get_page_data(html_str):
    """
    定义一个函数, 新建一个变量pdata_list初始值为空列表（也可以叫空数组）， 在网页源码中匹配出每一行的内容
    html_str: 入参参数, 指的是网页源码，HTML格式的
    """
    data_list = []
    try:
        """查找网页源码中的xpath，找到每一行的位置"""
        option = html_str.xpath('//div[@class="contentshow"]//div[@class="box"]/table/tbody[2]//tr')
        for op in option:
            """根据每一行，匹配出第一列的字符串，比如'2021年10月20日'，再通过正则匹配出它的数字部分用'/'隔开，则把字符串转换成2021/10/20"""
            col1 = "/".join(re.findall("\d+", op.xpath("./td[1]/text()")[0]))
            """根据每一行，匹配出其他4列的数字字符串，然后通过函数转换，将字符串转换成浮点类型, 获取失败则为空值"""
            try:
                col2 = float(op.xpath("./td[2]/text()")[0])
            except:
                col2 = ""
            try:
                col3 = float(op.xpath("./td[3]/text()")[0])
            except:
                col3 = ""
            try:
                col4 = float(op.xpath("./td[4]/text()")[0])
            except:
                col4 = ""
            try:
                col5 = float(op.xpath("./td[5]/text()")[0])
            except:
                col5 = ""
            data_list.append([col1, col2, col3, col4, col5])
    except Exception as e:
        print(e)
    return data_list


def write_excel(file_name, write_list):
    """
    定义一个函数, 将每一行的数据汇总的数组，进行遍历，依次写到excel中
    file_name: 入参参数, 指的是写入excel的名字
    write_list: 入参参数, 指的是写入excel的每一行汇总的数组
    """
    full_excel = openpyxl.Workbook()
    full_sheet = full_excel.active
    for i in range(0, len(write_list)):
        full_sheet.append(write_list[i])
    full_excel.save(file_name)


if __name__ == '__main__':
    start_time = datetime.datetime.now()

    """
    URL的规律是XXXX+当前日期+XXXX+当前页号
    """
    now_date = datetime.datetime.now().strftime("%Y-%m-%d")
    every_page_result_list = []  # 空数组接受每一页的所有数据行汇总数据

    """循环每一页获取数据"""
    # pages = 78
    pages = 10
    for index in range(1, pages+1):
        url = "http://fx.cmbchina.com/Hq/History.aspx?nbr=%e7%be%8e%e5%85%83&startdate=2009-01-01&enddate=" + now_date + "&page=" + index.__str__()
        every_page_result_list = every_page_result_list + get_page_data(get_url_html(url))
        print("获取第{0}页成功...".format(index))

    """这里是文件excel写入路径，你可以指定任意存在或者不存在的文件"""
    write_excel(r"D:\test.xlsx", every_page_result_list)

    end_time = datetime.datetime.now()
    print(f"耗时总共{(end_time - start_time).seconds}秒")

'''


# In[148]:


url = "https://f.qianzhan.com/yuanqu/diqu/32/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
html1 = requests.get(url, headers=header).text
##print(html1)
all_company_list={}
page_list = etree.HTML(html1)
print(etree.tounicode(page_list))
option = page_list.xpath('//table[@class="company-table"]/tbody')
option1 = page_list.xpath('//table[@class="company-table"]/tbody/tr/td/text()')
print(option1)


# In[ ]:


for oneSelector in option:
    for i in  range(1, 21):
        name = oneSelector.xpath('tr['+str(i)+']/td[2]/text()')
        city = oneSelector.xpath('tr['+str(i)+']/td[3]/text()')
        city_2 = oneSelector.xpath('tr['+str(i)+']/td[4]/text()')
        city_3 = oneSelector.xpath('tr['+str(i)+']/td[5]/text()')
        address = oneSelector.xpath('tr['+str(i)+']/td[6]/text()')
        area = oneSelector.xpath('tr['+str(i)+']/td[7]/text()')
        company_sum = oneSelector.xpath('tr['+str(i)+']/td[8]/text()')
        one_company_List = [name, city, city_2, city_3, address, area, company_sum]
        all_company_list.append(one_company_List)


# In[122]:


url = "https://gdp.gotohui.com/data-3412"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
html1 = requests.get(url, headers=header).content
import re
import json 
text=str(html1,'utf-8')
res=re.findall(r'[(](.*?)[)]',text)
res


# In[189]:


import numpy as np
data1 = pd.Series(np.random.rand(100)*100).sort_values()


# In[195]:


data = pd.DataFrame({'智商':[106,86,100,101,99,103,97,113,112,110],
                    '每周看电视小时数':[7,0,27,50,28,29,20,12,6,17]})
data.corr(method='spearman')


# In[3]:


#*100表示标准差为100的高斯函数
data = pd.DataFrame(np.random.randn(200,4)*100,columns=['A','B','C','D'])


pd.plotting.scatter_matrix(data,figsize=(10,6),
                c = 'r',
                 marker = '+',
                 diagonal='hist',
                hist_kwds={'bins':50,'edgecolor':'k'},
                 alpha = 0.5,
                 range_padding=0.1)


# In[14]:


for i in data.columns:
    a=data[i].std()
    print(i,a)


# In[199]:


data1 = pd.Series(np.random.rand(50)*100).sort_values()
data2 = pd.Series(np.random.rand(50)*50).sort_values()
data3 = pd.Series(np.random.rand(50)*500).sort_values(ascending=False)
#可知data1与data2呈正线性相关，data1与data3呈正线性相关

fig = plt.figure(figsize=(10,5))

ax1 = fig.add_subplot(1,2,1)
ax1.scatter(data1,data2)
plt.grid(linestyle='--')

ax2 = fig.add_subplot(1,2,2)
ax2.scatter(data1,data3)
plt.grid(linestyle='--')


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False


# In[135]:


import requests
from lxml import etree
url = 'http://www.youtx.com/room/67827/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36", }
body = requests.get(url,headers=headers).text
html = etree.HTML(body)
div_ele = html.xpath('//div[contains(@class,"lists") and contains(@class,"clearfix")]')[3]
print(div_ele) #<Element div at 0x2b37f30>
# print(hhh.xpath('./p/text()'))
cn = etree.tounicode(div_ele)
cn2 = html.xpath('//div[contains(@class,"lists") and contains(@class,"clearfix") and contains(@id,"trafficdiv")]/p/text()')
cn3=html.xpath('/html/body/div/div[3]/div/div/div[2]/div/ul/li[4]/div/div/p/text()')
#print(cn)
print(cn3)


# In[116]:


import json
import time

import requests
from lxml import etree

url = "https://f.qianzhan.com/yuanqu/diqu/32/?pg=1"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
html = requests.get(url, headers=header).text
page_list = etree.HTML(html)
truth_list = page_list.xpath('//table[@class="company-table"]/tbody/tr/td/text()')
print(truth_list)


# In[139]:


import json
import time

import requests
from lxml import etree

url = "https://www.congress.gov/search?q=%7B%22source%22%3A%22legislation%22%7D"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
html = requests.get(url, headers=header).text
page_list = etree.HTML(html)
truth_list = page_list.xpath('/html/body/div[2]/div/main/div/div/div[3]/div[2]/div/div/div[2]/ul/li[2]/label/text()')
print(truth_list)

