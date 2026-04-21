# Taiwan Hot Stocks Scraper - Project Workflow Diagram

## System Architecture Flowchart

```mermaid
graph TD
    A[User Start Application] --> B{Choose Interface}
    B -->|CLI| C[Run main.py]
    B -->|GUI| D[Run app.py Streamlit]
    
    C --> E[Initialize WebScraper]
    D --> E
    
    E --> F[Setup Logging & Session]
    F --> G[Scrape Taiwan Hot Stocks]
    
    G --> H[Loop Through Stock List]
    H --> I[Request Yahoo Finance]
    I --> J[Parse HTML Data]
    J --> K[Extract Stock Info]
    K --> L{More Stocks?}
    L -->|Yes| H
    L -->|No| M[Process Complete Data]
    
    M --> N[Display Results]
    N --> O[Save to CSV]
    O --> P[Save to JSON]
    P --> Q[Close Session]
    Q --> R[End Application]
    
    subgraph "Stock Data Extraction"
        K --> K1[Company Name]
        K --> K2[Current Price]
        K --> K3[Price Change]
        K --> K4[Volume]
        K --> K5[Market Cap]
    end
    
    subgraph "GUI Features"
        D --> D1[Stock Cards Display]
        D --> D2[Interactive Charts]
        D --> D3[Metrics Dashboard]
        D --> D4[Data Table]
        D --> D5[Download CSV]
    end
```

## Data Flow Process

```mermaid
flowchart LR
    A[Yahoo Finance] --> B[HTTP Request]
    B --> C[HTML Response]
    C --> D[BeautifulSoup Parser]
    D --> E[Data Extraction]
    E --> F[Structured Data]
    F --> G[Display/Storage]
    
    subgraph "Data Processing"
        E --> E1[Price Parsing]
        E --> E2[Volume Parsing]
        E --> E3[Change Calculation]
    end
    
    subgraph "Output Formats"
        G --> G1[Console Output]
        G --> G2[CSV File]
        G --> G3[JSON File]
        G --> G4[Web Dashboard]
    end
```

## Component Interaction Diagram

```mermaid
graph TB
    subgraph "Core Components"
        A[main.py] --> B[WebScraper Class]
        B --> C[HTTP Handler]
        B --> D[HTML Parser]
        B --> E[Data Processor]
    end
    
    subgraph "GUI Components"
        F[app.py] --> G[Streamlit Interface]
        G --> H[Chart Components]
        G --> I[Display Components]
    end
    
    subgraph "Data Sources"
        J[Yahoo Finance API] --> C
        K[Stock List] --> B
    end
    
    subgraph "Output Storage"
        E --> L[CSV Files]
        E --> M[JSON Files]
        E --> N[Log Files]
    end
    
    F --> B
    A --> B
```

## User Interaction Flow

```mermaid
journey
    title Taiwan Hot Stocks Scraper User Journey
    section CLI Mode
      Start Application: 5: User
      Run main.py: 4: User
      View Console Output: 5: User
      Check CSV Files: 4: User
    section GUI Mode
      Start Streamlit: 4: User
      Open Browser: 5: User
      View Dashboard: 5: User
      Interact with Charts: 5: User
      Download Data: 4: User
    section Data Analysis
      Review Stock Data: 5: User
      Analyze Trends: 4: User
      Export Results: 4: User
```

## Error Handling Flow

```mermaid
graph TD
    A[Request Stock Data] --> B{Success?}
    B -->|Yes| C[Extract Data]
    B -->|No| D[Log Error]
    D --> E{Retry?}
    E -->|Yes| F[Wait 2s]
    F --> A
    E -->|No| G[Skip Stock]
    G --> H{More Stocks?}
    H -->|Yes| I[Next Stock]
    H -->|No| J[Complete]
    
    C --> K{Data Valid?}
    K -->|Yes| L[Add to Results]
    K -->|No| M[Log Warning]
    M --> H
    
    L --> H
    I --> A
    J --> N[Generate Output]
```

## Deployment Architecture

```mermaid
graph TB
    subgraph "Development Environment"
        A[Local Machine] --> B[Python 3.13]
        B --> C[Virtual Environment]
        C --> D[Dependencies]
    end
    
    subgraph "Application Layer"
        E[CLI Interface] --> F[WebScraper Engine]
        G[GUI Interface] --> F
        F --> H[Data Processing]
    end
    
    subgraph "External Services"
        I[Yahoo Finance] --> F
        J[Internet Connection] --> I
    end
    
    subgraph "Storage Layer"
        H --> K[Local File System]
        K --> L[Data Directory]
        K --> M[Logs Directory]
    end
    
    A --> E
    A --> G
```
