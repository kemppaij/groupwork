# Time reporting application
This repository contains the collaborative work of **Team 2** for our group assignment. The project involves the setup, development, and automation of a cloud-based reporting application using Azure infrastructure, VIM, a backend API connected to a database and a basic frontend interface.



## 🛠 Project Setup

#### GitHub Configuration
- Repository created and cloned by all team members.
- Branching strategy established with successful testing of feature branches and pull requests to ensure smooth collaboration.

#### Azure Virtual Machine (VIM)
- Provisioned a VIM instance in Azure to host the application backend.
- SSH key pair generated and shared with the team (used instead of Azure SDK for performance reasons).
- Verified connectivity across all team members.

#### Development Environment
- Standardized directory structure and configuration setup in Visual Studio Code.
- Shared initial setup (including database connection settings) to ensure consistency before branching for individual tasks.



## 💾 Backend
- Database initialized and shared among all team members.
- Connection verified across different environments.
- Tables created with robust error handling mechanisms.
- CRUD API endpoints implemented and tested.
- Service layer developed for structured interaction with the database.

## 💻 Frontend 
- Created a simple interface (HTML, CSS and JavaScript) where the user can create a new entry to the database, as well as fetch and delete entries from the database. 
- Verified that entries were stored in database. 


## 📊 Report Generation
- Daily working hours fetched from the database.
- Data transformed into a Pandas DataFrame for processing.
- Clean, human-readable report generated in `.txt` format.

## 📦 Blob Storage Integration
- Daily reports automatically uploaded to Azure Blob Storage.
- Upload process verified with successful file persistence.



## 📅 Automation
- Date validations implemented for record creation and updates.
- Scheduled daily report generation using a **cron job** managed via **TMux** for persistent background execution.

## ✅ Summary

This project demonstrates our end-to-end collaboration using cloud infrastructure, database integration, API development, and automation techniques. The setup is robust, scalable, and designed for collaborative development in a real-world-like environment.

#### What  Next
- Using expanding the solution to use Azure key vault.
- Improve the frontend.
