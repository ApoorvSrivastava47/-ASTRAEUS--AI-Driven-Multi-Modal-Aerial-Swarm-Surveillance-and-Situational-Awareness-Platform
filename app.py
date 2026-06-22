import streamlit as st
import pandas as pd

st.set_page_config(page_title="ASTRAEUS", page_icon="🛰️", layout="wide")

# LOAD DATA

mission_summary = pd.read_csv("data/mission_summary.csv")

threat_overview = pd.read_csv("data/threat_overview.csv")

sector_dashboard = pd.read_csv("data/sector_dashboard.csv")

asset_status = pd.read_csv("data/asset_status.csv")

executive_summary = pd.read_csv("data/executive_summary.csv")

sensor_fusion = pd.read_csv("data/sensor_fusion_dataset.csv")

situational_awareness = pd.read_csv("data/situational_awareness.csv")

prediction_report = pd.read_csv("data/prediction_report.csv")

formation_report = pd.read_csv("data/formation_report.csv")

behaviour_report = pd.read_csv("data/behaviour_report.csv")

# HEADER

st.title("🛰️ ASTRAEUS")

st.subheader(
    "Multi-Modal Sensor Fusion Framework for UAV Swarm Detection and Threat Characterization"
)

st.divider()

# KPI SECTION

total_targets = int(
    mission_summary.loc[mission_summary["Metric"] == "Total Targets", "Value"].iloc[0]
)

high_threat = int(
    mission_summary.loc[
        mission_summary["Metric"] == "High Threat Targets", "Value"
    ].iloc[0]
)

critical_sector = mission_summary.loc[
    mission_summary["Metric"] == "Critical Sector", "Value"
].iloc[0]

escalation_level = mission_summary.loc[
    mission_summary["Metric"] == "Escalation Level", "Value"
].iloc[0]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Targets", total_targets)

col2.metric("High Threat", high_threat)

col3.metric("Critical Sector", critical_sector)

col4.metric("Escalation", escalation_level)

# ==========================================
# EXECUTIVE COMMAND CENTER
# ==========================================

executive_dict = dict(zip(executive_summary["Parameter"], executive_summary["Value"]))

formation = executive_dict.get("Formation", "Unknown")

behaviour = executive_dict.get("Behaviour", "Unknown")

intent = executive_dict.get("Intent", "Unknown")

warning_status = executive_dict.get("Warning Status", "Unknown")

readiness_score = float(executive_dict.get("Readiness Score", 0))

mission_health = round((readiness_score + (100 - high_threat * 10)) / 2, 2)

st.subheader("Executive Command Center")

c1, c2, c3, c4, c5, c6 = st.columns(6)

c1.metric("Formation", formation)

c2.metric("Behaviour", behaviour)

c3.metric("Intent", intent)

c4.metric("Warning", warning_status)

c5.metric("Readiness", f"{readiness_score}%")

c6.metric("Mission Health", f"{mission_health}%")

if warning_status == "RED ALERT":
    st.error("CRITICAL THREAT DETECTED")

elif warning_status == "AMBER ALERT":
    st.warning("HEIGHTENED SURVEILLANCE REQUIRED")

else:
    st.success("MISSION STATUS NORMAL")

# ==========================================
# COMMANDER BRIEFING
# ==========================================

critical_sector = sector_dashboard.loc[
    sector_dashboard["Threat_Score"].idxmax(), "Sector"
]

briefing = f"""
{total_targets} aerial targets are currently
being monitored.

{high_threat} target(s) have been classified
as high threat.

{critical_sector} remains the most critical
operational zone.

Observed swarm behaviour indicates
{behaviour} activity operating in a
{formation} pattern.

Operational intent assessment suggests
{intent}.

Current warning status is
{warning_status}.
"""

st.subheader("Commander's Briefing")

st.info(briefing)


st.divider()

# TABS

tabs = st.tabs(
    [
        "Mission",
        "Threats",
        "Fusion",
        "Situational",
        "Formation",
        "Behaviour",
        "Prediction",
        "Assets",
        "Executive",
    ]
)

# MISSION TAB

with tabs[0]:
    st.header("Mission Summary")

    st.dataframe(mission_summary, use_container_width=True)

# THREATS TAB

with tabs[1]:
    st.header("Threat Overview")

    st.dataframe(threat_overview, use_container_width=True)

    if "Threat_Category" in threat_overview.columns:
        st.subheader("Threat Category Distribution")

        st.bar_chart(threat_overview["Threat_Category"].value_counts())

# SENSOR FUSION TAB

with tabs[2]:
    st.header("Sensor Fusion Dataset")

    st.dataframe(sensor_fusion, use_container_width=True)

# SITUATIONAL AWARENESS TAB

with tabs[3]:
    st.header("Situational Awareness")

    st.dataframe(situational_awareness, use_container_width=True)

    if "Threat_Score" in sector_dashboard.columns:
        st.subheader("Sector Threat Scores")

        st.bar_chart(sector_dashboard.set_index("Sector")["Threat_Score"])

# FORMATION TAB

with tabs[4]:
    st.header("Formation Recognition")

    st.dataframe(formation_report, use_container_width=True)

# BEHAVIOUR TAB

with tabs[5]:
    st.header("Behaviour Analysis")

    st.dataframe(behaviour_report, use_container_width=True)

# PREDICTION TAB

with tabs[6]:
    st.header("Threat Prediction")

    st.dataframe(prediction_report, use_container_width=True)

# ASSETS TAB

with tabs[7]:
    st.header("Interceptor Assignments")

    st.dataframe(asset_status, use_container_width=True)

# EXECUTIVE TAB

with tabs[8]:
    st.header("Executive Summary")

    st.dataframe(executive_summary, use_container_width=True)

st.divider()

st.success("ASTRAEUS Operational Dashboard Active")
