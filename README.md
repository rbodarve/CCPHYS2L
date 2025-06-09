# CCPHYS2L - Electromagnetism Problem Solver

A Python-based GUI application for solving common electromagnetism problems, designed for physics students and educators.

## Features

- **Interactive GUI**: User-friendly interface built with Tkinter
- **Multiple Problem Types**: 
  - Coulomb's Law (Electrostatic Force)
  - Electric Field calculations
  - Electric Potential
  - Capacitance
  - Magnetic Force
- **Dynamic Variable Input**: Add/remove variables as needed
- **Real-time Problem Solving**: Instant calculations with proper error handling

## Screenshots

*GUI interface showing problem type selection and variable inputs*

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/CCPHYS2L.git
   cd CCPHYS2L
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**
   ```bash
   python electromagnetism-problem-solver.py
   ```

2. **Using the solver**:
   - Select a problem type from the dropdown menu
   - Add variables by clicking "Add Variable"
   - Enter known values in the input fields
   - Click "Solve Problem" to get the solution
   - Use the "X" button to remove unwanted variable rows

## Supported Problem Types

### Coulomb's Law
Calculate electrostatic force between two point charges:
- **Formula**: F = k(q₁q₂)/r²
- **Variables**: Force, Charge1, Charge2, Distance, Coulomb Constant

### Electric Field
Calculate electric field strength:
- **Formula**: E = F/q
- **Variables**: Electric Field, Force, Charge, Distance

### Electric Potential
Calculate electric potential:
- **Formula**: V = W/q
- **Variables**: Potential, Work, Charge

### Capacitance
Calculate capacitance:
- **Formula**: C = Q/V
- **Variables**: Capacitance, Charge, Voltage

### Magnetic Force
Calculate magnetic force on a moving charge:
- **Formula**: F = qvB
- **Variables**: Magnetic Force, Charge, Velocity, Magnetic Field

## Examples

### Example 1: Coulomb's Law
To find the force between two charges:
1. Select "Coulomb's Law (Electrostatic Force)"
2. Add variables: Charge1 = 1e-6, Charge2 = 2e-6, Distance = 0.1
3. Click "Solve Problem"
4. Result: Force in Newtons

### Example 2: Electric Field
To find electric field strength:
1. Select "Electric Field"
2. Add variables: Force = 0.001, Charge = 1e-6
3. Click "Solve Problem"
4. Result: Electric Field in N/C

## Development

### Project Structure
```
CCPHYS2L/
├── electromagnetism-problem-solver.py    # Main application file
├── requirements.txt                      # Python dependencies
├── README.md                            # Project documentation
├── .gitignore                          # Git ignore rules
└── LICENSE                             # Project license
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

### Future Enhancements

- [ ] Add more problem types (Gauss's Law, Electromagnetic Induction)
- [ ] Implement unit conversion
- [ ] Add step-by-step solution explanations
- [ ] Include visual diagrams
- [ ] Support for vector calculations
- [ ] Add problem history and save/load functionality

## Requirements

- Python 3.7+
- tkinter (usually included with Python)
- math (standard library)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Author**: [Your Name]
- **Email**: [your.email@example.com]
- **GitHub**: [yourusername]

## Acknowledgments

- Physics formulas and constants from standard electromagnetism textbooks
- Built with Python's tkinter for cross-platform GUI support
- Designed for educational purposes in physics courses

---

*This application is part of the CCPHYS2L (College Physics 2 Laboratory) coursework.*