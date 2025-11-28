# Security Roles Documentation: Access Management System

This document outlines the specific security roles required for the Access Management System (AMS) integrated with Microsoft Dynamics 365 and Dataverse. These roles are designed to enforce the principle of least privilege, ensuring users only have access to the data and functionalities necessary for their responsibilities.

--- 

## 1. Access Requestor

**Purpose:** This role is assigned to end-users who need to submit requests for access to various applications or roles within the organization. They can view the status of their own requests.

**Key Privileges on Custom Entities:**
*   **Access Request (cr123_accessrequest):**
    *   Create: Organization (User only can create their own requests)
    *   Read: User (Can read their own requests)
    *   Update: User (Can update their own requests before submission/approval, if allowed by business logic)
    *   Delete: None (Requests should not typically be deleted by the requestor)
    *   Append: User (To link to other records like User or Application)
    *   Append To: User
*   **Application (cr123_application):** Read: Organization (To select available applications)
*   **Role (cr123_role):** Read: Organization (To select available roles within applications)
*   **User (SystemUser):** Read: Business Unit (To view basic user information, e.g., for lookups)

**Other Privileges:**
*   Read: Standard SystemUser records, basic organizational data.
*   Execute: Any associated Power Automate flows triggered by their actions (e.g., submitting a request).

--- 

## 2. Access Approver

**Purpose:** This role is assigned to individuals (e.g., managers, application owners) responsible for reviewing, approving, or rejecting access requests submitted by others.

**Key Privileges on Custom Entities:**
*   **Access Request (cr123_accessrequest):**
    *   Read: Business Unit / Parent: Child Business Unit (To view requests they need to approve or requests within their scope)
    *   Update: Business Unit / Parent: Child Business Unit (To change status, add comments, assign approvals)
    *   Create: None (Typically not creating requests)
    *   Append: Business Unit
    *   Append To: Business Unit
*   **Application (cr123_application):** Read: Organization
*   **Role (cr123_role):** Read: Organization
*   **Approval History (cr123_approvalhistory):** Create, Read, Update: Business Unit (To log approval actions)
*   **User (SystemUser):** Read: Business Unit (To view requestor details)

**Other Privileges:**
*   Execute: Power Automate flows for approval processes.
*   Read: Queue and Queue Item entities (if using queues for approval routing).

--- 

## 3. Access Administrator

**Purpose:** This role is for central administrators who manage the Access Management System itself. They can configure applications, roles, maintain reference data, and oversee all access requests and processes.

**Key Privileges on Custom Entities:**
*   **Access Request (cr123_accessrequest):** Create, Read, Update, Delete: Organization (Full control over all requests)
*   **Application (cr123_application):** Create, Read, Update, Delete: Organization (To add/modify/remove applications)
*   **Role (cr123_role):** Create, Read, Update, Delete: Organization (To add/modify/remove roles)
*   **Configuration (cr123_configuration):** Create, Read, Update, Delete: Organization (To manage system settings)
*   **Approval History (cr123_approvalhistory):** Read, Delete: Organization
*   **User (SystemUser):** Read, Update, Assign: Organization (To manage user assignments to roles, if directly done in AMS)
*   **Team (Team):** Create, Read, Update, Delete: Organization (If AMS leverages Teams for access groups)
*   **Security Role (Role):** Read: Organization (To understand existing security roles)

**Other Privileges:**
*   Read/Write: Dataverse Solution components (e.g., workflows, plugins, web resources related to AMS).
*   Ability to run specific administrative Power Automate flows.
*   Read audit logs for AMS entities.

--- 

## 4. Integration User / Service Principal

**Purpose:** This is a non-interactive user account (or Application User/Service Principal) used by automated processes, such as Power Automate flows, custom integrations, or external systems, to interact with Dataverse.

**Key Privileges on Custom Entities:**
*   **Access Request (cr123_accessrequest):** Create, Read, Update: Organization (As needed by automated flows to create/update requests)
*   **Application (cr123_application):** Read: Organization
*   **Role (cr123_role):** Read: Organization
*   **Approval History (cr123_approvalhistory):** Create: Organization (To log automated approval actions)
*   **User (SystemUser):** Read: Organization

**Other Privileges:**
*   Execute Workflows, Activate Processes (for Power Automate to run within Dataverse context).
*   Read/Write to other entities as strictly required by the integration logic (e.g., updating a user record in Azure AD after approval).

**Important:** This user should have minimal privileges, only what is necessary for the automated processes it performs. It should never be used for interactive login.

--- 

## 5. Read-Only Auditor

**Purpose:** This role is for auditors or compliance officers who need to review access management data and processes without the ability to make any modifications.

**Key Privileges on Custom Entities:**
*   **Access Request (cr123_accessrequest):** Read: Organization
*   **Application (cr123_application):** Read: Organization
*   **Role (cr123_role):** Read: Organization
*   **Approval History (cr123_approvalhistory):** Read: Organization
*   **Configuration (cr123_configuration):** Read: Organization
*   **User (SystemUser):** Read: Organization
*   **Team (Team):** Read: Organization
*   **Security Role (Role):** Read: Organization

**Other Privileges:**
*   Read: Audit Summary and Audit Detail records.
*   Read: System Job (AsyncOperation) records to understand flow executions.

**Important:** This role must have no Create, Update, or Delete privileges on any AMS-related entity.

---

## Security Role Best Practices:

*   **Least Privilege:** Always grant the minimum necessary privileges for each role.
*   **Business Units:** Utilize Business Units to segment data access if your organization has a hierarchical or departmental structure.
*   **Teams:** Use Teams (Owner or Access Teams) to share specific records or to grant collective access to a group of users.
*   **Testing:** Thoroughly test each security role to ensure users can perform their required tasks but cannot access unauthorized information or functionalities.
*   **Documentation:** Keep this documentation updated as security requirements or system functionalities change.
