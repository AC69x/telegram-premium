import os

def find_and_replace_method(file_path, method_signature, replacement_text):
    temp_file_path = file_path + '.temp'
    method_started = False
    found_method = False

    with open(file_path, 'r') as input_file, open(temp_file_path, 'w') as output_file:
        for line in input_file:
            if method_signature in line:
                method_started = True
                found_method = True
                output_file.write(replacement_text)
            elif method_started and '.end method' in line:
                method_started = False
            elif not method_started:
                output_file.write(line)

    os.replace(temp_file_path, file_path)

    if found_method:
        print("Method replaced successfully.")
    else:
        print("Method not found.")

target_smali = os.path.join('decompiled_apk', 'smali', 'org', 'telegram', 'messenger', 'UserConfig.smali')

find_and_replace_method(target_smali, '.method public isPremium()Z', '''.method public isPremium()Z
    .locals 1
    const/4 v0, 0x1
    return v0
.end method
''')

find_and_replace_method(target_smali, '.method public static hasPremiumOnAccounts()Z', '''.method public static hasPremiumOnAccounts()Z
    .locals 1
    const/4 v0, 0x1
    return v0
.end method
''')
