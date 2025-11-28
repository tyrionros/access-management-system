# Build and Deployment Plan: Access Management System for Dynamics 365

## 1. Introduction

This document outlines the comprehensive build and deployment (CI/CD) strategy for the Access Management System (AMS) project. The goal is to establish a standardized, automated, and reliable process for moving the solution from development through to production. This plan leverages Azure DevOps for orchestration and the Power Platform Build Tools to interact with the Dataverse environments.

## 2. Environment Strategy

A multi-environment strategy is essential for ensuring quality and stability. Each environment serves a distinct purpose.

| Environment      | Purpose                                                                                                  | Solution Type | Managed By                                       |
| ---------------- | -------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------ |
| **Development**  | Individual developer sandboxes for building and testing new features. Source of all customizations.        | Unmanaged     | Developers                                       |
| **Build**        | Automated environment used exclusively by the CI/CD pipeline to validate the unmanaged solution and generate the managed solution artifact. | Unmanaged -> Managed | Azure DevOps Service Principal                 |
| **UAT (User Acceptance Testing)** | Staging environment for business users and testers to validate features before a production release. Mirrors production as closely as possible. | Managed       | Release Pipeline / Quality Assurance Team        |
| **Production**   | The live environment used by end-users.                                                                  | Managed       | Release Pipeline (with manual approval gates)    |

---

## 3. Source Code Management

*   **Repository:** A single Git repository in Azure Repos will be the source of truth for all project assets.
*   **Branching Strategy:** A GitFlow-like branching model will be used:
    *   `main`: Represents the production-ready code. Only release branches are merged here.
    *   `develop`: The main integration branch for all features. The nightly build runs against this branch.
    *   `feature/` branches: Developers create these from `develop` for new work. Merged back into `develop` via Pull Requests.
    *   `release/` branches: Created from `develop` to prepare for a production release. Used for final testing and bug fixes.

### Repository Structure:

```
/
├── solutions/
│   └── AccessManagementSystem/  # Power Platform Solution Packager source folder
│       ├── solution.xml
│       └── ... (other solution components)
├── plugins/
│   └── AccessManagement.Plugins.sln # .NET Solution for custom plugins/workflows
├── data/
│   ├── configuration_data.xml   # Configuration Migration Tool data
│   └── data_schema.xml          # Schema for configuration data
└── pipelines/
    ├── ams-ci-pipeline.yml      # Azure DevOps CI Pipeline definition
    └── ams-cd-pipeline.yml      # Azure DevOps CD Pipeline definition
```

---

## 4. Build Process (Continuous Integration - CI)

The CI pipeline automates the process of validating the solution and creating a deployable artifact. It is triggered on every push to the `develop` and `release/` branches.

**Pipeline Name:** `AMS-CI-Build`
**Agent:** Windows-latest

### Steps:

1.  **Get Sources:**
    *   Checkout the code from the Git repository.

2.  **Install Tools:**
    *   Install the Power Platform CLI using a script or a dedicated pipeline task.
    *   Use the .NET Tool Installer task to install the required .NET SDK version.
    *   Restore NuGet packages for the .NET plugin solution.

3.  **Version Stamping (Optional but Recommended):**
    *   Update the solution version number in `solution.xml` based on the build number (e.g., `1.0.$(Build.BuildId)`). This ensures each build has a unique solution version.

4.  **Build Plugin Assembly:**
    *   Build the .NET solution (`AccessManagement.Plugins.sln`) in `Release` mode.
    *   Run any unit tests associated with the plugin code and fail the build if tests fail.

5.  **Pack the Power Platform Solution:**
    *   Use the Power Platform CLI to pack the source files from the `/solutions/AccessManagementSystem/` directory into an **unmanaged** solution zip file (`AccessManagementSystem_unmanaged.zip`).

