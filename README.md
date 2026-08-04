# 🤖 AI-Based IT Helpdesk Chatbot

---

## 🚀 About the Project

This project is a simple yet powerful AI-based IT Helpdesk Chatbot that helps users quickly solve common technical issues like WiFi problems, VPN errors, password resets, and more.

Instead of waiting for IT support, users can get instant, step-by-step solutions. The chatbot combines a predefined knowledge base with AI to make responses both accurate and easy to understand.

---

## ✨ What It Can Do

* 🔽 Lets users select common issues from a dropdown
* ✍️ Allows custom queries for flexibility
* 🧠 Uses AI (Claude) to give clear, helpful responses
* 📚 Uses a knowledge base for consistent answers
* 📂 Organizes issues into categories (Network, System, etc.)
* 🎟️ Includes a simple “raise ticket” option
* 🌐 Can be deployed online and shared easily

---

## 📸 How It Looks

### 🖥️ Main Interface
<img width="1918" height="1006" alt="image" src="https://github.com/user-attachments/assets/1cb21cdd-f875-4962-8607-541e93dd2b64" />

---

## 🛠️ Built With

* Python
* Streamlit (for the interface)
* Claude AI (for intelligent responses)
* JSON (for storing common issues and solutions)

---

## 📁 Project Structure

```
AI-Helpdesk-Chatbot/
│
├── app.py                # Main application
├── it_helpdesk.json      # Knowledge base
├── requirements.txt      # Dependencies
└── README.md             # Documentation
```

---

## ⚙️ How to Run It

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-helpdesk-chatbot.git
cd ai-helpdesk-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your API key

Set your Claude API key as an environment variable:

**Windows:**

```bash
setx ANTHROPIC_API_KEY "your_api_key_here"
```

### 4. Run the app

```bash
python -m streamlit run app.py
```

---

## 🌐 Deployment

You can easily deploy this project using Streamlit Community Cloud.
Just make sure to add your API key in the **Secrets** section:

```
ANTHROPIC_API_KEY = "your_api_key_here"
```

---

## 🎯 Why This Project

In many companies, IT teams spend a lot of time solving the same basic issues again and again. This chatbot helps reduce that load by giving users quick answers on their own.

It improves response time, saves effort, and makes the overall support process smoother.

---

## 🔮 What Can Be Added Next

* 💬 A proper chat-style interface
* 👍 Feedback system (Was this helpful?)
* 📊 Basic analytics (most common issues)
* 🌐 Multi-language support
* 🔗 Integration with real ticketing tools

---

## 👩‍💻 Author

This project was created as a practical implementation of AI in IT support to improve productivity and user experience.

---

## ⭐ Final Note

If you found this project useful or interesting, feel free to give it a ⭐ on GitHub!

And don’t forget to keep your API keys secure 🔐
