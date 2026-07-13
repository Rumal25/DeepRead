# DeepRead
**Research Paper Manager for Deep Learning Researchers**

> Developed by: BOIDYA Rumal (25R8106)
> Course: Object Oriented Web Programming
> Hosei University — 2026

---

##  About This System

DeepRead is a web-based research paper management system
designed specifically for Deep Learning and Reinforcement
Learning researchers. Unlike general tools like Mendeley
or Zotero, DeepRead includes features tailored for RL
researchers such as algorithm tagging, citation graphs,
and experiment tracking.

---

## Database Models (6 Classes)

| Model | Description |
|-------|-------------|
| **Paper** | Core model — stores paper info, status, rating |
| **Author** | Normalized author table linked to Paper (M:M) |
| **Topic** | Algorithm tags e.g. PPO, SAC, DQN (M:M with Paper) |
| **Citation** | Self-referencing FK — paper cites paper |
| **ReadingNote** | Per-paper notes with page numbers (FK to Paper) |
| **Experiment** | Experiments inspired by papers (FK to Paper) |

---

## Key Features

- Add and manage research papers with full metadata
- Set reading status: To Read → Reading → Read → Implemented
- Rate papers 1–5 stars
- Tag papers with RL algorithm topics (PPO, SAC, DQN...)
- Add reading notes with page numbers
- Track experiments linked to source papers
- Citation graph: link papers that cite each other
- Filter papers by status and topic
- Admin panel for database management

---

##  How to Run This System

### Requirements
- Python 3.13+
- pipenv

### Setup Steps

**1. Clone the repository**
```bash
git clone https://github.com/Rumal25/DeepRead.git
cd DeepRead
```

**2. Create and activate virtual environment**
```bash
pipenv --python 3.13
pipenv shell
```

**3. Install dependencies**
```bash
pipenv install django
```

**4. Run database migrations**
```bash
python manage.py migrate
```

**5. Create admin user**
```bash
python manage.py createsuperuser
```

**6. Start the server**
```bash
python manage.py runserver
```

**7. Open in browser**
