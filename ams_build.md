# Documentation Plan: Access Management System

Here is a detailed elaboration on each point of the documentation plan.

### 1. Define the Documentation Scope and Audience

This initial step is crucial as it sets the foundation for the entire documentation project. Getting this right ensures that the content you create is relevant, useful, and easy to understand for its intended readers.

*   **1.1. Identify the target audience:**
    *   **System Administrators:** They need deep technical details. Your documentation should cover installation, configuration, security settings, troubleshooting, and backup procedures. They'll need to know how to manage users, roles, and system integrations.
    *   **Developers:** This audience requires information on the system's architecture, data model, APIs, and any custom code (like plugins or scripts). They need to understand how to extend or modify the system.
    *   **End-Users:** These are the non-technical users of the Model-Driven App. They need simple, task-oriented guides. The focus should be on "how-to" instructions for their daily tasks, like submitting an access request or running a report. Use clear language and plenty of screenshots.
    *   **Auditors/Compliance Officers:** They are interested in security, data privacy, and process controls. The documentation should clearly explain how the system enforces security policies, tracks access changes (audit trails), and helps meet regulatory requirements.

*   **1.2. Define the scope:**
    *   Be explicit about what's included and what's not. For example, your scope might be: "This documentation covers the Access Management Model-Driven App, its custom Dataverse tables, and the associated Power Automate flows. It does not cover the standard features of Microsoft Dynamics 365 or the underlying Azure infrastructure."
    *   A clear scope prevents "scope creep" and helps you focus your efforts on what's most important.

### 2. Document the System Architecture

This section provides a high-level overview of the system, helping everyone understand how the pieces fit together.

*   **2.1. Create a high-level architecture diagram:**
    *   Use a tool like Visio, draw.io, or even PowerPoint.
    *   The diagram should show the main components:
        *   Your Access Management System (is it a separate application?)
        *   Microsoft Dynamics 365 (CRM, etc.)
        *   Dataverse (as the central database)
        *   The Model-Driven App (as the user interface)
        *   Any other integrated systems (e.g., Azure Active Directory for user authentication, an HR system for employee data).
    *   Use arrows to show the flow of data and interactions between these components. For example, an arrow from the Model-Driven App to Dataverse labeled "Read/Write Access Requests."

*   **2.2. Describe the components:**
    *   For each box in your diagram, write a short paragraph explaining its function.
    *   **Example for Dataverse:** "Dataverse serves as the primary data repository for the Access Management System. It stores all custom tables related to access requests, approvals, and user permissions. It also hosts the business logic, such as business rules and workflows."
    *   **Example for Model-Driven App:** "The Model-Driven App provides the user interface for all access management tasks. It is built on top of the Dataverse tables and allows users to interact with the data through forms, views, and dashboards."

### 3. Detail the Dataverse Data Model

This is the heart of the technical documentation. It provides a detailed "map" of your data structure.

*   **3.1. Document each Dataverse table:**
    *   Create a section for each custom table (e.g., "Access Request", "Application Role", "Approval History").
    *   For each table, include:
        *   **Purpose:** A clear, one-sentence description (e.g., "The Access Request table stores all requests for new or modified access submitted by users.").
        *   **Columns/Fields:** A list of the important fields in the table. For each field, specify:
            *   **Display Name:** (e.g., "Request Status")
            *   **Schema Name:** (e.g., `cr123_requeststatus`)
            *   **Data Type:** (e.g., Choice, Lookup, Text)
            *   **Description:** (e.g., "Indicates the current stage of the request, such as 'Submitted', 'Approved', 'Rejected'.").
            *   **Required/Optional:** Is the field mandatory?
        *   **Relationships:** Explain how this table connects to others. (e.g., "The Access Request table has an N:1 relationship with the User table, as each request is submitted by one user.").

*   **3.2. Create an Entity-Relationship Diagram (ERD):**
    *   This is a visual version of your data model documentation. It shows the tables as boxes and the relationships between them as lines.
    *   An ERD makes it much easier to understand complex relationships than reading text alone. It's an invaluable tool for developers and administrators.

### 4. Document the Model-Driven App

This section focuses on the user-facing part of the system.

*   **4.1. Provide an overview of the app:**
    *   Start with a brief introduction. What is the app's name? What is its primary purpose? Who should be using it?

