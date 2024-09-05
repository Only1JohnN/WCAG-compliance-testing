# WCAG-Compliance-Testing

Automated scripts for accessibility testing based on WCAG standards. This project demonstrates various accessibility functionalities, including color contrast ratio checks and screen reader compatibility testing, using the Page Object Model (POM). It aims to help developers ensure web content meets essential accessibility requirements for all users.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project provides automated scripts to test web applications against WCAG standards, specifically focusing on:

1. **Color Contrast**: Validates the contrast ratio between text and background colors to meet accessibility requirements.
2. **Screen Reader Compatibility**: Ensures that web elements are accessible to screen readers, enhancing the experience for visually impaired users.

## Features

- **Color Contrast Testing**: Checks if text and background colors meet WCAG contrast standards.
- **Screen Reader Testing**: Verifies screen reader accessibility of web elements.
- **POM-Based Structure**: Uses the Page Object Model (POM) design pattern for better code maintainability and scalability.

## Technologies Used

- **Python**: Programming language used for writing test scripts.
- **Selenium**: For browser automation.
- **webdriver-manager**: Automatically manages and sets up WebDriver binaries.
- **pytest**: For running the test scripts and reporting results.
- **WCAG-Contrast-Ratio**: For calculating color contrast ratios.

## Setup

### Prerequisites

1. Python 3.7 or above installed on your machine.

### Create and Activate a Virtual Environment

1. Navigate to your project directory:

   ```bash
   cd path/to/WCAG-Compliance-Testing
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - **On Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - **On macOS/Linux**:

     ```bash
     source venv/bin/activate
     ```

### Install Dependencies

With the virtual environment active, install the required packages:

```bash
pip install -r requirements.txt
```

The `webdriver-manager` will automatically handle WebDriver binaries, so no need for manual WebDriver setup.

## Usage

1. **Run Color Contrast Test**:

   ```bash
   pytest tests/test_color_contrast.py
   ```

2. **Run Screen Reader Test**:

   ```bash
   pytest tests/test_screen_reader.py
   ```

Review the output logs to see any issues detected and suggestions for compliance.

## Project Structure

```plaintext
WCAG-Compliance-Testing/
│
├── pages/                         # Page Objects for web elements
│   ├── cowrywise_page.py          # Example Page Object file
│
├── tests/                         # Test scripts for different accessibility checks
│   ├── test_color_contrast.py     # Script for color contrast testing
│   ├── test_screen_reader.py      # Script for screen reader testing
│
├── requirements.txt               # List of dependencies
├── README.md                      # Project documentation
├── .gitignore                     # Git ignore file
└── venv/                          # Virtual environment directory (not included in version control)
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch-name`).
3. Make your changes and commit (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch-name`).
5. Open a pull request.

## License

# Custom License

Copyright (c) 2024 Adeniyi John

## Terms of Use

1. **Permission Required**: This software and its associated documentation files (the "Software") cannot be used, copied, modified, merged, published, distributed, or otherwise dealt with in any way until you have obtained explicit permission from the copyright holder, Adeniyi John.

2. **Contact Information**: To request permission, please contact Adeniyi John.

3. **No Warranty**: The Software is provided "as is," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the author or copyright holder be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the Software or the use or other dealings in the Software.

## Usage

To use the Software, please ensure you have received written consent from Adeniyi John. Unauthorized use is prohibited.
