# Flask + Redis Counter 🚀

A simple containerized web application built with **Python Flask and Redis**, orchestrated using **Docker Compose**.

The application demonstrates how two independent containers communicate over a Docker network while sharing application state through Redis.

## 🏗️ Architecture

The application consists of two services:

- **Flask (`web`)** – Handles HTTP requests and application logic.
- **Redis (`cache`)** – Stores and manages the visit counter.

### Request Flow

```text
          Browser
             |
             | HTTP :8008
             v
      Flask Container
             |
             | Redis command
             | cache:6379
             v
      Redis Container
             |
             | Counter stored
             v
       Updated Result
             |
             v
          Browser
```

## ✨ Features

- Flask web application with two routes.
- Redis-backed visit counter.
- Dockerized Flask application using a custom Dockerfile.
- Docker Compose orchestration for multiple containers.
- Container-to-container communication through Docker networking.
- Automatic service discovery using Docker's embedded DNS.
- Environment variables for Redis connection configuration.
- Redis health checks and startup dependency management.
- Named Docker volume for Redis data storage.
- Simple responsive-style interface using HTML and CSS.

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Application programming |
| Flask | Web framework |
| Redis | In-memory data store |
| Docker | Containerization |
| Docker Compose | Multi-container orchestration |
| HTML & CSS | User interface |

## 📁 Project Structure

```text
flask-redis-counter/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
└── docker-compose.yml
```

## ⚙️ Getting Started

### Prerequisites

- Docker Desktop or Docker Engine
- Docker Compose

### 1. Clone the repository

```bash
git clone git@github.com:Fetu-Deen/flask-redis-app.git
cd flask-redis-counter
```

### 2. Start the application

```bash
docker compose up --build
```

Docker Compose builds the Flask image, prepares the Redis image, creates the network and volume, and starts the services.

The Flask service waits until Redis passes its health check before starting.

### 3. Access the application

Open your browser:

- Homepage: `http://localhost:8008/`
- Visit counter: `http://localhost:8008/count`

Each request to `/count` increments the Redis counter.

### 4. Stop the application

```bash
docker compose down
```

To also remove the named volume:

```bash
docker compose down -v
```

**Note:** Removing the volume deletes its stored data. Redis persistence must also be enabled and successfully writing data for the counter to survive container recreation.

## 🐳 Docker Concepts Practiced

This project provided hands-on experience with:

1. **Docker Images and Containers** – Building custom images and running multiple containers.
2. **Dockerfile Instructions** – Understanding `FROM`, `WORKDIR`, `COPY`, `RUN`, `EXPOSE`, and `CMD`.
3. **Layer Caching** – Separating dependency installation from application source copying.
4. **Docker Compose** – Defining and orchestrating multiple services.
5. **Container Networking** – Allowing Flask and Redis to communicate over a shared Docker network.
6. **Embedded DNS** – Using the Compose service name `cache` instead of hardcoding Redis's container IP.
7. **Port Mapping** – Exposing the Flask application through host port `8008`.
8. **Environment Variables** – Configuring Redis host and port independently of application source code.
9. **Health Checks** – Using `redis-cli ping` to verify Redis readiness.
10. **Named Volumes** – Providing persistent storage for Redis data files.

## 🧠 Key Takeaway

The main objective was to understand how independently running containers work together to deliver a functional application.

Rather than running Flask and Redis directly on the host machine, each service runs in its own container, communicates through Docker networking, and is managed through Docker Compose.

A small project, but a practical introduction to containerization and multi-container application architecture.

---

**Built as part of my hands-on journey toward becoming a DevOps Engineer.**