# Electrostatics Calculator

**Final Project for Physics 2 Electromagnetism (CCPHYS2L)**

A comprehensive Python application for visualizing and calculating electrostatic properties on a 2D Cartesian plane. This interactive tool allows users to place charged particles and perform various electrostatics calculations including electric fields, potentials, forces, and more.

## Project Information

**Course**: CCPHYS2L - College Physics 2 (Electromagnetism)  
**Project Team**:
- James Adrian Castro
- Harley Galamiton
- Renaire Odarve
- Jude Renwell Prodigalidad

## Features

### Interactive 2D Cartesian Plane

- Visual grid-based coordinate system
- Real-time particle placement with mouse clicks
- Color-coded particles (blue for positive, red for negative)
- Coordinate conversion between screen and mathematical coordinates

### Particle Management

- Add positive particles (protons) - displayed as blue circles
- Add negative particles (electrons) - displayed as red circles
- Custom charge values for each particle (validated to a physical range)
- Visual charge labels on each particle
- **Edit Charge** - Double-click a particle (or right-click → Edit Charge) to change its charge
- **Delete Particle** - Right-click a particle → Delete Particle
- Clear all particles functionality
- **Save Configuration** - Save current particle setup to JSON file
- **Load Configuration** - Load previously saved particle configurations
- **Undo/Redo** - Undo and redo particle actions (add, delete, edit, clear, load)

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

- Python 3.7 or higher
- tkinter (usually included with Python)

### Setup

1. Clone or download this repository
2. Navigate to the project directory

**Note**: No additional packages need to be installed. All dependencies are part of Python's standard library.

### Running the Application

```bash
python electromagnetism.py
```

## Usage Guide

### Getting Started

1. **Launch the application** - Run the Python script
2. **Add particles** - Click either "Add Positive Particle" or "Add Negative Particle"
3. **Place particles** - Click anywhere on the Cartesian plane to place a particle
4. **Set charge** - Enter the charge magnitude when prompted (the sign is set by particle type)
5. **Repeat** - Add as many particles as needed
6. **Calculate** - Click the "Calculate" button to access computation options

### Particle Placement

- **Positive Particles**: Click "Add Positive Particle" → Click on plane → Enter charge
- **Negative Particles**: Click "Add Negative Particle" → Click on plane → Enter charge
- **Coordinates**: Based on the visual grid where each square represents one unit (1 meter)
- **Charge Values**: Enter the magnitude only; the sign is set automatically by particle type. Values are validated to the range 1×10⁻¹² C to 1×10⁻³ C (zero and out-of-range values are rejected)

### Editing and Deleting Particles

- **Edit Charge**: Double-click a particle, or right-click it and choose "Edit Charge", then enter a new magnitude
- **Delete Particle**: Right-click a particle and choose "Delete Particle"

### Configuration Management

- **Save Configuration**: Save your current particle setup to a JSON file for later use
- **Load Configuration**: Load a previously saved particle configuration
- **Undo**: Undo the last action (add, delete, edit charge, clear, or load)
- **Redo**: Redo a previously undone action
- **Clear All**: Remove all particles from the plane

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
- Distance unit: 1 grid unit = 1 meter (coordinates are used directly as meters in the SI calculations)

### Error Handling

- Prevents division by zero when a calculation point coincides with a particle, or when two particles occupy the same location
- Charge input validation with an enforced physical range
- Graceful handling of calculation and file save/load errors with recovery suggestions

## File Structure

```
CCPHYS2L/
│
├── electromagnetism.py    # Main application file
├── LICENSE.md             # MIT License
├── README.md              # This file
└── .gitignore             # Git ignore rules
```

## Dependencies

### Required Packages

- **tkinter**: For GUI interface (usually included with Python)

### Standard Library Modules Used

- `math`: Mathematical functions and calculations
- `tkinter.messagebox`: Dialog boxes for user notifications
- `tkinter.simpledialog`: Input dialogs for user input
- `tkinter.filedialog`: File save/load dialogs
- `itertools`: For efficient iteration operations
- `json`: For saving and loading particle configurations
- `datetime`: For timestamping saved files

## System Requirements

- Python 3.7 or higher with tkinter (part of the standard library)
- Any OS with a graphical display (Windows, macOS, or Linux)
- A display large enough for the fixed 1000×700 application window (1024×768 or higher recommended)

