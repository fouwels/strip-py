Takes a POST to '/' with the file key'd as 'image'. Accepts most formats.

Decodes and converts to RGBA, then returns base64 encoded as a png.

##Example

~~Read the .ps1 in /test/, or dot source it and pipe to-~~

Execute the .ps1 and check out.png.

If you have a way of writing __bytes__ natively in powershell let me know, but currently sources [io.file] to do it properly.

Base64 decode in powershell
````
$e = (curl.exe -H "Content-Type: multipart/form-data" -F "image=@clear.png" localhost:5000)
$decoded = [System.Convert]::FromBase64CharArray($e, 0, $e.Length)
[io.file]::WriteAllBytes('out.png', $decoded)

Get-Content('out.png') | Format-Hex
````

(Requires the PSCH powershell community extensions)
