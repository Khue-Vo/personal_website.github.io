---
title: "GreenStep Sustainability Challenge Administrative Platform"
pub_date: "2026-05-20"
summary: "A centralized digital hub for the Minnesota Pollution Control Agency that unifies fragmented spreadsheets into a secure platform with three-tier role access, interactive data visualizations, and one-click CSV report exports."
tags: ["Centralized Digital Platform", "System Architecture", "Role-Based Access Control", "Soft-Delete History", "Data Visualization", "CSV Export"]
---
![GreenStepChallenge](../image/GreenStepChallenge.png)
### Situation
Managing state-wide environmental campaigns for the Minnesota Pollution Control Agency was severely hindered because tracking participant engagement data was fragmented across disconnected spreadsheets, making reporting highly time-intensive for program managers

### Obstacle
The platform needed to unify multi-category tracking while maintaining strict security constraints. Sensitive operational controls had to be protected, and deleting records could not risk destroying historical compliance data needed for executive rollups

### Action
Serving as the Lead Fullstack Developer, I architected a centralized digital platform. I structured a robust system architecture featuring three distinct role tiers—SuperAdmin, Admin, and GeneralUser—to enforce strict role-based access control, ensuring only the highest tier could manage user creation. To preserve system history, I engineered a soft-delete constraint instead of permanent truncation. I integrated interactive data visualization charts into the dashboard for performance trend comparisons, and built a single-focus, one-click CSV export module with clean headers for leadership reporting

### Result
This solution completely replaced fragmented tracking with a single secure hub. It eliminated hours of manual data rollups for the program manager and provided real-time leadership statistics, directly solving the operational tracking problem to support environmental sustainability for the common good