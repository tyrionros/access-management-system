# User Stories for Access Management System

This document outlines the functional requirements for the Access Management System (AMS) in the form of user stories. Each story represents a specific user need and is accompanied by acceptance criteria to define its scope and completion.

---

## 1. Personas

*   **Priya (Requestor):** A standard employee (e.g., a salesperson, a marketing professional) who needs access to Dynamics 365 applications to perform her job.
*   **Anand (Approver):** A manager or application owner who is responsible for approving access requests for their team or the systems they own.
*   **Sam (Administrator):** A system administrator responsible for configuring and maintaining the AMS, including the catalog of available applications and roles.
*   **Rita (Auditor):** A compliance or security officer who needs to review access logs and processes to ensure the organization meets its regulatory requirements.

---

## 2. Epic: Implement a Compliant Access Management System

As an organization, we want to implement a centralized and automated system for managing user access to Dynamics 365 applications, so that we can improve operational efficiency, enhance user experience, and ensure compliance with security standards like ISO 27001.

---

## 3. User Stories & Acceptance Criteria

### 3.1 Submitting a New Access Request

*   **Story:** As **Priya (Requestor)**, I want to use a guided wizard to request access to a new application or role, so that I can easily and correctly submit my request without needing to know the internal approval process.

*   **Acceptance Criteria:**
    1.  When I click "New Request," I am presented with a Business Process Flow (wizard) at the top of the form.
    2.  The first stage requires me to select the Application I need access to from a predefined list.
    3.  Once I select an Application, the "Role" lookup is filtered to show only the roles associated with that application.
    4.  I must provide a business justification for the request.
    5.  The system automatically identifies me as the requestor.
    6.  When I finish the wizard and save the form, the request is submitted and its status is set to "Submitted."
    7.  After submission, the request becomes read-only for me.
    8.  I can view a list of all my past and present requests and their current status.

### 3.2 Approving an Access Request

*   **Story:** As **Anand (Approver)**, I want to receive a notification for new access requests and be able to approve or reject them from a simple interface, so that I can quickly and responsibly action requests assigned to me.

*   **Acceptance Criteria:**
    1.  When a request is submitted by one of my direct reports, I receive an email notification.
    2.  The email contains key details of the request (Who, What, Why) and a direct link to the request record in the Model-Driven App.
    3.  From the request form, I can see all the details provided by the requestor.
    4.  I have the ability to "Approve" or "Reject" the request.
    5.  I can add comments before approving or rejecting. My comments are logged in an "Approval History" section.
    6.  If I approve, the request status changes to "Approved," and the system automatically grants the user the requested security role.
    7.  If I reject, the request status changes to "Rejected," and the requestor is notified.

### 3.3 Managing the Access Catalog

*   **Story:** As **Sam (Administrator)**, I want to be able to add, modify, and remove the applications and roles in the access catalog, so that the options available to requestors are always accurate and up-to-date.

*   **Acceptance Criteria:**
    1.  I have access to an "Administration" area in the Model-Driven App.
    2.  In this area, I can create, update, and deactivate `Application` records.
    3.  I can also create, update, and deactivate `Role` records.
    4.  I can associate one or more Roles with an Application through a simple interface (a sub-grid on the Application form).
    5.  Deactivating an application or role means it will no longer appear in the lookup fields for new requests.

### 3.4 Auditing Access History

*   **Story:** As **Rita (Auditor)**, I want to be able to view a complete and immutable history of any access request, so that I can verify that the process was followed correctly and provide evidence for compliance audits.

*   **Acceptance Criteria:**
    1.  I have a read-only security role that gives me access to all records in the AMS.
    2.  For any given access request, I can see who requested it and when.
    3.  I can see who approved or rejected it, when they did so, and any comments they made.
    4.  I can use the built-in Dataverse Auditing feature to see a log of all field changes on the request record.
    5.  I can create a report or view showing all access granted to a specific user or for a specific application within a given timeframe.
