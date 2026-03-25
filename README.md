# 🚀 CodeSage AI

An AI-powered web-based code review platform that analyzes code quality, detects inefficiencies, and provides actionable suggestions in real-time.

🔗 **Live Demo:** https://ai-code-reviewer-6epo.onrender.com  

---

## ✨ Features

- 💻 **VS Code-like Editor** using Monaco Editor  
- 🌐 **Multi-language Support** (Python, Java, JavaScript)  
- 🧠 **AI-style Code Analysis** with scoring and suggestions  
- ⚡ **Real-time Feedback** on code quality  
- 🎨 **Modern UI** with animations and theme switching  
- 🌙 **Dark/Light Mode Toggle**  
- 📊 **Code Quality Score (0–10)**  

---

## 🧠 How It Works

1. User writes code in the Monaco Editor  
2. Code is sent to Django backend  
3. Rule-based analysis checks for:
   - Unused variables  
   - Nested loops  
   - Duplicate lines  
   - Basic syntax issues (e.g., missing semicolons in Java)  
4. System returns:
   - Score  
   - Issues  
   - Suggestions  
   - AI explanation  

---

## 🛠 Tech Stack

- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, JavaScript  
- **Editor:** Monaco Editor  
- **Deployment:** Render  

---

## 🚀 Installation (Run Locally)

```bash
# Clone repository
git clone https://github.com/PriyanshiSingh05/ai-code-reviewer.git

# Navigate into project
cd ai-code-reviewer

# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run server
python manage.py runserver
