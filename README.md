# Group work - Team 2 
1) Configured Github for the team.
- Create and cloned repo 
- Tested creating separate branches and pull request to make sure things were working on everyone's machine.
2) Create a VIM in Azure
- Downloaded and shared perm key (because we didn't want to use Azure SDK due to it being slow)
- Made sure that everyone could connect to the VIM from their computers.
3) Create directory structure for the assignment (in visual studio code)
- To make sure that we all had the same structure and configs (DB connection) before starting to work in individual branches.
5) Create Localstorage and database
6) Make sure that everyone was connected to database.
7) Create tables for the database (with error handling)
8) Create API and service 
- Create and test CURD methods
9) Create reporting software
- Create method to fetch daily working hours from database 
- Convert to dataframe for easier processing
- Create nice-looking text file and upload to blob storage.
10) Upload to storage blob
- Confirm that text file was indeed uploaded.
11) Create date validations (for when creating and updating database input)
12) Create cron job so that a report is created and uploaded once a day.
13) Expand db connection solution (Azure key vault instead of database.ini)
14) Expand interface
# Team 2 – Group Project

This repository contains the collaborative work of **Team 2** for our group assignment. The project involves the setup, development, and automation of a cloud-based reporting application using Azure infrastructure, VIM, and a backend API connected to a database. 

---

## 🛠 Project Setup

### 1. GitHub Configuration
- Repository created and cloned by all team members.
- Branching strategy established with successful testing of feature branches and pull requests to ensure smooth collaboration.

### 2. Azure Virtual Machine (VIM)
- Provisioned a VIM instance in Azure to host the application backend.
- SSH key pair generated and shared with the team (used instead of Azure SDK for performance reasons).
- Verified connectivity across all team members.

### 3. Development Environment
- Standardized directory structure and configuration setup in Visual Studio Code.
- Shared initial setup (including database connection settings) to ensure consistency before branching for individual tasks.

---
## 💻 Frontend 
- Created a simple interface (HTML, CSS and JavaScript) where the user can create a new entry to the database, as well as fetch and delete entries from the database. 
- Verified that entries were stored in database. 

## 💾 Backend & Storage

### 4. Database & Local Storage
- Database initialized and shared among all team members.
- Connection verified across different environments.
- Tables created with robust error handling mechanisms.

### 5. API & Services
- CRUD API endpoints implemented and tested.
- Service layer developed for structured interaction with the database.

---

## 📊 Reporting System

### 6. Report Generation
- Daily working hours fetched from the database.
- Data transformed into a Pandas DataFrame for processing.
- Clean, human-readable report generated in `.txt` format.

### 7. Blob Storage Integration
- Daily reports automatically uploaded to Azure Blob Storage.
- Upload process verified with successful file persistence.

---

## 📅 Automation

### 8. Validations & Scheduling
- Date validations implemented for record creation and updates.
- Scheduled daily report generation using a **cron job** managed via **TMux** for persistent background execution.

---

## ✅ Summary

This project demonstrates our end-to-end collaboration using cloud infrastructure, database integration, API development, and automation techniques. The setup is robust, scalable, and designed for collaborative development in a real-world-like environment.

#### What  Next
- Using expanding the solution to use Azure key vault.
