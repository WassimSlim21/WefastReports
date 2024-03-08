# WEFAST FORMULA1 ANALYSIS

## Project Overview:
WEFAST FORMULA1 ANALYSIS is an optimized decision support system designed for Formula 1 teams. It streamlines data collection from 15+ sources, enhancing data accessibility and efficiency.

## Key Features:
- Utilization of Talend and PostgreSQL for ETL processes, significantly improving data processing time and enabling real-time data analysis.
- Implementation of machine learning models achieving 95% accuracy in categorizing Formula 1 qualifications and win rates, providing actionable insights for strategic decision-making.

## Repository Contents:

### 1. Formula1DataIntegration:
- **Description:** Talend project containing the Data Integration of various dimensions.
- **Job Folders:**
  - Circuit Dimension
  - Constructor Dimension
  - Drivers Dimension
  - LapTimes Dimension
  - Qualifying Dimension
  - PitStops Dimension
  - Race_Circuits Dimension
  - Races Dimension
  - Status Dimension
- **External Data Extract:**
  - Seasons: Extract using Ergast API F1
  - Drivers External Data: Extract using Ergast API F
- **Fact Tables:**
  - Driver_Standing Fact Table
  - Qualifying Fact Table
  - Result Fact Tables
- **Data Integration JOB:** Integration of all dimensions within the fact tables, building a constellation Data Warehouse model.

### 2. Reports:
- **Description:** Power BI reports, including Python analysis.

### 3. apiF1:
- **Description:** Backend web application API using NodeJS, ExpressJS, and PostgreSQL.

### 4. wefastfront:
- **Description:** Angular dynamic web application utilizing Lazy Loading Modules architecture. Allows users to connect, add comments on reports, and consume the API from apiF1.

## Getting Started:
1. Clone the repository to your local machine.
2. Navigate to each subdirectory for specific setup and usage instructions.

## Requirements:
- Talend
- PostgreSQL
- Power BI
- Python
- NodeJS
- ExpressJS
- Angular

## Usage:
1. Configure Talend jobs for data integration.
2. Set up PostgreSQL database for storage and retrieval.
3. Run Power BI reports for data visualization and analysis.
4. Start the apiF1 backend for web application functionality.
5. Launch the wefastfront web application for user interaction.

## Acknowledgments:
- Special thanks to the Formula 1 community and Ergast API for providing valuable data sources.

### Video Demo

To watch the video demo, please visit the following LinkedIn post:
[View Video Demo](https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:6946510288301010944)
