# Catalog data for the Access Management System
ROLES_CATALOG = [
    {
        "application": "D365 Core Platform",
        "role": "System Administrator",
        "description": "Has the highest level of access. Can manage all security, users, and customizations. Should be used sparingly."
    },
    {
        "application": "D365 Core Platform",
        "role": "System Customizer",
        "description": "Can customize entities, forms, views, and business processes. Cannot manage users or security roles."
    },
    {
        "application": "D365 Core Platform",
        "role": "Basic User",
        "description": "Provides standard privileges to view, create, edit, and delete records for day-to-day tasks."
    },
    {
        "application": "D365 Core Platform",
        "role": "Read-Only",
        "description": "For users who only need to view data and should not have create, update, or delete capabilities."
    },
    {
        "application": "D365 Sales",
        "role": "Salesperson",
        "description": "For sellers who work with leads, opportunities, quotes, orders, and invoices. Can manage their own sales pipeline."
    },
    {
        "application": "D365 Sales",
        "role": "Sales Manager",
        "description": "Manages a team of sellers. Can view team performance, manage sales goals, and access team members' records."
    },
    {
        "application": "D365 Sales",
        "role": "VP of Sales",
        "description": "Has a high-level view of the entire sales organization, including all territories and business units. Can override and manage sales processes."
    },
    {
        "application": "D365 Customer Service",
        "role": "Customer Service Representative",
        "description": "Manages customer cases, activities, and knowledge articles. The primary role for service agents."
    },
    {
        "application": "D365 Customer Service",
        "role": "CSR Manager",
        "description": "Manages a team of representatives. Can view team queues, dashboards, and performance metrics."
    },
    {
        "application": "D365 Customer Service",
        "role": "Omnichannel agent",
        "description": "A specialized agent role for handling real-time customer interactions across channels like chat, SMS, and social media."
    },
    {
        "application": "D365 Customer Service",
        "role": "Omnichannel supervisor",
        "description": "Monitors agent conversations, manages agent assignments, and views real-time analytics for the contact center."
    },
    {
        "application": "D365 Customer Service",
        "role": "App Profile Manager Admin",
        "description": "Manages app profiles, session templates, and productivity tools for the agent experience."
    },
    {
        "application": "D365 Field Service",
        "role": "Field Service - Resource",
        "description": "For frontline workers (technicians) who execute work orders on-site. Primarily uses the Field Service mobile app."
    },
    {
        "application": "D365 Field Service",
        "role": "Field Service - Dispatcher",
        "description": "Responsible for scheduling jobs, creating bookings, and assigning work orders to frontline workers. Manages the schedule board."
    },
    {
        "application": "D365 Field Service",
        "role": "Field Service - Administrator",
        "description": "Provides extensive permissions to all Field Service tables and settings. Intended for IT administrators and service managers."
    },
    {
        "application": "D365 Field Service",
        "role": "Field Service - Inventory Purchase",
        "description": "For inventory managers who oversee stock on service vehicles, manage purchasing, and process product returns."
    },
    {
        "application": "D365 Field Service",
        "role": "IoT - Administrator",
        "description": "Registers and manages IoT devices and configures business processes based on IoT alerts."
    },
    {
        "application": "D365 Marketing",
        "role": "Marketing Professional – Business",
        "description": "For standard marketers who create and manage customer journeys, emails, segments, and marketing pages."
    },
    {
        "application": "D365 Marketing",
        "role": "Marketing Manager – Business",
        "description": "Has broader permissions than the Professional role, including the ability to configure marketing settings."
    },
    {
        "application": "D365 Marketing",
        "role": "Event Planner",
        "description": "For users who specifically need to create, manage, and track marketing events."
    },
    {
        "application": "D365 Marketing",
        "role": "LinkedIn Lead Gen Salesperson",
        "description": "A specific role that allows users to view and manage leads generated from LinkedIn Lead Gen Forms."
    },
    {
        "application": "D365 Project Operations",
        "role": "Project Manager",
        "description": "Manages all aspects of a project, including scheduling, resource assignments, budget tracking, and approvals for time and expenses."
    },
    {
        "application": "D365 Project Operations",
        "role": "Project Accountant",
        "description": "Manages the financial aspects of projects, including invoicing, revenue recognition, and project-based accounting."
    },
    {
        "application": "D365 Project Operations",
        "role": "Practice Manager",
        "description": "Oversees a portfolio of projects, managing resource utilization, profitability, and overall practice health."
    },
    {
        "application": "D365 Project Operations",
        "role": "Resource Manager",
        "description": "Responsible for staffing projects by matching the skills and availability of consultants with project demands."
    },
    {
        "application": "D365 Project Operations",
        "role": "Team Member",
        "description": "For project consultants who need to record time and expenses, update task progress, and manage their own project work."
    }
]
