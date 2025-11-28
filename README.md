# Access Management System (AMS)

This project is a solution designed to automate and formalize the process of requesting, approving, and auditing user access to Microsoft Dynamics 365 applications. Its primary goals are to improve operational efficiency, enhance the user experience for access requests, and ensure compliance with security standards like ISO 27001.

## Technologies & Architecture

- **Core Platform:** The system is built on the **Microsoft Power Platform**.
- **User Interface:** A **Model-Driven App** serves as the primary interface for all users (requestors, approvers, and administrators). It includes a guided "New Access Wizard" using a Business Process Flow (BPF).
- **Automation & Logic:** **Power Automate** flows are the backbone of the system, handling approval routing, notifications, and the automated provisioning/revocation of security roles.
- **Database:** **Microsoft Dataverse** is the central data repository, storing custom tables for access requests, the application/role catalog, and approval history. It also manages the security model and provides comprehensive audit logs.
- **Identity:** The system relies on **Azure Active Directory (Entra ID)** for user identity, authentication, and retrieving the organizational hierarchy (e.g., for finding a user's manager).

## Building and Running

The project uses a formal Continuous Integration and Continuous Deployment (CI/CD) process orchestrated with **Azure DevOps**.

### Environment Strategy

The project follows a standard multi-environment strategy:
1.  **Development:** Individual unmanaged environments for developers.
2.  **Build:** An automated pipeline environment for generating the managed solution artifact.
3.  **UAT (User Acceptance Testing):** A managed environment for business user validation.
4.  **Production:** The final, live managed environment for end-users.

### Key Commands & Process

Building and deploying the AMS is not done via simple command-line execution but through a structured Azure DevOps pipeline defined in YAML.

**CI Pipeline (`ams-ci-pipeline.yml`):**
1.  **Trigger:** Runs on pushes to `develop` and `release/*` branches.
2.  **Pack Solution:** Uses the **Power Platform CLI** to pack the unmanaged source code into a solution zip file.
3.  **Publish Artifact:** Publishes the unmanaged solution zip (`AccessManagementSystem_unmanaged.zip`) and any compiled plugin assemblies as a build artifact.

**CD Pipeline (`ams-cd-pipeline.yml`):**
1.  **Trigger:** Runs after the CI pipeline completes successfully.
2.  **Generate Managed Solution:** The pipeline first imports the unmanaged artifact into the **Build** environment and exports it as a **managed** solution (`AccessManagementSystem_managed.zip`). This managed artifact is the "golden copy" for all other deployments.
3.  **Deploy to UAT:** Deploys the managed solution to the UAT environment, imports configuration data, and runs post-deployment steps like activating flows. This stage often includes a manual approval gate.
4.  **Deploy to Production:** After UAT validation, a final manual approval gate allows the same managed solution to be deployed to the Production environment.

**TODO:** While the process is documented, the actual YAML pipeline files (`ams-ci-pipeline.yml`, `ams-cd-pipeline.yml`) are not present in the repository. These would need to be created in Azure DevOps to fully implement the CI/CD strategy.

## Development Conventions

### Source Code Management

- **Branching:** The project uses a GitFlow-like branching strategy:
    - `main`: Production-ready code.
    - `develop`: Main integration branch for new features.
    - `feature/*`: For developing new functionality.
    - `release/*`: For preparing a production release.
- **Pull Requests:** All `feature` branches must be merged into `develop` via a Pull Request.

### Security Model

- **Least Privilege:** Security roles are designed with the principle of least privilege in mind. The specific roles are:
    - `Access Requestor`: For all standard end-users.
    - `Access Approver`: For managers.
    - `Access Administrator`: For system managers.
    - `Read-Only Auditor`: For compliance and security teams.
- **Dataverse Security:** The system relies heavily on Dataverse's built-in security model, including business units and teams, to control data visibility.

### Testing Practices

- **Persona-Based Testing:** The QA plan is structured around four key personas: **Priya (Requestor)**, **Anand (Approver)**, **Sam (Administrator)**, and **Rita (Auditor)**.
- **Checklist:** A detailed test checklist exists (`ams_qa_test_plan.md`) covering happy paths, negative test cases, and security scenarios for each functional area of the application.
