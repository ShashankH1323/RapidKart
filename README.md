# RapidKart: Quick-Commerce Funnel Optimization

> **Product Analytics deep-dive into on-demand delivery checkout flows, eliminating UX friction to drive conversion and retention.**

---

## 🚀 Overview
In the highly competitive quick-commerce space, cart abandonment is the primary barrier to profitability. This project analyzes event-stream data to map the user journey and pinpoint exactly where and why users fail to complete their orders.

## 📈 Key Product Metrics & Business Impact
* **The Problem:** The app was experiencing low checkout conversion despite high initial cart-add rates.
* **The Data Discovery:** By constructing a strict conversion funnel from raw event streams, we identified a massive **35% drop-off** occurring specifically at the payment selection screen due to confusing and redundant UI logic.
* **The Solution & Impact:** Spearheaded a UX redesign to simplify the checkout flow and remove redundant confirmation steps. Post-launch analytics showed a **20% increase** in checkout completions and a downstream **15% bump** in Daily Active User (DAU) retention.

## 🧰 Tools & Skills
* **SQL:** Advanced funnel analysis utilizing Window Functions (`LEAD`, `LAG`) to track strict sequential event progression.
* **Python (Pandas, Plotly):** Funnel visualization and statistical validation of the UI change impact.
* **Product Strategy:** UX optimization, conversion rate optimization (CRO), user journey mapping.

## 📂 Repository Structure
* `queries.sql`: SQL scripts used to generate the funnel drop-off metrics.
* `analysis.py`: Python script to parse the funnel data and calculate the drop-off percentages.
* `data/`: Mock event-stream dataset for the checkout funnel.
