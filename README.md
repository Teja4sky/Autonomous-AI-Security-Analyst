# Autonomous AI Security Analyst

Autonomous AI Security Analyst is a fully local AI-powered vulnerability detection system that analyzes source code, identifies security vulnerabilities, classifies risk levels, and generates professional security reports using a local Large Language Model (Dolphin LLM via Ollama).

This system works completely offline and demonstrates real-world AI security engineering architecture.

---

## Key Features

• Autonomous vulnerability detection using local LLM  
• Vulnerability classification (Buffer Overflow, Injection, XSS, etc.)  
• Severity scoring system (Critical, High, Medium, Low)  
• Multi-file and folder scanning  
• Professional report generation (TXT and JSON)  
• Fully offline operation  
• Modular and production-style architecture  
• CLI-based security scanning tool  

---

## Architecture
User Input
↓
File Scanner
↓
Code Analyzer
↓
Dolphin LLM (Ollama)
↓
Vulnerability Classifier
↓
Severity Scorer
↓
Report Generator
↓
Security Report Output


---

## Project Structure

```
Autonomous-AI-Security-Analyst/
│
├── core/
│   ├── analyzer.py          # Main AI code analysis engine
│   ├── classifier.py        # Vulnerability classification module
│   ├── scorer.py            # Severity scoring system
│   ├── file_scanner.py      # Scans directories and finds source files
│   ├── report_writer.py     # Generates security reports
│   └── llm_engine.py        # Handles Dolphin LLM interaction
│
├── samples/                 # Sample vulnerable code files for testing
│
├── reports/                 # Generated security report
│
├── main.py                  # Main entry point (CLI controller)
│
├── requirements.txt         # Python dependencies
│
├── README.md                # Project documentation
│
└── LICENSE                  # MIT License
```

---
## Installation

Install Ollama:

https://ollama.com/download

Pull Dolphin model: ollama pull dolphin-mistral:7b


Clone repository:

git clone https://github.com/Teja4sky/Autonomous-AI-Security-Analyst.git

cd Autonomous-AI-Security-Analyst


---

## Usage

Scan folder:

 python main.py --scan samples

Scan single file: python main.py --file samples/test_code.c


---

## Example Output
 File: test_code.c
Vulnerability: Buffer Overflow
Severity: Critical
Score: 9.0
Fix: Replace gets() with fgets()


---

## Version History

 v1.0 — Basic Analyzer  
• Single file analysis  
• Basic LLM integration  


<img width="1902" height="713" alt="v1 OUTPUT" src="https://github.com/user-attachments/assets/4c13f74e-dd76-4ea8-8b94-6a2eb43cce49" />

---

 v2.0 — Autonomous Analyzer  
• Multi-file scanning  
• Automated report generation  


<img width="995" height="242" alt="v2OUTPUT" src="https://github.com/user-attachments/assets/d38538bd-63c7-4e84-a399-54e78c79344f" />

<img width="1903" height="873" alt="v2OUTPUT2" src="https://github.com/user-attachments/assets/7d1863a7-1dc2-4d15-9899-54d0b3a77e2a" />


---

 v3.0 — AI Security Engine  
• Vulnerability classification  
• Severity scoring  
• CLI support  
• Professional reporting  

<img width="1350" height="145" alt="v3OUTPUT" src="https://github.com/user-attachments/assets/3774fb30-c92e-4837-be42-a2411d8a5e8b" />

<img width="784" height="492" alt="v3output2" src="https://github.com/user-attachments/assets/63449f2a-48bd-467b-8fd5-a520c82fa5a4" />



---

## Technologies Used

Python  
Large Language Models (LLM)  
Ollama  
Dolphin LLM  
Cybersecurity Analysis  
AI Security Engineering  

---

## Use Cases

• AI Security Research  
• Vulnerability Analysis  
• Secure Code Review  
• AI Security Engineering Projects  
• Educational and Research purposes  

---

## Author

Teja Surya  
AI / ML Engineer | Cybersecurity Enthusiast

GitHub: https://github.com/Teja4sky

---

## License

MIT License
