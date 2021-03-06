import File as file

class StandardizeMinMax:
    """Chuẩn hoá dữ liệu theo phương pháp Min-Max
    """

    @staticmethod
    def CalculateMinMax(min_i, max_i, value):
        """tính toán giá trị mới của value đầu vào

        Args:
            min_i (int): giá trị min cũ của value
            max_i (int): giá trị max cữ của value
            value (float): giá trị cần chuẩn hoá

        Returns:
            float: giá trị sau khi chuẩn hoá theo thang [0, 1]
        """
        if (max_i-min_i)<=0.000000000001 :
            return max_i
        return (value-min_i)/(max_i-min_i)*(1-0)+0

    @staticmethod
    def StandardizeMinMax(fileIn, fileOut,attrb):
        """chuẩn hoá giá trị số trong file fileIn
        Xuất kết quả ra file fileOut

        Args:
            fileIn (string): tên file đầu vào
            fileOut (string): tên file đầu ra

        Returns:
            list: trả về data của file mới ở dạng cột 
        """

        # Đọc data theo cột, mỗi cột là 1 attribute
        oldList = file.ColumnFile.getInstance(fileIn).data.copy()

        find=False
        for i in range(len(oldList)):
            if oldList[i][0]==attrb:
                find=True
                break

        if find==False:
            print("Không tồn tại thuộc tính bạn yêu cầu")
            return None

        # Lấy data cột đó mà không có header
        newList = oldList[i][1:]

        # Kiểm tra xem attb có phải nummeric không
        isNumber = True

        j = 0
        while j in range(len(newList)):
            if (newList[j] != ''):
                if(type(newList[j]) != int and type(newList[j]) != float):
                    isNumber = False
                    break
            else:
                newList.pop(j)
                j -= 1
            j += 1

        if len(newList)==0:
            print("Thuộc tính bạn yêu cầu không có giá trị")
            return None

        if isNumber == False:
            print("Thuộc tính bạn yêu cầu có giá trị không phải số")
            return None

        if isNumber == True:
            a = min(newList)
            b = max(newList)
            for j in range(1, len(oldList[i])):
                if oldList[i][j] != '':
                    oldList[i][j] = StandardizeMinMax.CalculateMinMax(a, b, oldList[i][j])

        file.MakeFile.makeColumnFile(fileOut, oldList)

        print("Chuẩn hóa thành công")
        return oldList
