# Solution Architecture: Access Management System

This document provides the solution architecture for the Access Management System (AMS), illustrating the key components and their interactions.

---

### Solution Architecture Diagram

This diagram illustrates the key components of the Access Management System and how they interact with each other, with users, and with the surrounding Microsoft Cloud ecosystem.

#### Mermaid Script

You can render this diagram by pasting the script into a Mermaid-compatible viewer (e.g., `mermaid.live` or plugins in VS Code/Azure DevOps).

```mermaid
graph TD
    subgraph Users
        direction LR
        A[End User / Requestor]
        B[Manager / Approver]
        C[Access Administrator]
    end

    subgraph PowerPlatform
        direction TB
        MDA[Model-Driven App <br/><i>(AMS Interface w/ BPF Wizard)</i>]
        
        subgraph Automation & Logic
            PA[Power Automate Flows <br/><i>(Approval, Notifications, Logic)</i>]
        end

        subgraph Dataverse as Core
            DV_Tables[<b>Custom Tables</b><br/><i>- Access Request<br/>- Application & Role Catalog<br/>- Approval History</i>]
            DV_Security[<b>Security Model</b><br/><i>- AMS Security Roles<br/>- Business Units & Teams</i>]
            DV_Audit[<b>Audit Logs</b><br/><i>(Who, What, When)</i>]
        end
    end

    subgraph MicrosoftEcosystem
        direction TB
        AAD[<b>Azure Active Directory</b><br/><i>User Identity & Authentication</i>]
        D365[<b>Dynamics 365 Apps</b><br/><i>(Sales, Service, etc.)</i>]
        Notifications[Outlook / Teams<br/><i>(Approval Emails & Notifications)</i>]
    end

    %% --- Connections ---
    A -->|1. Submits Request via| MDA
    B -->|5. Approves via Link| MDA
    C -->|Manages System via| MDA
    
    MDA -->|2. Creates/Updates Record in| DV_Tables
    DV_Tables -->|3. Triggers Flow| PA
    
    PA -->|4. Gets Manager & Sends Approval| AAD
    PA -->|4. Sends Notification to| Notifications
    PA -->|6. Updates Record in| DV_Tables
    PA -->|7. Applies Security Role in| DV_Security
    
    DV_Security -->|8. Grants Access to| D365
    
    AAD -->|Secures| MDA
    AAD -->|Provides Identities for| DV_Security
```

---

### Explanation of Components and Flow

#### Key Components

1.  **Users:**
    *   **End User/Requestor:** The employee who needs access.
    *   **Manager/Approver:** The individual responsible for approving the access request.
    *   **Access Administrator:** The IT or system administrator who configures and manages the AMS.

2.  **Power Platform (Core of the AMS):**
    *   **Model-Driven App:** This is the primary user interface. It hosts the forms, views, and the "New Access Wizard" (Business Process Flow - BPF) that users interact with.
    *   **Power Automate Flows:** The automation engine that runs in the background. It handles the approval logic, sends notifications, and applies the security roles upon approval.
    *   **Dataverse:** The secure and scalable database that underpins the entire solution.
        *   **Custom Tables:** Store all the system's data, such as each access request and the catalog of available applications and roles.
        *   **Security Model:** Contains the custom security roles (`Access Requestor`, `Approver`, etc.) that control what users can see and do within the AMS itself.
        *   **Audit Logs:** The native Dataverse auditing feature, which provides a compliant trail of all actions performed.

3.  **Microsoft Ecosystem (Integrated Systems):**
    *   **Azure Active Directory (AAD / Entra ID):** The foundational identity provider. It manages user identities, authentication (including MFA), and user group memberships. The AMS relies on AAD for all user information.
    *   **Dynamics 365 Apps:** The target applications (Sales, Customer Service, etc.) that the AMS grants access *to*.
    *   **Outlook / Teams:** Used by Power Automate to send approval requests and notifications.

#### Workflow (Numbered in the Diagram)

1.  An **End User** opens the **Model-Driven App** and initiates a new request using the guided "wizard" experience.
2.  The app creates a new "Access Request" record in the **Dataverse Tables**.
3.  The creation of this record **triggers a Power Automate Flow**.
4.  The flow looks up the requestor's manager in **Azure AD** and sends an approval notification via **Outlook/Teams**.
5.  The **Manager** receives the notification, clicks a link that takes them to the Model-Driven App, and approves or rejects the request.
6.  The flow captures the approval and **updates the request record** in Dataverse.
7.  If approved, the flow assigns the appropriate security role to the user within the **Dataverse Security Model**.
8.  This newly assigned security role now **grants the user the intended access** to the target **Dynamics 365 App**.

Throughout this entire process, all changes to records are automatically logged by the **Dataverse Audit** feature.
