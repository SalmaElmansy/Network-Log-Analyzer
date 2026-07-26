device_type =input("Enter Your device_type: ").lower()
ip_address =input("Enter Your ip_address: ")
login_attempts =int(input("Enter Your log_data: "))
is_admin_flag =input("Is_admin_flag(True/False):" ).title()
log_data = [device_type, ip_address, login_attempts, is_admin_flag]
if log_data[0]=="firewall":
    if log_data[2]<=3:
        if log_data[3]=="True":
          if log_data[1]=="192.168.1.1" :
              print("Status 200: Authorized Admin Access from Master IP.")
          else:
                print("Warning 301: Admin Access attempt from non-master IP!")
        else:
            print("Status 201:Normal Firewall User Activity.")
    else:
            print("Alert 401: Brute Force Attempt Detected on Firewall!")
elif log_data[0]=="server":
    print("Notice:Server Log Redirected to Server Panel.")
else:
        print("Error 404: Unknown Device Log!")
    