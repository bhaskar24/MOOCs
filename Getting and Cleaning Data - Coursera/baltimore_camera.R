require("XLConnect")

if (!file.exists("data"))
{
	dir.create("data")
}

fileUrl <- 'http://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FDATA.gov_NGAP.xlsx'
download.file(fileUrl, destfile = '/home/shubham/Dropbox/MOOCs/Getting and Cleaning Data - Coursera/data/ngap.xlsx')
list.files("/home/shubham/Dropbox/MOOCs/Getting and Cleaning Data - Coursera/data")

cameraData <- readWorksheetFromFile(loadWorkbook("/home/shubham/Dropbox/MOOCs/Getting and Cleaning Data - Coursera/data/ngap.xlsx"), sheet=1)

head(cameraData)

