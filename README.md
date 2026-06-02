**Silly Website Invite**

A minimal web app that renders a single invite page from templates. Good for testing local development and simple deployments.

https://silly-website-invite.onrender.com/

**Requirements**
- **Python**: 3.8+ recommended.
- **Dependencies**: See [requirements.txt](requirements.txt).

**Setup (Windows PowerShell)**

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Setup (macOS / Linux)**

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Run locally**

```bash
python app.py
# Open http://127.0.0.1:5000/ in your browser
```

**Files of interest**
- **App entry**: [app.py](app.py)
- **Template**: [templates/index.html](templates/index.html)
- **Dependencies**: [requirements.txt](requirements.txt)
- **Render deploy config**: [render.yaml](render.yaml)

**Deploy**
This project includes a Render manifest (render.yaml) for easy deployment on Render.com. Follow Render's docs and import this repo or use the dashboard to create a new web service from the manifest.

**Notes**
- Edit the template in [templates/index.html](templates/index.html) to change the invite content.
- If you need HTTPS or a different host/port, update `app.py` accordingly.


