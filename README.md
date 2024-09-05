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
- **WCAG-Contrast-Ratio**: For calculating color contrast ratios.
- **WebDriver**: For interacting with browsers (Chrome, Firefox, etc.).

## Setup

### Prerequisites

1. Python 3.7 or above installed on your machine.
2. Selenium WebDriver (e.g., ChromeDriver) installed and accessible in your system path.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/WCAG-Compliance-Testing.git
   cd WCAG-Compliance-Testing
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Update the WebDriver path in your test scripts if necessary.

## Usage

1. **Run Color Contrast Test**:

   ```bash
   python tests/test_color_contrast.py
   ```

2. **Run Screen Reader Test**:

   ```bash
   python tests/test_screen_reader.py
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
└── .gitignore                     # Git ignore file
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch-name`).
3. Make your changes and commit (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Only1JohnN/WCAG-Compliance-Testing/blob/main/LICENSE) file for details.
