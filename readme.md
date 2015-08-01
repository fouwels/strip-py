Accepts a POST to '/' with image = image file.

Decodes and converts to RGBA, then returns base64 encoded as a png.

##testing

Read the .ps1 in /test/, or dot source it and pipe

````
$decoded | Format-Hex
````

(Required the PSCH powershell community extensions)

Base64 decode in powershell
````
curl.exe -H "Content-Type: multipart/form-data" -F "image=@clear.png" localhost:5000 >> encoded.png
$e = Get-Content("encoded.png")
[System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($e)) | Out-File("out.png")
````