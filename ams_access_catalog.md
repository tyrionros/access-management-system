# Access Catalog for Access Management System

This document provides a comprehensive list of common default security roles across the main Dynamics 365 applications. This catalog should be used as a template to populate the `Application` and `Role` tables within the Access Management System.

---

## 1. Core Platform & System Roles

These roles are fundamental to the Dynamics 365 platform and are not tied to a specific app.

| Application               | Role Name              | Description                                                                                                                              |
| ------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **D365 Core Platform**    | **System Administrator** | Has the highest level of access. Can manage all security, users, and customizations. Should be used sparingly.                         |
| **D365 Core Platform**    | **System Customizer**    | Can customize entities, forms, views, and business processes. Cannot manage users or security roles.                                     |
| **D365 Core Platform**    | **Basic User**           | Provides standard privileges to view, create, edit, and delete records for day-to-day tasks.                                              |
| **D365 Core Platform**    | **Read-Only**            | For users who only need to view data and should not have create, update, or delete capabilities.                                        |

---

## 2. Dynamics 365 Sales

Roles designed for users of the Sales Hub and related sales functionalities.

| Application      | Role Name       | Description                                                                                                                     |
| ---------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **D365 Sales**   | **Salesperson** | For sellers who work with leads, opportunities, quotes, orders, and invoices. Can manage their own sales pipeline.              |
| **D365 Sales**   | **Sales Manager** | Manages a team of sellers. Can view team performance, manage sales goals, and access team members' records.                     |
| **D365 Sales**   | **VP of Sales** | Has a high-level view of the entire sales organization, including all territories and business units. Can override and manage sales processes. |

---

## 3. Dynamics 365 Customer Service

Roles for users of the Customer Service Hub, Omnichannel, and case management.

| Application                 | Role Name                       | Description                                                                                                                    |
| --------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **D365 Customer Service**   | **Customer Service Representative** | Manages customer cases, activities, and knowledge articles. The primary role for service agents.                               |
| **D365 Customer Service**   | **CSR Manager**                 | Manages a team of representatives. Can view team queues, dashboards, and performance metrics.                                  |
| **D365 Customer Service**   | **Omnichannel agent**           | A specialized agent role for handling real-time customer interactions across channels like chat, SMS, and social media.            |
| **D365 Customer Service**   | **Omnichannel supervisor**      | Monitors agent conversations, manages agent assignments, and views real-time analytics for the contact center.                 |
| **D365 Customer Service**   | **App Profile Manager Admin**   | Manages app profiles, session templates, and productivity tools for the agent experience.                                      |

---

## 4. Dynamics 365 Field Service

Roles for managing and executing on-site work with work orders.

| Application                | Role Name                      | Description                                                                                                                       |
| -------------------------- | ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| **D365 Field Service**     | **Field Service - Resource**   | For frontline workers (technicians) who execute work orders on-site. Primarily uses the Field Service mobile app.                 |
| **D365 Field Service**     | **Field Service - Dispatcher** | Responsible for scheduling jobs, creating bookings, and assigning work orders to frontline workers. Manages the schedule board.     |
| **D365 Field Service**     | **Field Service - Administrator**| Provides extensive permissions to all Field Service tables and settings. Intended for IT administrators and service managers.     |
| **D365 Field Service**     | **Field Service - Inventory Purchase** | For inventory managers who oversee stock on service vehicles, manage purchasing, and process product returns.                   |
| **D365 Field Service**     | **IoT - Administrator**        | Registers and manages IoT devices and configures business processes based on IoT alerts.                                          |

---

## 5. Dynamics 365 Marketing

Roles for users of the Dynamics 365 Marketing application.

| Application             | Role Name                       | Description                                                                                                                                  |
| ----------------------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **D365 Marketing**      | **Marketing Professional – Business** | For standard marketers who create and manage customer journeys, emails, segments, and marketing pages.                                   |
| **D365 Marketing**      | **Marketing Manager – Business**| Has broader permissions than the Professional role, including the ability to configure marketing settings.                                   |
| **D365 Marketing**      | **Event Planner**               | For users who specifically need to create, manage, and track marketing events.                                                             |
| **D365 Marketing**      | **LinkedIn Lead Gen Salesperson**| A specific role that allows users to view and manage leads generated from LinkedIn Lead Gen Forms.                                           |

---

## 6. Dynamics 365 Project Operations

Roles for managing project-based sales and delivery.

| Application                    | Role Name           | Description                                                                                                                            |
| ------------------------------ | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **D365 Project Operations**    | **Project Manager** | Manages all aspects of a project, including scheduling, resource assignments, budget tracking, and approvals for time and expenses.      |
| **D365 Project Operations**    | **Project Accountant**| Manages the financial aspects of projects, including invoicing, revenue recognition, and project-based accounting.                      |
| **D365 Project Operations**    | **Practice Manager**| Oversees a portfolio of projects, managing resource utilization, profitability, and overall practice health.                           |
| **D365 Project Operations**    | **Resource Manager**| Responsible for staffing projects by matching the skills and availability of consultants with project demands.                         |
| **D365 Project Operations**    | **Team Member**     | For project consultants who need to record time and expenses, update task progress, and manage their own project work.                  |
