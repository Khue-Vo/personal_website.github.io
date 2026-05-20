---
title: "Personal Vehicle Management Website"
pub_date: "2026-05-20"
summary: "A comprehensive website using HTML, CSS, JS and RESTful API built with Express.js and MongoDB to help vehicle owners log repairs, track maintenance history, and monitor expenses over time."
tags: ["RESTful API", "Express.js", "MongoDB", "JWT Authentication", "Route Protection", "Front-End"]
---
![PersonalVehicleManagement](../image/PersonalVehicleManagement.png)
### Situation
Maintaining vehicle longevity and safety metrics is highly difficult for owners when repair receipts, mileage logs, and expense tracking histories are scattered across disjointed physical and digital spaces.

### Obstacle
Building a centralized digital management system required handling high-throughput operations securely, ensuring that users could only access, modify, or view their own private vehicle data sheets without exposing endpoints to malicious exploits.

### Action
As the Lead Fullstack Developer, I designed and implemented a comprehensive RESTful API built on an Express.js server. I configured the backend architecture using MongoDB and Mongoose for advanced database object modeling, establishing clean schema validation and relational references linking user profiles to maintenance entries. I implemented full CRUD operations for service records, including complex sorting by model year and history pagination. Most importantly, I engineered secure route protection by implementing JSON Web Token (JWT) authentication middleware to safeguard the request pipeline

### Result
The final product delivered a highly secure backend system ensuring absolute data integrity. By translating scattered records into a保護 (protected), structured digital repository, this project successfully gave users transparent access and control over their vehicle health analytics