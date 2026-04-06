██████╗  ██████╗ ████████╗███████╗██╗    ██╗██╗████████╗██╗  ██╗
██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝██║    ██║██║╚══██╔══╝██║  ██║
██████╔╝██║   ██║   ██║   █████╗  ██║ █╗ ██║██║   ██║   ███████║
██╔══██╗██║   ██║   ██║   ██╔══╝  ██║███╗██║██║   ██║   ██╔══██║
██║  ██║╚██████╔╝   ██║   ███████╗╚███╔███╔╝██║   ██║   ██║  ██║
╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝ ╚══╝╚══╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝

              BOTSmith Labs – StaffCAD Edition

StaffCAD is a lightweight moderation control panel built with Flask.  

It allows staff members to log in, manage other staff, and record moderation actions such as warnings, bans, kicks, and notes.  

This project is created and maintained by \*\*@codebullet23\*\*.



\---



\## 📌 Features



| Category | Details |

|---------|---------|

| \*\*Authentication\*\* | Login, logout, forced password change, default admin creation |

| \*\*Staff Management\*\* | Add staff, list staff, assign roles (admin/moderator) |

| \*\*Moderation Tools\*\* | Log actions (warn, ban, kick, note), track timestamps, track staff responsible |

| \*\*Dashboard\*\* | View the 50 most recent actions in a clean table |

| \*\*Database\*\* | SQLite backend using SQLAlchemy |

| \*\*UI\*\* | Bootstrap‑styled templates |



\---



\## 📁 Project Structure



.

├── init.py

├── auth.py

├── actions.py

├── staff.py

├── models.py

├── extensions.py

├── templates/

│   ├── base.html

│   ├── auth/

│   ├── actions/

│   └── staff/

└── cad.db



\---



\## 🚀 Setup Instructions



1\. Clone the repository:

&#x20;  ```bash

&#x20;  git clone https://github.com/codebullet23/staffcad.git

&#x20;  cd staffcad



