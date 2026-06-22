# 🛰️ ASTRAEUS

## AI-Driven Multi-Modal Aerial Swarm Surveillance and Situational Awareness Platform

ASTRAEUS (Advanced Surveillance, Threat Recognition, Analysis, and Unified Situational Awareness System) is an intelligent defense-oriented surveillance framework designed to detect, analyze, characterize, and assess aerial drone swarms using multi-modal sensor fusion.

The platform integrates camera intelligence, synthetic radar intelligence, sensor fusion, swarm analysis, threat prediction, interceptor assignment, and executive decision support into a unified command dashboard.

---

# 📌 Project Overview

Modern UAV swarms pose significant challenges to traditional surveillance systems. Individual sensors often provide incomplete situational awareness.

ASTRAEUS addresses this challenge by combining information from multiple sensing modalities to generate actionable intelligence.

The system performs:

* Aerial target monitoring
* Sensor fusion
* Threat characterization
* Swarm formation recognition
* Behaviour analysis
* Intent assessment
* Threat escalation prediction
* Sector intelligence generation
* Interceptor assignment
* Executive command dashboard generation

---

# 🎯 Objectives

* Detect and monitor aerial targets
* Simulate radar observations
* Fuse camera and radar intelligence
* Generate unified target tracks
* Analyze swarm formations
* Recognize swarm behaviours
* Assess operational intent
* Predict threat escalation
* Recommend interceptor assignments
* Provide executive-level situational awareness

---

# 🏗️ System Architecture

```text
VisDrone Dataset
        ↓
Dataset Validation
        ↓
Image Intelligence Layer
        ↓
Synthetic Radar Generation
        ↓
Radar Intelligence Layer
        ↓
Camera-Radar Sensor Fusion
        ↓
Threat Characterization
        ↓
Situational Awareness
        ↓
Formation Recognition
        ↓
Behaviour Analysis
        ↓
Intent Assessment
        ↓
Threat Prediction
        ↓
Sector Intelligence
        ↓
Interceptor Assignment
        ↓
Executive Intelligence
        ↓
ASTRAEUS Command Dashboard
```

---

# 📂 Dataset

## Primary Dataset

### VisDrone 2019 Detection Dataset

The project utilizes the VisDrone benchmark dataset containing aerial imagery captured by unmanned aerial vehicles.

Dataset Characteristics:

* High-resolution drone imagery
* Multiple object classes
* Real-world urban environments
* Diverse viewpoints
* Dense target distributions

Classes Used:

* Pedestrian
* People
* Bicycle
* Car
* Van
* Truck
* Tricycle
* Awning-Tricycle
* Bus
* Motor

---

# ⚙️ Technology Stack

## Programming Language

* Python

## Data Processing

* Pandas
* NumPy

## Visualization

* Matplotlib
* Streamlit

## Computer Vision

* OpenCV
* YOLO Framework

## Machine Learning

* Scikit-Learn

---

# 🚀 Core Modules

## 1. Dataset Validation Module

Functions:

* Dataset inspection
* Image verification
* Annotation validation
* Dataset statistics generation

Outputs:

* Image counts
* Annotation counts
* Dataset quality reports

---

## 2. Synthetic Swarm Generation Module

Generates:

* Drone IDs
* Coordinates
* Altitudes
* Threat levels

Outputs:

* Synthetic swarm dataset

---

## 3. Synthetic Radar Generation Module

Generates:

* Radar range
* Bearing
* Velocity
* Altitude

Outputs:

* Synthetic radar tracks

---

## 4. Sensor Fusion Engine

Combines:

* Camera observations
* Radar observations

Outputs:

* Unified target tracks
* Confidence values
* Threat indicators

---

## 5. Threat Intelligence Module

Calculates:

* Threat score
* Threat category
* Priority level
* Recommended actions

Threat Categories:

* Low
* Medium
* High
* Critical

---

## 6. Situational Awareness Module