The application is a lightweight standard-library script with negligible memory and disk requirements.

## Educational Applications

This tool is ideal for:

- **Physics Education**: Visualizing electrostatic concepts
- **Student Learning**: Interactive exploration of electric fields
- **Problem Solving**: Verification of analytical calculations
- **Demonstrations**: Classroom presentations of electrostatics

## Review notes (2026-10-14)

A later code review and simulation run. The program code is unchanged; this section only records the findings.

### Known issues

| # | What happens | How to reproduce | Suggested fix |
|---|---|---|---|
| S1 | Load onto an empty plane cannot be undone, and Redo after a load replaces the loaded particles with an old state. Fix checked in a copy. | Add a particle → Undo → Load a file → Redo | `load_configuration` (line 707): always call `save_state()`, which also clears the redo stack |
| S2 | A bad file leaves a partial or empty plane. Fix checked in a copy. | Load `{"particles": [{"x": 1}]}`, or a file whose second entry has `"charge": "big"` | Lines 709-718: build the new list first, then call `restore_state`; on error keep the old particles |
| S3 | Values from a file skip charge validation. Fix checked in a copy. | Load a file with charge −1e-9, 0 or 1.0, or `"particle_type": "neutron"` | Line 715: run `validate_charge` and accept only `"proton"` or `"electron"` (`validate_charge` shows its own error dialog, so a bad charge then gives two dialogs; check the range inline to avoid this) |
| S4 | A huge coordinate crashes the calculation; `nan` input prints `nan` results | Electric field at x = 1e200, or x = nan | Line 811: also catch `OverflowError`; reject non-finite input with `math.isfinite` |
| S5 | A negative Gaussian radius is accepted | Electric Flux with radius −5 | Line 970: reject `radius <= 0` |
| S6 | A zero field shows a direction of 0.0° | +1 nC at (−1, 0) and (1, 0), point (0, 0) | Lines 77 and 114: print "undefined" when the magnitude is 0 |
| S7 | Two particles can be placed on the same spot; Potential Energy then always fails | Click the same pixel twice | Line 432: reject a click on an existing particle |
| S8 | A neutral system can be reported as charged | +1 nC, +2 nC and −3 nC | Line 1007: use `math.isclose(total_charge, 0, abs_tol=1e-15)` |
| S9 | Cancelling the first input still shows the next inputs | Cancel X in the Electric Field dialog | Line 858: return after each cancelled input |
| S10 | Right-click on overlapping particles selects the hidden one | Particles at canvas x = 400 and x = 404 | Line 515: search `reversed(self.particles)` |

### Edge cases

- A neutral system can show a tiny net charge (about 4×10⁻²⁵ C) because of floating-point rounding (S8).
- For a system with a net charge, the dipole moment depends on the choice of origin; the result only notes the net charge.
- The test charge in "Force on a Charge" is not validated (0, `nan` and `inf` are accepted).
- The "Current Particles" box shows 6 rows and has no scrollbar; particle 7 and later are hidden.

### Simplification ideas

- Compute the force as test charge × electric field instead of repeating the field loop (lines 98-117).
- Let `load_configuration` call `restore_state` instead of repeating it (lines 711-718).
- Store the signed charge once instead of `particle.charge * particle.sign` in 6 places.
- Merge `toggle_proton_mode` and `toggle_electron_mode` into one method (lines 344-359).
- Use `collections.deque(maxlen=50)` for the undo stack instead of `list.pop(0)` (lines 597-599).
- Use `math.hypot(dx, dy)` instead of `math.sqrt(dx**2 + dy**2)` (6 places).

### Tested

- 846 automated checks.
- Physics: `PhysicsEngine` with 60 random setups (1-6 particles), compared with an independent Coulomb's-law calculation, plus known cases. Field, potential, force, potential energy, flux and the neutral dipole are correct.
- Application: the real `ElectrostaticsCalculator` on a hidden window, with the input, message and file dialogs replaced by scripted answers. 30 random add/delete/edit/clear/undo/redo sequences were checked against a model, plus save/load, bad files and input edge cases.
- Not tested: real mouse clicks and double-click timing, the right-click menu, modal window behavior, real file dialogs, the visual layout and the "Close Program" buttons.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Built using Python's tkinter for cross-platform compatibility
- Physics calculations based on standard electrostatics formulas
- Designed for educational and research applications
