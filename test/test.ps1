$e = (curl.exe -H "Content-Type: multipart/form-data" -F "image=@clear.png" localhost:5000)
$decoded = ([System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($e)))
$decoded | Out-File("out.png")
