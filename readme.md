
Returns calculated file base64 encoded

##testing
Base64 decode in powershell
````
curl.exe -H "Content-Type: multipart/form-data" -F "image=@clear.png" localhost:5000 >> encoded.png
$e = Get-Content("encoded.png")
[System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($e)) | Out-File("out.png")
````