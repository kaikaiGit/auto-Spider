import openpyxl

def createExcell(data, appID):
    # 创建一个新的Excel工作簿
    wb = openpyxl.Workbook()

    # 选择默认的工作表
    sheet = wb.active

    # 设置工作表名称
    sheet.title = f"appID{appID}"

    # 将数据写入工作表
    for row in data:
        sheet.append(row)

    # 保存工作簿
    wb.save(f"dian_dian{appID}.xlsx")
