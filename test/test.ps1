$e = (curl.exe -H "Content-Type: multipart/form-data" -F "image=@clear.png" localhost:5000)

echo "Raw: " $e
echo ""
$decoded = [System.Convert]::FromBase64CharArray($e, 0, $e.Length)
[io.file]::WriteAllBytes('out.png', $decoded)

Get-Content('out.png') | Format-Hex