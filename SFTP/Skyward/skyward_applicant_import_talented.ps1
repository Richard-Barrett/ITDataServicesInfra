$txtfile = "E:\FTP\TalentEd\SkywardApplicantExportSQL.txt"
$csvfile = "E:\FTP\TalentEd\SkywardApplicantExportSQL_$(Get-Date -F 'MM-dd-yyyy').csv"
$addFields = "E:\FTP\TalentEd\SkywardApplicantExportSQL1_$(Get-Date -F 'MM-dd-yyyy').csv"
$Daysback = "-7"
$CurrentDate = Get-Date
$DatetoDelete = $CurrentDate.AddDays($Daysback)
$removeFiles = "E:\FTP\TalentEd\"

#Retrieve SkywardApplicantExportSQL.txt from TalentEd SFTP and download to E:\FTP\TalentEd\SkywardApplicantExportSQL.txt
#Convert SkywardApplicantExportSQL.txt from tab delimited to comma delimited.
Function CommaRename{
(Get-Content $txtfile) -replace “`t”, ", " | Set-Content $csvfile
}
CommaRename

#Wait 10 seconds before implementing addFields function.
Start-Sleep -Second 10.

#Add required fields for Skyward Applicant Import from TalentEd converted csv.
Function addFields{
Import-Csv $csvfile | 
Select-Object "FirstName", "MiddleName", "LastName", "Suffix", "SSN", "StateID", "FormerName", "SpouseName", "Gender", "Birthdate", "MaritalStatus", "House#", "Direction", "Street", "AddrLine2", "S.U.D.", "S.U.D.#", "POBox", "City", "State", "ZIP", "ZIP+4", "County", "Township", "MailingHouse#", "MailingDirection", "MailingStreet", "MailingAddrLine2", "MailingS.U.D.", "MailingS.U.D.#", "MailingPOBox", "MailingCity", "MailingState", "MailingZIP", "MailingZIP+4", "Phone", "PhoneExt", "PhoneCategory", "Phone2", "Phone2Ext", "Phone2Category", "Phone2Type", "Phone3", "Phone3Ext", "Phone3Category", "Phone3Type", "Fax", "Email", "Degree1ProcDate", "Degree1HighestDeg", "Degree1", "Degree1Institution", "Degree1Major", "Degree1Minor", "Degree1RecDate", "Degree1RecYear", "Degree1GPA", "Degree1Credits", "Degree1AddtlCredits", "Degree2ProcDate", "Degree2HighestDeg", "Degree2", "Degree2Institution", "Degree2Major", "Degree2Minor", "Degree2RecDate", "Degree2RecYear", "Degree2GPA", "Degree2Credits", "Degree2AddtlCredits", "Degree3ProcDate", "Degree3HighestDeg", "Degree3", "Degree3Institution", "Degree3Major", "Degree3Minor", "Degree3RecDate", "Degree3RecYear", "Degree3GPA", "Degree3Credits", "Degree3AddtlCredits", "Degree4ProcDate", "Degree4HighestDeg", "Degree4", "Degree4Institution", "Degree4Major", "Degree4Minor", "Degree4RecDate", "Degree4RecYear", "Degree4GPA", "Degree4Credits", "Degree4AddtlCredits", "Cert1Type", "Cert1Number", "Cert1State", "Cert1IssueDate", "Cert1ExpireDate", "Cert1Institution", "Cert1ENDOR1", "Cert1ENDOR2", "Cert2Type", "Cert2Number", "Cert2State", "Cert2IssueDate", "Cert2ExpireDate", "Cert2Institution", "Cert2ENDOR1", "Cert2ENDOR2", "Cert3Type", "Cert3Number", "Cert3State", "Cert3IssueDate", "Cert3ExpireDate", "Cert3Institution", "Cert3ENDOR1", "Cert3ENDOR2", "Cert4Type", "Cert4Number", "Cert4State", "Cert4IssueDate", "Cert4ExpireDate", "Cert4Institution", "Cert4ENDOR1", "Cert4ENDOR2" | 
Export-Csv $addFields -NoTypeInformation
}
addFields

#Wait 10 seconds before implementing addFields function.
Start-Sleep -Second 10.

#Remove Applicant Import files older than 7 days
Function removecsvFiles{
Get-ChildItem $removeFiles | Where-Object { $_.LastWriteTime -lt $DatetoDelete } | Remove-Item
}
removecsvFiles




