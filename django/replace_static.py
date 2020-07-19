from pathlib import Path
from web.config import HOME_PATH
import re

index = Path(f"{HOME_PATH}/django/web/index/templates/dashboard.html")
ver_str = index.read_bytes().decode("utf8")

href="../assets/css/material-dashboard.css?v=2.1.2"
href="{% static "/css/material-dashboard.css?v=2.1.2" %}"
tex = 'href="../assets/css/material-dashboard.css?v=2.1.2"'
re.findall('href="../assets(.*)"', ver_str)


ver_str = ver_str.replace('href= "../assets', f"{HOME_PATH}{VUEWEB_PATH}/")

index.write_bytes(ver_str.encode("utf8"))
