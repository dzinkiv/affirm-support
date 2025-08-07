# affirm-support
A customer support website for Affirm utilizing LLMs for a personalized issue resolution.

### Running Backend
#### Create virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
#### Install all dependencies
```
pip install -r requirements.txt
```
#### Start the server
```
uvicorn server.main:app --reload --host 0.0.0.0 --port 8000
```

### Running Frontend
#### Install all dependencies
```
cd frontend
npm i
```
#### Start the app
```
npm run dev
```