import File as file

class CalculateAttribute:
    def getDataTypeAttribute(filename,nameAtt):
        oldList = file.ColumnFile.getInstance(filename).data.copy()

        for i in oldList:
            if i[0]==nameAtt:
                break
        for j in i[1:]:
            if j=='':
                return None
            if type(j)!= int and type(j)!= float:
                return 'string'
        return 'nummeric'


    def CalculateAttribute(fileIn, fileOut):
        """xử lý các yêu cầu tính toán giữa các thuộc tính
        Xuất file sau khi xử lý xong

        Args:
            fileIn (string): tên file chứa data đầu vào
            fileOut (string): tên file chứa data đầu ra

        Returns:
            list: list chứa data cũ kèm thêm 1 cột thể hiện kết quả biểu thức
        """

        oldList=file.RowFile.getInstance(fileIn).data.copy()

        req=input("Nhập vào phép tính cần tính: ")

        #Xử lý chuỗi request
        req=req.replace(" ","")
        req = req.replace("\\n", "")
        req = req.replace("\"", "")
        req = req.replace("...", "")

        for i in oldList[0]:
            if i in req:
                typeOfAtt=CalculateAttribute.getDataTypeAttribute(fileIn,i)
                if typeOfAtt==None:
                    print("Thuộc tính bạn yêu cầu bị thiếu dữ liệu")
                    return
                if typeOfAtt == 'string':
                    print("Thuộc tính bạn yêu cầu tính không phải số, không thể tính")
                    return

        for i in range(len(oldList)-1):
            row={}
            for j in range(len(oldList[0])) :
                row[oldList[0][j]]=oldList[i+1][j]
            try:
                oldList[i+1].append(eval(req,row))

            except:
                print("Bạn nhập chưa đúng định dạng!")
                break

        oldList[0].append(req)

        # print(oldList)
        file.MakeFile.makeRowFile(fileOut, oldList)
        return oldList



# CalculateAttribute.CalculateAttribute("house-prices.csv")