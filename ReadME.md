# 🤖 Hello Agent with UV SDK (Gemini API)

This project demonstrates how to build a simple AI agent using the [UV SDK](https://github.com/universal-ventures/uv-agent-sdk) and Google Gemini API (OpenAI-compatible endpoint). It includes both **synchronous** and **asynchronous** agent execution.

## 🌟 Features

- Integration with Google's Gemini API
- Support for both synchronous and asynchronous operations
- Simple and clean implementation
- Easy to understand and extend
- Environment-based configuration

## 📦 Requirements

- Python 3.8 or above  
- Gemini API Key from [Google AI Studio](https://makersuite.google.com/app)  
- Packages:
  - `agents`
  - `python-dotenv`
  - `asyncio` (standard library)

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AhmedAli0123/Hello-Agent.git
   cd hello-agent
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory
   - Add your Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

## 🚀 Usage

1. **Basic Usage**:
   ```python
   from hello_agent import HelloAgent
   
   agent = HelloAgent()
   response = agent.run("Your prompt here")
   print(response)
   ```

2. **Async Usage**:
   ```python
   import asyncio
   from hello_agent import HelloAgent
   
   async def main():
       agent = HelloAgent()
       response = await agent.run_async("Your prompt here")
       print(response)
   
   asyncio.run(main())
   ```

## 📝 Project Structure

```
hello-agent/
├── hello_agent/
│   ├── __init__.py
│   └── agent.py
├── tests/
│   └── test_agent.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [UV SDK](https://github.com/universal-ventures/uv-agent-sdk) for the agent framework
- [Google Gemini API](https://makersuite.google.com/app) for the AI capabilities



---

## 📦 Requirements

- Python 3.8 or above  
- Gemini API Key from [Google AI Studio](https://makersuite.google.com/app)  
- Packages:
  - `agents`
  - `python-dotenv`
  - `asyncio` (standard library)

---

## ⚙️ Installation

1. **Clone or download the project folder**.

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows