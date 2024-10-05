# Throne of Liberty guild managment:

## Architecture Overview

1. Frontend (UI Layer)
   - Web interface for players and guild administrators to interact with the system.
   - This layer will handle user interactions, display data, and send API requests to the backend.
2. Backend (API Layer)
   - FastAPI application for handling API requests.
   - This layer will contain the business logic and communicate with the database layer.
   - It will manage players, events, rewards, guild hierarchy, logs, and more.
3. Database (Data Layer)
   - Relational database (e.g., PostgreSQL or MySQL).
   - Tables for players, events, roles, logs, rewards, and any additional features needed by the guild.


### Additionally, you could include optional layers for future scalability:

Task Queue (for async tasks like sending notifications or processing large data).
Authentication and Authorization (JWT or OAuth2 for managing access control).

## Component Breakdown
1. Players Module:

   - Players can have roles (e.g., Leader, Member, Officer).
   - Each player will have attributes such as stats, participation history, rewards, etc.

2. Event Module:
   - The event system should support different types of events (PvP, PvE, Raids, Sieges).
   - Each event can have specific rules for awarding points, and it should track participation, duration, and outcome.
3. Reward Module:
   - A system that dynamically calculates rewards based on event participation, performance, and other factors.
   - Can include automatic distribution of virtual rewards after each event.

4. Guild Management Module:
   - Guild hierarchy and role management (e.g., Leader, Officer, Member).
   - Ability to track member performance, assign roles, and promote/demote members.
5. Notification/Communication Module (optional for future):
   - Notify players about upcoming events or announcements.
   - Integration with Discord or in-game chat for guild communications.
6. Logs and Analytics Module:
   - A logging system to track activities such as promotions, demotions, participation, and event outcomes.
   - Analytics for event participation, player engagement, and rewards distribution.

## High-Level Software Architecture Diagram
```text
┌────────────────────────────────────────────────────────────┐
│                        Frontend (UI)                       │
│  - Player portal (stats, rewards, participation history)   │
│  - Admin portal (manage events, roles, view logs, etc.)    │
│  - Event scheduling, communication, leaderboard, etc.      │
└────────────────────────────────────────────────────────────┘
                │
                ▼
┌────────────────────────────────────────────────────────────┐
│                        Backend (API)                       │
│  - FastAPI: Handles API requests for players, events, etc. │
│  - Business logic for managing players, events, roles      │
│  - Validation, authentication (JWT/OAuth2)                 │
│  - Integration with Task Queue, Notifications              │
└────────────────────────────────────────────────────────────┘
                │
                ▼
┌────────────────────────────────────────────────────────────┐
│                         Database                           │
│  - Tables for Players, Events, Roles, Rewards, Logs        │
│  - Relational structure with foreign keys                  │
│  - Indexed queries for fast lookups (e.g., by player, event)│
└────────────────────────────────────────────────────────────┘

                 +------------------------------------------+
                 | Optional Modules for Scalability         |
                 +------------------------------------------+
                 | Task Queue (Celery/Redis for async tasks)|
                 | Notifications (email, Discord bot)       |
                 | Logs and Analytics (external service)    |
                 +------------------------------------------+
```

