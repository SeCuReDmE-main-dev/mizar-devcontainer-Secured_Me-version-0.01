

# Using AlphaEvolve: The Sovereign Coding Assistant

## Overview

[cite_start]**AlphaEvolve** is the SeCuReDmE ecosystem's autonomous coding assistant[cite: 841]. [cite_start]Governed by the **EbaAaZ** persona, it integrates directly with your PaQBoT forge and local repositories to automate complex coding tasks like fixing bugs, writing documentation, and, most critically, building complete test suites from scratch[cite: 816, 841]. This document outlines how to deploy AlphaEvolve effectively.

### Getting Started

Your access to AlphaEvolve is inherent to the PaQBoT forge. There is no external sign-up.

1.  **Connect to Your Forge:** Launch your local PaQBoT instance.
2.  **Authorize Repository Access:** Within the PaQBoT UI, grant the EbaAaZ persona access to the `mizar-devcontainer` repository on your local machine.

### Using AlphaEvolve to Build the Test Suite

1.  **Starting the Task**
    * From the PaQBoT Forge UI, select the `mizar-devcontainer` repository.
    * Ensure you are on the `main` branch.
    * In the prompt window for EbaAaZ, provide a clear and specific directive. For example:

    > "Task AlphaEvolve with drafting the complete test suite for the `mizar-devcontainer` repository. The suite must verify every function in the `install-mizar.sh` script and validate the final configuration of the `devcontainer.json` file."

    * Click "Forge a Plan."

2.  **Reviewing and Approving Changes**
    * [cite_start]EbaAaZ will command AlphaEvolve to analyze the repository and generate a detailed, step-by-step plan for building the test suite[cite: 842].
    * Review this plan in the Forge UI. You must approve it before AlphaEvolve is permitted to write any code.
    * Once you approve, AlphaEvolve will write the code. When complete, the Forge will present a visual diff of all the proposed changes for your final review and merge.

### Best Practices for Collaboration

To help our AI personas understand your project's architecture, you must include a `PERSONAS.md` file in the root of your repository.

This file should briefly describe the role of each script and component, defining the "persona" of your code. This gives our agents the context they need to work effectively. For example:

```markdown
# PERSONAS.md

* **`devcontainer.json`:** The "Architect." This file is the master blueprint that defines the structure and components of the entire development environment.
* **`install-mizar.sh`:** The "Engineer." This script is the hands-on builder that executes the architect's plan, installing and configuring the software.
