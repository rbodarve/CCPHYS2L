# Electrostatics Calculator

A comprehensive Python application for visualizing and calculating electrostatic properties on a 2D Cartesian plane. This interactive tool allows users to place charged particles and perform various electrostatics calculations including electric fields, potentials, forces, and more.

## Features

### Interactive 2D Cartesian Plane

- Visual grid-based coordinate system
- Real-time particle placement with mouse clicks
- Color-coded particles (blue for positive, red for negative)
- Coordinate conversion between screen and mathematical coordinates

### Particle Management

- Add positive particles (protons) - displayed as blue circles
- Add negative particles (electrons) - displayed as red circles
- Custom charge values for each particle
- Visual charge labels on each particle
- Clear all particles functionality

### Comprehensive Calculations

1. **Electric Field at a Point** - Calculate field components, magnitude, and direction
2. **Electric Potential at a Point** - Find potential at any specified location
3. **Force on a Charge** - Calculate force on a test charge at any point
4. **Potential Energy of the System** - Total electrostatic potential energy
5. **Electric Flux** - Through a specified Gaussian surface (circular)
6. **Gauss's Law** - Application using flux calculations
7. **Dipole Moment** - Electric dipole moment of the entire system

## Installation

### Prerequisites

- Python 3.12.3 or higher
- pip (Python package installer)

### Setup

1. Clone or download this repository
2. Navigate to the project directory
3. Install required dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application

```bash
python electromagnetism.py
```

## Usage Guide

### Getting Started

1. **Launch the application** - Run the Python script
2. **Add particles** - Click either "Add Positive Particle" or "Add Negative Particle"
3. **Place particles** - Click anywhere on the Cartesian plane to place a particle
4. **Set charge** - Enter the charge value when prompted
5. **Repeat** - Add as many particles as needed
6. **Calculate** - Click the "Calculate" button to access computation options

### Particle Placement

- **Positive Particles**: Click "Add Positive Particle" → Click on plane → Enter charge
- **Negative Particles**: Click "Add Negative Particle" → Click on plane → Enter charge
- **Coordinates**: Based on the visual grid where each square represents one unit
- **Charge Values**: Can be any positive number (sign is determined by particle type)

### Calculations

#### Electric Field at a Point

- Calculates the electric field vector at any specified point
- Shows X and Y components, magnitude, and direction angle
- Uses superposition principle for multiple charges

#### Electric Potential at a Point

- Finds the electric potential (voltage) at any point
- Accounts for all particles in the system
- Results in volts (V)

#### Force on a Charge

- Calculates force on a test charge placed at any point
- Shows force components, magnitude, and direction
- Requires input of test charge value and position

#### Potential Energy of the System

- Calculates total electrostatic potential energy
- Considers all pairwise interactions between particles
- Requires at least 2 particles

#### Electric Flux

- Calculates flux through a circular Gaussian surface
- Requires center coordinates and radius
- Shows enclosed charge and resulting flux

#### Gauss's Law

- Demonstrates Gauss's law using flux calculations
- ∮ E⋅dA = Q_enclosed/ε₀

#### Dipole Moment

- Calculates electric dipole moment of the system
- Shows vector components and magnitude
- Indicates if system has net charge

### Navigation

After each calculation, you have three options:

- **Back to Plane**: Return to the main interface
- **Back to Calculations**: Return to the calculation menu
- **Close Program**: Exit the application

## Technical Details

### Physics Constants

- Coulomb's constant (k): 8.99 × 10⁹ N⋅m²/C²
- Permittivity of free space (ε₀): 8.854 × 10⁻¹² F/m

### Coordinate System

- Origin (0,0) at the center of the canvas
- X-axis increases to the right
- Y-axis increases upward (standard mathematical convention)
- Grid scale: 20 pixels per unit

### Error Handling

- Prevents division by zero when points coincide with particles
- Input validation for all user entries
- Graceful handling of calculation errors

## File Structure

```
electrostatics-calculator/
│
├── electrostatics_calculator.py    # Main application file
├── requirements.txt                # Python dependencies
└── README.md                      # This file
```

## Dependencies

### Required Packages

- **numpy**: For mathematical calculations and array operations
- **tkinter**: For GUI interface (usually included with Python)

### Standard Library Modules Used

- `math`: Mathematical functions
- `messagebox`: Dialog boxes
- `simpledialog`: Input dialogs

## System Requirements

### Minimum Requirements

- Python 3.7+
- 4 GB RAM
- 100 MB free disk space
- Display resolution: 1024x768 or higher

### Recommended Requirements

- Python 3.9+
- 8 GB RAM
- Display resolution: 1920x1080 or higher

## Educational Applications

This tool is ideal for:

- **Physics Education**: Visualizing electrostatic concepts
- **Student Learning**: Interactive exploration of electric fields
- **Problem Solving**: Verification of analytical calculations
- **Demonstrations**: Classroom presentations of electrostatics

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Built using Python's tkinter for cross-platform compatibility
- Physics calculations based on standard electrostatics formulas
- Designed for educational and research applications
