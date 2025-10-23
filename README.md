# Cloud-Environment-Provisioning-API-Simulator-
# Cloud Environment Provisioning API (Simulator)

A backend API that simulates **automated provisioning of cloud environments** — built using **FastAPI**, **Pydantic**, and **SQLModel**.

This project demonstrates how a cloud infrastructure automation platform might work internally: accepting environment requests, simulating provisioning workflows, tracking their states, and managing environment lifecycle.  

Later, this simulation can scale to integrate real AWS services like **Lambda**, **Step Functions**, and **DynamoDB**.

---

## Project Goal

The goal of this project is to:
- Learn **FastAPI** in depth by implementing all its key features (validation, auth, async tasks, etc.).
- Understand how backend APIs can **automate and orchestrate cloud provisioning**.
- Build a **scalable foundation** that could later connect to real AWS services.

---

## Tech Stack

| Layer | Technology | Purpose |
|--------|-------------|----------|
| **Framework** | [FastAPI](https://fastapi.tiangolo.com/) | Core API and routing framework |
| **Validation** | [Pydantic](https://docs.pydantic.dev/) | Input/output validation |
| **ORM** | [SQLModel](https://sqlmodel.tiangolo.com/) | Simplified SQLAlchemy ORM + Pydantic |
| **Database** | SQLite (local) → PostgreSQL (scalable) | Persistent data storage |
| **Auth** | JWT (JSON Web Tokens) | Authentication & authorization |
| **Async Tasks** | FastAPI BackgroundTasks | Simulate provisioning |
| **Testing** | Pytest + HTTPX | API testing |
| **Deployment** | Docker / Uvicorn | Local or containerized deployment |
| **Future** | AWS Lambda, Step Functions, Boto3 | Real provisioning workflows |

---

## Major Features

✅ User Authentication (Signup/Login with JWT)  
✅ Create new cloud environments (API-driven)  
✅ Async simulation of environment provisioning  
✅ List, view, update, and delete environments  
✅ Validation & schema enforcement with Pydantic  
✅ Background tasks (simulate async provisioning)  
✅ Error handling and status tracking  
✅ Pagination and filtering  
✅ Ready for AWS integration (Boto3-based workflows)  

---

## Project Architecture


In future, AWS services (Lambda + Step Functions) can handle real provisioning tasks, with FastAPI acting as the orchestration API.

---

## 🔌 API Endpoints

| Method | Endpoint | Description 
|--------|-----------|--------------
| `POST` | `/auth/signup` | Register new user 
| `POST` | `/auth/login` | Login and get JWT token 
| `POST` | `/environments` | Create new environment 
| `GET` | `/environments` | List all environments (with filters/pagination) 
| `GET` | `/environments/{id}` | View details of one environment 
| `DELETE` | `/environments/{id}` | Delete or deprovision environment 
| `GET` | `/health` | Health check endpoint 

---

## Example Workflow

1. User signs up and logs in to get a JWT token  
2. Sends `POST /environments` with a JSON body
3. This API will, in turn, call a step function, which will trigger a set of the lambda functions.