6.  **Publish Build Artifacts:**
    *   Publish the following files to be used by the release pipeline:
        *   `AccessManagementSystem_unmanaged.zip`
        *   The compiled plugin assembly (`.dll`)
        *   The configuration data files (`/data/`)
    *   The artifact will be named `AMS_Solution_Package`.

---

## 5. Deployment Process (Continuous Deployment - CD)

The CD pipeline automates the deployment of the solution to the various environments. It is triggered upon the successful completion of the CI pipeline.

**Pipeline Name:** `AMS-CD-Release`

### Stage 1: Deploy to Build Environment

This stage is fully automated and creates the official **managed** solution artifact.

1.  **Download Artifacts:**
    *   Download the `AMS_Solution_Package` artifact from the CI build.

2.  **Import Unmanaged Solution to Build Environment:**
    *   Use the Power Platform CLI to import the `AccessManagementSystem_unmanaged.zip` into the **Build** Dataverse environment.
    *   The import should overwrite customizations to ensure the environment is a clean reflection of the source code.

3.  **Publish All Customizations:**
    *   Run a "Publish All" command to ensure all solution components are activated.

4.  **Export as Managed Solution:**
    *   Use the Power Platform CLI to export the solution from the **Build** environment as a **managed** solution (`AccessManagementSystem_managed.zip`).

5.  **Publish Managed Solution Artifact:**
    *   Publish the `AccessManagementSystem_managed.zip` as a new pipeline artifact. This is the "golden copy" that will be deployed to all subsequent environments.

### Stage 2: Deploy to UAT Environment

This stage is triggered after the Build stage succeeds. A pre-deployment approval can be configured to control when releases go to UAT.

1.  **Approval Gate (Optional):**
    *   Wait for a project manager or QA lead to approve the deployment.

2.  **Download Managed Artifact:**
    *   Download the managed solution artifact created in the previous stage.

3.  **Deploy Managed Solution to UAT:**
    *   Use the Power Platform CLI to import `AccessManagementSystem_managed.zip` into the **UAT** environment.
    *   Enable the "Publish Workflows" (for classic workflows) and "Activate Plugins" options during the import.

4.  **Deploy Configuration Data:**
    *   Use the Configuration Migration Tool (via a PowerShell script and the Power Platform CLI) to import the data from the `/data/` folder into UAT.

5.  **Run Post-Deployment Steps:**
    *   Activate any Power Automate flows that are not automatically enabled by the solution import. This can be done via scripts using the Power Platform CLI.

6.  **Send Notification:**
    *   Notify the QA team via email or a Teams message that a new version is ready for testing in UAT.

### Stage 3: Deploy to Production Environment

This stage should always have a manual approval gate to ensure maximum control over production releases.

1.  **Approval Gate (Required):**
    *   Wait for a formal approval from business stakeholders and the project manager.

2.  **Download Managed Artifact:**
    *   Download the same managed solution artifact that was deployed to UAT.

3.  **Deploy Managed Solution to Production:**
    *   Use the Power Platform CLI to import `AccessManagementSystem_managed.zip` into the **Production** environment.

4.  **Deploy Configuration Data:**
    *   Use the Configuration Migration Tool to import the configuration data.

5.  **Run Post-Deployment Steps:**
    *   Activate any required Power Automate flows.

6.  **Send Notification:**
    *   Notify stakeholders that the new version has been successfully deployed to production.

---

## 6. Tools & Technologies

*   **Source Control:** Azure Repos (Git)
*   **CI/CD Platform:** Azure DevOps Pipelines
*   **Core Tooling:**
    *   **Power Platform CLI:** The primary tool for interacting with Dataverse environments (solution pack/unpack, import/export, data migration).
    *   **Power Platform Build Tools for Azure DevOps:** A marketplace extension that provides convenient tasks for the CLI commands.
    *   **.NET SDK:** For building and testing custom plugin code.
*   **Development Tools:**
    *   Visual Studio 2022 (for plugin development)
    *   VS Code (for pipeline YAML and web resources)