Generates:

* Sector-wise threat distribution
* Alert levels
* Operational summaries

Alert Levels:

* GREEN
* AMBER
* RED

---

## 7. Formation Recognition Module

Recognizes:

* Circular Formation
* Linear Formation
* V Formation
* Cluster Formation

Current Detection:

```text
Circular Formation
```

---

## 8. Behaviour Analysis Module

Identifies:

* Reconnaissance
* Surveillance
* Approach
* Attack Preparation

Current Detection:

```text
Reconnaissance
```

---

## 9. Intent Assessment Module

Determines:

* Information Gathering
* Monitoring
* Surveillance
* Potential Threat

Current Intent:

```text
Information Gathering
```

---

## 10. Threat Escalation Prediction Module

Predicts:

* Threat growth
* Escalation level
* Early warning status

Current Output:

```text
Escalation Level : MEDIUM
Warning Status   : AMBER ALERT
Threat Growth    : 52.85%
```

---

## 11. Interceptor Assignment Engine

Assigns:

* Available assets
* Target priorities
* Engagement readiness

Outputs:

```text
ASSET_01 → TRK_002
ASSET_02 → TRK_019
ASSET_03 → TRK_020
ASSET_04 → TRK_001
ASSET_05 → TRK_014
```

---

# 📊 Generated Reports

The system automatically generates:

* Mission Summary
* Threat Overview
* Sector Dashboard
* Asset Status Report
* Executive Summary
* Formation Report
* Behaviour Report
* Prediction Report
* Situational Awareness Report
* Sensor Fusion Dataset

---

# 🖥️ ASTRAEUS Command Dashboard

The project includes an interactive Streamlit-based command dashboard.

Dashboard Features:

## Executive Command Center

* Mission Health
* Warning Status
* Readiness Score
* Operational Intent
* Formation Type
* Behaviour Type

## Threat Intelligence

* Threat Overview
* Threat Categorization
* Priority Assessment

## Sensor Fusion View

* Unified Target Tracks
* Confidence Scores
* Radar-Camera Correlation

## Situational Awareness

* Sector Threat Scores
* Alert Levels

## Mission Control

* Operational Summaries
* Command Briefings

## Asset Assignment

* Interceptor Status
* Target Allocation

---

# 📈 Key Outputs

Current System Results:

```text
Total Targets        : 20
High Threat Targets  : 1
Critical Sector      : Sector_C

Formation            : Circular Formation
Behaviour            : Reconnaissance
Intent               : Information Gathering

Escalation Level     : MEDIUM
Warning Status       : AMBER ALERT

Readiness Score      : 95%
```

---

# 📁 Project Structure

```text
ASTRAEUS
│
├── app.py
├── README.md
├── requirements.txt
│
├── data
│   ├── mission_summary.csv
│   ├── threat_overview.csv
│   ├── sector_dashboard.csv
│   ├── asset_status.csv
│   ├── executive_summary.csv
│   ├── sensor_fusion_dataset.csv
│   ├── situational_awareness.csv
│   ├── prediction_report.csv
│   ├── formation_report.csv
│   └── behaviour_report.csv
│
├── assets
├── screenshots
└── docs
```

---

# 🔮 Future Enhancements

Planned Upgrades:

* Real-Time Drone Detection
* Live Video Analytics
* Webcam Integration
* RTSP Feed Support
* YOLO-Based UAV Detection
* Multi-Object Tracking
* Kalman Filter Prediction
* Live Coordinate Estimation
* Real-Time Sensor Fusion
* Interactive Threat Map
* Automated Mission Reports

---

# 👨‍💻 Author

**Apoorv Srivastava**

B.Tech Computer Science & Engineering (AI & ML)

United College of Engineering and Research, Prayagraj

Dr. A.P.J. Abdul Kalam Technical University (AKTU)

---

# 📜 License

This project is intended for educational, research, and academic demonstration purposes.
