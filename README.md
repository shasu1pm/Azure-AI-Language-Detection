# Azure Text Analytics Language Detection

This project demonstrates **Azure Text Analytics Language Detection** using **Azure AI Services and Python**.

## 🚀 Project Overview
- **Project Name**: Azure Text Analytics Language Detection
- **Tools**: Azure AI Services, Python, VS Code, uvicorn/uv toolchain
- **Purpose**: Detect languages in user input using Azure AI / Cognitive Services.

---

## 🛠️ Step-by-Step Setup

### 1️⃣ Create Azure AI Services
- Create a **Resource Group**.
- Create an **Azure AI Language (Cognitive Services)** instance.
- Note down the **Keys** and **Endpoint**.

### 2️⃣ Local Project Setup
- On **Drive D:** create a folder:
  ```
  D:/Azure Text Analytics
  ```
- Open **VS Code**.
- Open the **Azure Text Analytics** folder.
- Open the **Terminal**:
  ```bash
  uv init
  ```

### 3️⃣ Install Dependencies
In the terminal:
```bash
uv add python-dotenv
```

> This will generate **pyproject.toml** and handle environment isolation for your project.

### 4️⃣ Create `.env` file
In the **root folder**, create a file named `.env` with:
```
AI_SERVICE_ENDPOINT=https://your-endpoint.cognitiveservices.azure.com/
AI_SERVICE_KEY=your-key-here
```

(Your provided `.env` already contains these credentials.)

### 5️⃣ Add Python Script
Use your provided `main.py` which:
- Loads environment variables.
- Accepts user text input.
- Calls Azure Text Analytics API to detect languages.
- Displays detected languages.

### 6️⃣ Run the Application
In the terminal:
```bash
uv run main.py
```

Then enter your text in different languages and observe the detected languages in the console.

---

## 📂 Files in Repository
- `main.py`: Main script for detecting languages.
- `.env`: Contains your Azure AI Service endpoint and key.
- `pyproject.toml`: Auto-generated with dependency details.
- `README.md`: This guide.

---

## 🪄 Example Usage
```
Enter some text ("quit" to stop):
Hello World こんにちは世界

Languages Detected: English, Japanese
```

---

## 📈 Extending This Project
- Integrate with a **FastAPI** or **Flask** frontend for a web interface.
- Connect to **Azure Blob Storage** to analyze text files in batches.
- Use the **Azure SDK for Python** for advanced management.
- Add logging and exception monitoring for production use.
---

Happy learning and building with Azure AI! 🌐⚡
