# 🧠 Cognitive Distortion Checker

A simple FastAPI-based web app that identifies cognitive distortions in user thoughts using keyword matching. It's useful for educational, psychological, or self-reflection purposes.

## What This Project Does

This application checks a user-submitted thought for common cognitive distortions such as:

- All-or-nothing thinking
- Overgeneralization
- Catastrophizing
- Mind reading
- Should statements
- Labeling
- Mental filter
- Personalization

It returns the original input along with a list of distortions detected using simple keyword rules.

## 🚀 How to Run the App

### 📁 Step 1: Setup Environment

```bash
git clone https://github.com/anu03k/fuseAi.git
cd fuseAi
python -m venv myenv
myenv\Scripts\activate  # On Windows
# OR
source myenv/bin/activate  # On macOS/Linux
pip install -r requirements.txt
```

### 🖥️ Step 2: Run the server

```bash
uvicorn app.main:app --reload
```

### 🧪 Step 3: Run tests (optional)

```bash
# On Windows PowerShell:
$env:PYTHONPATH=".." ; pytest

# On macOS/Linux:
PYTHONPATH=.. pytest
```

You should see output like:
```
5 passed in 2.31s
```

This confirms that all core logic is functioning correctly. You can also run `tests/test_api.py` directly if desired.

## 💬 Interactive Usage via Docs

For a user-friendly, interactive way to test the app, you can visit the automatically generated Swagger UI at:

👉 [http://localhost:8000/docs](http://localhost:8000/docs)

There, you'll find an interface to try out the `/check-distortion` endpoint by entering your thought directly into a text box. Once submitted, the app will return the detected cognitive distortions in real time.

This interface is especially useful for demoing or exploring the API without needing to write any code.

## ⚙️ Configuration Notes

- All the distortion detection logic is implemented in `app/main.py`.
- The keyword rules are defined in the `distortion_keywords` dictionary, structured like this:

```python
distortion_keywords = {
    "all-or-nothing": ["never", "always", "every time", "all"],
    "catastrophizing": ["disaster", "ruined", "worst", "terrible"],
    # ...
}
```

You can add or update the keywords for each distortion category to improve or customize detection.


