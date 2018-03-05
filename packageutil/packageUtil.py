
import xlrd
# 生成多渠道的配置的脚本
excelHome = xlrd.open_workbook('微端打包-卓越20180302.xlsx')
excelHome.sheets()
# 要新和成的
# workbook = Workbook()
# newSheet = workbook.add_sheet('hotel')
count = 1;
for num in range(0,excelHome.sheets().__len__()):
    sheet = excelHome.sheet_by_index(num)
    print("sheet名称;",sheet.name)
    for r in range(0,sheet.nrows):
        channel = "空"
        link = "空"
        for c in range(0,sheet.ncols):
            # print('行', r, '列', c, '数据：', sheet.cell(r, c).value)
            if(c ==1):
                channel =  sheet.cell(r,c).value
                if (isinstance(channel,(int,float))):
                    channel = int(channel)
            if(c ==2):
                link = sheet.cell(r,c).value
            # if(channel.strip() and link.strip()):
            #     print('渠道:',channel,"链接：",link)
        if(channel!="空" and link!="空"):
            # print('第几行',r,'渠道:',channel,"链接：",link)
            # print("ch_",channel,"{ buildConfigField  \" String\", \"GAME_URL\", \"\\\"",link,"\\\"\" }");
            print("ch_%s{buildConfigField  \"String\", \"GAME_URL\", \"\\\"%s\\\"\" }"% (channel,link));
        count = count +1;