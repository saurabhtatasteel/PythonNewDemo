def changeFile(path, findText, replaceText, lineNo):
    try:
        try:
            fo = open(path, "r")
            allData = fo.read()
        finally:
            fo.close()

        allDataList = allData.split('\n')
        newData = ''
        tempCurrentLine = ''

        for x in range(len(allDataList)):
            tempCurrentLine = allDataList[x]
            if x+1 ==lineNo:
                tempCurrentLine = tempCurrentLine.replace(findText, replaceText)
                
            newData = newData + tempCurrentLine + "\n"
        try:   
            fo = open(path, "w+")
            #writing  newData into original file
            fo.write(newData)
        finally:
            fo.close()

    except Exception(e):
        result = e.args
    else:
        result = "File Changed Successfully" 

    return result

output = changeFile("C:\\Users\\Saurabh\\Desktop\\Temp Saved.txt","Deloitte","Deloitte Company",17)
print (output)