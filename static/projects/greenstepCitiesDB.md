---
title: "GreenStep Cities - Database Design"
pub_date: "2026-05-20"
summary: "A high-performance MySQL database built to optimize municipal efficiency metrics, utilizing strict 3NF schema normalization and surrogate keys to eliminate redundancies and accelerate analyst query speeds."
tags: ["Database Design", "Schema Normalization", "Relational Database", "Query Optimization", "Provenance Tracking", "MySQL"]
---
![GreenStepCities](../image/GreenStepCities.png)
### Description
For this system project, I collaborated to architect a high-performance relational database in MySQL designed to optimize how GreenStep Cities inputs, tracks, and audits sustainability metrics across various municipal programs. The primary goal was to eliminate data redundancy and enhance retrieval speed across massive data arrays submitted by multiple city contributors. My personal contribution focused on the execution of strict schema normalization up to the Third Normal Form (3NF). I introduced a surrogate key (CityID) system to eliminate duplicate name conflicts and accelerate multi-table joins, and designed custom query mapping to handle validation workflows and action reports. Additionally, I added attributes for user role tables and data provenance tracking, enabling program analysts to easily verify data quality and audit report submissions. This project established a clean, optimized backend infrastructure that empowered analysts to quickly extract the insights needed to measure urban efficiency benchmarks