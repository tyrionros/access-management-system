# Power Automate Expressions for Access Management Systems

This document provides a collection of common and useful Power Automate expressions tailored for building an Access Management System on top of Microsoft Dataverse and Dynamics 365.

---

## 1. User and Approval Expressions

These expressions are fundamental for creating dynamic approval workflows.

### 1.1 Get the Requestor's Manager

Used in the "Start and wait for an approval" action to dynamically assign the approval to the user who submitted the request's manager.

**Scenario:** An access request needs to be approved by the requestor's line manager.

**Expression:**
```powerautomate
outputs('Get_a_row_by_ID')?['body/_manager_value']
```
**Explanation:**
This assumes you have a "Get a row by ID" action earlier in your flow that retrieves the record of the user who created the access request. The `_manager_value` is the lookup field on the User table that points to their manager.

### 1.2 Get the Current User's Email

Useful for stamping who performed a certain action or for sending notifications.

**Scenario:** You need to record the email of the user who manually triggered a flow.

**Expression:**
```powerautomate
triggerOutputs()?['body/user/email']
```
**or for a Dataverse connector trigger:**
```powerautomate
triggerOutputs()?['body/_ownerid_value']
```
**Explanation:**
The `triggerOutputs()` function retrieves information about the trigger condition. The exact path depends on the trigger type. For a "Manually trigger a flow", you can get user properties directly. For a Dataverse trigger (e.g., "When a row is added, modified or deleted"), the `_ownerid_value` often holds the GUID of the user who initiated the action.

### 1.3 Check if a User has a Specific Security Role

Used in a Condition control to determine the workflow path based on the user's permissions.

**Scenario:** If a user is a "System Administrator," auto-approve their request.

**Expression:**
(This is more complex and typically involves a `List rows` action first)
1.  **Action:** `List rows` on the "User Roles" table.
2.  **Filter Rows:** `_parentroleid_value eq 'GUID_OF_SECURITY_ROLE' and _systemuserid_value eq '@{triggerOutputs()?['body/_ownerid_value']}'`
3.  **Condition Expression:** Use the output of the `List rows` action.
```powerautomate
empty(outputs('List_User_Roles')?['body/value'])
```
**Explanation:**
You first try to find an entry in the "User Roles" table that links the user and the specific security role. The expression in the condition checks if the result of that query is empty. If `empty()` is `false`, it means a record was found, and the user has the role.

---

## 2. Dataverse and FetchXML Expressions

For querying and interacting with your data.

### 2.1 Get a Value from a Lookup Field

Retrieves a formatted value (like the Name) from a related table.

**Scenario:** In an email notification, you want to include the name of the Application the user is requesting access to, not just its GUID.

**Expression:**
```powerautomate
outputs('Get_access_request_record')?['body/_cr123_application_value@OData.Community.Display.V1.FormattedValue']
```
**Explanation:**
When you retrieve a record with a lookup field (e.g., `_cr123_application_value`), Dataverse also provides a special annotation (`@OData.Community.Display.V1.FormattedValue`) that contains the user-friendly display name of the looked-up record.

### 2.2 Constructing a FetchXML Query Dynamically

Used to build more complex queries than are possible with standard OData filters.

**Scenario:** Find all active access requests for a specific application that were submitted in the last 7 days.

**Expression (in a `List rows` action with FetchXML):**
```xml
<fetch>
  <entity name="cr123_accessrequest">
    <attribute name="cr123_requestname" />
    <attribute name="createdon" />
    <filter type="and">
      <condition attribute="statecode" operator="eq" value="0" />
      <condition attribute="_cr123_application_value" operator="eq" value="@{variables('ApplicationId')}" />
      <condition attribute="createdon" operator="last-x-days" value="7" />
    </filter>
  </entity>
</fetch>
```
**Explanation:**
You can insert dynamic content (like variables or outputs from previous steps) directly into the FetchXML query. In this case, `@{variables('ApplicationId')}` would be replaced with the GUID of the application you are querying for.

---

## 3. String and Date Manipulation Expressions

For formatting data and handling logic.

### 3.1 Formatting a Date for Email Notifications

Converts a standard UTC date into a more readable format.

**Scenario:** Display the request submission date in an approval email.

**Expression:**
```powerautomate
formatDateTime(triggerOutputs()?['body/createdon'], 'MM/dd/yyyy hh:mm tt')
```
**Explanation:**
The `formatDateTime()` function takes a date string and a format string as input. This example would format "2025-11-28T10:30:00Z" into "11/28/2025 10:30 AM". You may need to use `convertTimeZone` first if you need to display it in a specific user's time zone.

### 3.2 Calculating an SLA Deadline

Calculates a date in the future for a Service Level Agreement (SLA).

**Scenario:** An access request must be approved within 3 business days.

**Expression:**
```powerautomate
addDays(utcNow(), 3)
```
**Explanation:**
The `addDays()` function adds a specified number of days to a given date. `utcNow()` provides the current date and time. *Note: This is a simple calculation. For true business day calculations, you would need a more complex expression or a custom connector that accounts for weekends and holidays.*

### 3.3 Creating a URL to the Model-Driven App Record

Builds a direct link to the access request record for an approver to easily open it.

**Scenario:** Include a "View Request" link in the approval email.

**Expression:**
```powerautomate
concat('https://[YourOrg].crm.dynamics.com/main.aspx?appid=[YourAppId]&pagetype=entityrecord&etn=cr123_accessrequest&id=', triggerOutputs()?['body/cr123_accessrequestid'])
```
**Explanation:**
The `concat()` function joins several strings together. You need to replace:
*   `[YourOrg]` with your Dynamics 365 organization URL.
*   `[YourAppId]` with the GUID of your Model-Driven App.
The expression then appends the unique ID of the access request record from the trigger.

### 3.4 Conditional Expressions with `if`

Used to set a value based on a condition, often for setting fields in a record.

**Scenario:** If the request is for the "Finance" application, set the priority to "High". Otherwise, set it to "Normal".

**Expression:**
```powerautomate
if(equals(outputs('Get_access_request_record')?['body/_cr123_application_value@OData.Community.Display.V1.FormattedValue'], 'Finance'), 'High', 'Normal')
```
**Explanation:**
The `if(condition, value_if_true, value_if_false)` function is used. Here, it checks if the application's formatted name is "Finance". If it is, it returns 'High'; otherwise, it returns 'Normal'. This can be used directly in a field of an "Update a row" action.