*   **4.2. Document the app components:**
    *   **Sitemap/Navigation:** Take a screenshot of the left-hand navigation pane and explain what each link leads to (e.g., "The 'My Requests' link opens a view showing all access requests you have submitted.").
    *   **Views:** For each entity (table), there are often multiple views (e.g., "Active Requests," "All Requests," "Approved Requests"). Document the purpose of each view, what columns it shows, and what filters are applied.
    *   **Forms:** For each table, document the main form that users interact with. You can use a screenshot and annotate it, explaining each section and field.
    *   **Dashboards and Charts:** If you have dashboards, explain what information they provide at a glance. Describe each chart and what it visualizes.

*   **4.3. Create user guides:**
    *   These should be step-by-step guides for the most common tasks.
    *   **Example Task: "How to Submit a New Access Request"**
        1.  "Open the Access Management App." (Include a screenshot of the app icon).
        2.  "In the left navigation, click on 'New Request'." (Highlight the button in a screenshot).
        3.  "Fill out the request form. The 'Application' and 'Role' fields are mandatory." (Show a screenshot of the form with key fields highlighted).
        4.  "Click the 'Save' button at the top of the form."

*   **4.4. Design a Business Process Flow (BPF) for New Access Wizard:**
    *   To enhance user experience, a Business Process Flow will guide users through a wizard-like process for submitting new requests.
    *   **Stage 1: Request Details**
        *   **Step:** Select the Application the user needs access to.
        *   **Step:** Select the specific Role(s) required.
        *   **Step:** Specify if this is a new request, a modification, or a removal of access.
    *   **Stage 2: Justification**
        *   **Step:** Provide a business justification for the access request.
        *   **Step:** Attach any supporting documents (optional).
    *   **Stage 3: Review & Submit**
        *   **Step:** A summary of the request is displayed (read-only).
        *   **Step:** User confirms the details and finishes the process to submit the request.

### 5. Explain the Access Management Logic

This section goes beyond the data and UI to explain the "brains" of the system.

*   **5.1. Document the security model:**
    *   Explain how you are using Dynamics 365's built-in security features.
    *   Describe the custom **Security Roles** you have created (e.g., "Requestor," "Approver," "System Admin"). For each role, explain its privileges (what can users with this role create, read, update, or delete?).
    *   Explain if and how you are using **Business Units** and **Teams**.

*   **5.2. Detail any custom access management logic:**
    *   If you have **Power Automate flows**, document them. For each flow, explain:
        *   What triggers it (e.g., "When a new Access Request record is created").
        *   What it does (e.g., "It sends an approval email to the requestor's manager.").
        *   Any external systems it connects to.
    *   Document any **Business Rules** (e.g., "A business rule on the Access Request form hides the 'Approval Date' field until the 'Status' is set to 'Approved'.").
    *   If you have custom **Plugins** (written in C#), this is where you provide detailed technical documentation for them.

*   **5.3. Describe the access request and approval process:**
    *   Create a flowchart or a step-by-step description of the entire lifecycle of an access request, from submission to fulfillment.
    *   Explain the different stages and what happens at each stage.

### 6. Document Administration and Configuration

This is a guide for the system administrators who will maintain the system.

*   **6.1. Provide setup and configuration instructions:**
    *   If there are settings that can be changed, explain how. For example, you might have a "Configuration" table in Dataverse where you store email templates or approval timeout values. Document what each setting does and how to modify it.
    *   Explain how to set up new applications or roles that can be requested.

*   **6.2. Document user administration tasks:**
    *   Provide instructions for common administrative tasks, such as:
        *   How to assign security roles to users.
        *   How to troubleshoot a failed Power Automate flow.
        *   How to manually override an approval if a manager is unavailable.

### 7. Finalize and Publish the Documentation

The final step is to polish and share your work.

*   **7.1. Review and edit:**
    *   Have someone else read your documentation. Ask someone from each target audience (if possible) to review the relevant sections to ensure they are clear and accurate.
    *   Check for typos, grammatical errors, and broken links or images.

*   **7.2. Choose a documentation platform:**
    *   **SharePoint:** Good for collaboration within an organization. Easy to use for non-technical people.
    *   **Confluence:** A powerful wiki tool, great for creating structured and searchable documentation.
    *   **Git repository (e.g., on Azure DevOps or GitHub) with Markdown files:** This is an excellent "docs-as-code" approach. It allows for version control, peer reviews (pull requests), and can be easily integrated with developer workflows.

*   **7.3. Publish and maintain:**
    *   Make the documentation easily accessible to everyone who needs it.
    *   Documentation is not a one-time task. As the system evolves, the documentation must be updated. Establish a clear process for who is responsible for keeping it current. For example, "All changes to the system must be accompanied by an update to the documentation."
