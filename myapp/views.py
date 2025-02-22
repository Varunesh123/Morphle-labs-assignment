import subprocess
import datetime
import pytz
import os
import sys
from django.http import HttpResponse

full_name = "Varunesh Pathak"  # Replace with your actual name

# Get username based on OS
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to My Django Project</h1>")

if sys.platform == "win32":
    username = os.getlogin()  # Windows
else:
    import pwd
    username = pwd.getpwuid(1000).pw_name  # Linux/Mac

def htop_view(request):
    ist_time = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))

    # Use `tasklist` instead of `top` for Windows
    if sys.platform == "win32":
        top_output = subprocess.getoutput("tasklist")
    else:
        top_output = subprocess.getoutput("top -b -n 1")

    response_content = f"""
    <pre>
    Name: {full_name}
    Username: {username}
    Server Time (IST): {ist_time.strftime("%Y-%m-%d %H:%M:%S.%f")}
    
    System Process Output:
    {top_output}
    </pre>
    """
    return HttpResponse(response_content, content_type="text/html")
