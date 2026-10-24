try {
    $excel = New-Object -ComObject Excel.Application
    $excel.Visible = $false
    $excel.DisplayAlerts = $false
    $xlsx = "C:\Users\Gayathri S\Downloads\IncuBrix_2027_Growth_Engineer_Option_2_Social_Media_and_Content_Submission_Workbook.xlsx"
    $pdf = "C:\Users\Gayathri S\Downloads\IncuBrix_2027_Growth_Engineer_Option_2_Social_Media_and_Content_Submission_Workbook.pdf"
    $wb = $excel.Workbooks.Open($xlsx)
    Write-Host "Excel opened cleanly! Sheet: $($wb.ActiveSheet.Name)"
    $wb.ExportAsFixedFormat(0, $pdf)
    Write-Host "Exported PDF to: $pdf"
    $wb.Close($false)
    $excel.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null
    Write-Host "Done!"
} catch {
    Write-Host "Error: $($_.Exception.Message)"
}
