<h3 align="center">EECS 581 - Group20 Project 1</h3>

<p align="center">
  Minesweeper
  <br />
  10x10 Single-Player Puzzle Game
  <br />
  <a href="https://github.com/phsadhankar/EECS-581-Project-1/tree/main/docs"><strong>Explore the docs »</strong></a>
  <br />
  <a href="https://github.com/phsadhankar/EECS-581-Project-1/tree/main/src"><strong>See the code »</strong></a>
  <br />
  <a href="https://github.com/phsadhankar/EECS-581-Project-1/tree/main/test"><strong>Check out tests »</strong></a>
  <br />
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#meet-the-team">Meet the Team</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#repository-structure">Repository Structure</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contacts">Contacts</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This project is developed as part of EECS 581 – Software Engineering II and focuses on developing Minesweeper, a single-player puzzle game played on a 10x10 grid. The game allows players to uncover cells, flag suspected mine locations, and use adjacent mine counts to safely navigate the board.

The objective of the game is to uncover all non-mine cells without detonating a mine. The project emphasizes modular system design, implementation, testing, documentation, and extensibility for future development.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MEET THE TEAM -->

## Meet the Team

|  Team Member  |         Role         |                                           Responsibilities                                           |  Availability  | Programming Experience | Computing Platform Experience |
| :-----------: | :------------------: | :--------------------------------------------------------------------------------------------------: | :------------: | :--------------------: | :---------------------------: |
| [Team Member] |    Project Leader    |   Coordinates team meetings, tracks project progress, and ensures project milestones are completed   | [Availability] |      [Experience]      |     [Platform Experience]     |
| [Team Member] |   Technical Leader   |            Provides technical direction and assists with implementation and system design            | [Availability] |      [Experience]      |     [Platform Experience]     |
| [Team Member] |    GitHub Manager    |        Manages the repository, maintains organization, and handles merges and version history        | [Availability] |      [Experience]      |     [Platform Experience]     |
| [Team Member] | Documentation Leader |           Maintains project documentation and ensures documentation is clear and consistent          | [Availability] |      [Experience]      |     [Platform Experience]     |
| [Team Member] |   QA Testing Leader  |          Develops test cases, performs testing, and ensures identified defects are resolved          | [Availability] |      [Experience]      |     [Platform Experience]     |
| [Team Member] |  Integration Leader  | Ensures code from different team members integrates properly and the complete program runs correctly | [Availability] |      [Experience]      |     [Platform Experience]     |
| [Team Member] |     UX/UI Leader     |    Leads the design and implementation of the game interface to make sure the game is easy to use    | [Availability] |      [Experience]      |     [Platform Experience]     |
 
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Follow these steps to build and run Minesweeper locally.

### Prerequisites

- C++ compiler
- Git
- Bash or compatible shell

### Installation

1. Clone the repository

    - git clone https://github.com/phsadhankar/EECS-581-Project-1

2. Navigate into the project directory

    - cd EECS-581-Project-1/src

3. Build/install the program if necessary

    - `[BUILD COMMAND]`

4. Run the program

    - `[RUN COMMAND]`
  
5. (Optional) Clean build files:

    - `[CLEAN COMMAND]`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

When the game begins, the player selects the number of mines to place on the board. The number of mines must be between **10 and 20**.

The game is played on a **10x10 grid**, with columns labeled **A–J** and rows numbered **1–10**.

Players can:
- Uncover a covered cell
- Place a flag on a suspected mine
- Remove a previously placed flag
- View the number of remaining flags
- View the current game status

When a mine-free cell is uncovered, the cell displays a number from **0–8** representing the number of mines in the surrounding cells. If a cell has zero adjacent mines, neighboring cells are automatically uncovered.

The first cell selected by the player is guaranteed to be mine-free.

### Winning

The player wins by uncovering all non-mine cells without detonating a mine. When all safe cells have been uncovered, the game status displays **Victory**.

### Losing

If the player uncovers a mine, the game ends and all mines are revealed. The game status displays **Game Over: Loss**.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap
- [ ] Project Planning
- [ ] System Architecture Design
- [ ] Implementation
- [ ] Mine Placement and Board Generation
- [ ] Cell Uncovering and Flagging
- [ ] Win/Loss Detection
- [ ] User Interface
- [ ] Test Cases
- [ ] System Documentation
- [ ] Final Testing
- [ ] Final Demonstration

See the [open issues](docs/knownIssues.md) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- REPO STRUCTURE -->
## Repository Structure

* `/docs` – Project documentation, including system architecture, diagrams, person-hour estimates, and actual person-hour records
* `/src` – Minesweeper source code
* `/test` – Test cases and validation files

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

This project is developed for academic purposes as part of EECS 581 – Software Engineering II at the University of Kansas.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contacts

[Team Member] - [KU Email]<br />
[Team Member] - [KU Email]<br />
[Team Member] - [KU Email]<br />
[Team Member] - [KU Email]<br />
[Team Member] - [KU Email]<br />
[Team Member] - [KU Email]<br />
[Team Member] - [KU Email]<br />

Project Link: [EECS 581 Group20 Project 1 – Minesweeper]([GITHUB-REPOSITORY-URL])

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

The team acknowledges Professor Hossein Saiedian for defining the project objectives and providing instructional guidance within the EECS 581 – Software Engineering II course.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
