# Building AMS Agents with Microsoft Copilot Studio

This document provides a high-level guide for creating the specialized AI agents for the Access Management System (AMS) using **Microsoft Copilot Studio**.

---

## 1. Introduction

Microsoft Copilot Studio is the recommended low-code platform for building, deploying, and managing the AI agents (Copilots) defined in the `AMS_ARCHITECTURE.MD` document. It provides a graphical interface that integrates seamlessly with the rest of the Power Platform, including Power Automate and Dataverse, making it the ideal tool for this project.

The "Copilot Agent Layer" in the architecture will be realized by creating a distinct Copilot in the Studio for each specialized agent persona (Requestor, Approver, Admin). These Copilots can then be embedded directly into the Model-Driven App.

## 2. Core Concepts in Copilot Studio

To build the AMS agents, you will primarily use the following features in Copilot Studio:

*   **Topics:** These are the discrete conversation paths that a Copilot can handle. For example, the Requestor Agent would have a "Request New Access" topic. Each topic is triggered by a set of user-defined phrases.
*   **Entities:** These represent specific pieces of information you want to extract from a user's conversation, such as an application name, a date, or a justification. You can create custom entities for AMS-specific information.
*   **Actions:** These allow your Copilot to connect to external systems and perform tasks. For AMS, this will almost always involve calling a **Power Automate Flow** to interact with the Dataverse database (e.g., to create an access request or retrieve its status).
*   **Generative AI:** Copilot Studio includes generative AI capabilities that can be used to generate responses, summarize information from a data source (like a request record in Dataverse), or handle conversation turns more dynamically.

## 3. Step-by-Step Guide: Creating the Requestor Agent

This walkthrough outlines the process for building the **Requestor Agent**.

### Step 1: Create a New Copilot

1.  Navigate to the [Copilot Studio portal](https://copilotstudio.microsoft.com/).
2.  Create a new Copilot and name it "AMS Requestor Assistant".
3.  Ensure it is created in the correct Power Platform environment for the AMS project.

### Step 2: Create a "Request New Access" Topic

1.  Inside your new Copilot, go to the **Topics** section.
2.  Create a new topic and name it `Request New Access`.
3.  Define a set of **trigger phrases** that a user might say to start this conversation, such as:
    *   "I need new access"
    *   "Request a new role"
    *   "Can I get access to an app?"

### Step 3: Gather Information from the User

1.  In the topic's authoring canvas, add **Question** nodes to gather the necessary information from the user.
2.  For each question, identify the information you need to collect using **Entities**. For example:
    *   "Which application do you need access to?" (Identify: `ApplicationName` - you may need to create a custom entity for this).
    *   "What role do you require?" (Identify: `RoleName` - another custom entity).
    *   "Please provide a business justification." (Identify: `Justification` - use a multi-line text entity).

### Step 4: Call a Power Automate Flow (Action)

1.  After gathering the information, add a new node and select **Call an action**.
2.  Choose "Create a new action" to open Power Automate.
3.  Design a new Flow that accepts the `ApplicationName`, `RoleName`, and `Justification` as input parameters.
4.  Inside the Flow, use the **Dataverse** connector to create a new "Access Request" record, populating the fields with the inputs from the Copilot.
5.  The Flow can return the ID or status of the newly created request back to the Copilot.

### Step 5: Confirm with the User

1.  Back in Copilot Studio, add a **Message** node after the action.
2.  Use the output from the Flow to confirm to the user that their request has been submitted. For example: "Thank you! Your access request has been submitted with ID: [Request ID]. You will be notified once it is approved."
3.  End the conversation with a survey or a simple "Goodbye".

### Step 6: Test and Publish

1.  Use the built-in test pane in Copilot Studio to test the entire conversation flow.
2.  Once you are satisfied, **Publish** the Copilot to make it available.

## 4. Implementing Other Agents

The same principles apply to the other agents:

*   **Approver Agent:**
    *   **Topics:** "Summarize Request", "Approve Request", "Reject Request".
    *   **Actions:** Would call Power Automate Flows that query Dataverse for request details based on an ID, and then update the record with an approval or rejection status. Generative AI actions could be used here to summarize the request details for the manager.
*   **Admin Agent:**
    *   **Topics:** "Check User Access", "Troubleshoot Request", "Get Audit History".
    *   **Actions:** Would call more complex Power Automate Flows designed for administrative tasks, such as querying user permissions or the audit logs in Dataverse.

## 5. Integration with the Model-Driven App

Once published, your Copilots can be integrated into the AMS Model-Driven App. You can add a **Copilot component** to the app's main form, providing users with an always-on assistant that is context-aware and ready to help them perform their tasks.
