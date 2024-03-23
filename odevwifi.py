import subprocess
# Komutun çıktısını alın
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
# Tüm profilleri alın
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

# Her profil için ayrıntıları alın
for profile in profiles:
    try:
        # Komutun çıktısını alın
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')

        # Parolayı alın
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

        # Ekrana profil adı ve parolasını yazdırın
        try:
            print ("{:<30}|  {:<}".format(profile, results[0]))
        except IndexError:
            print ("{:<30}|  {:<}".format(profile, ""))
    except subprocess.CalledProcessError:
        print ("{:<30}|  {:<}".format(profile, "ENCODING ERROR"))

# Kullanıcıdan bir tuşa basın
input("")

