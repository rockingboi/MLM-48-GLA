# MLM-GLA(MACHINE LEARNING MANTHAN)
Hackhaton of GLA UNIVERSITY for experinceing the industry level problem statements.

# HVAC Energy Efficiency Simulator with Q-Learning

This project demonstrates how reinforcement learning (Q-learning) can be used to optimize energy efficiency in buildings by controlling HVAC systems. It uses the [Energy Efficiency Data Set](https://archive.ics.uci.edu/ml/datasets/energy+efficiency) from the UCI Machine Learning Repository.

## 📂 Dataset

The dataset includes features that influence energy consumption (like surface area, wall area, height, glazing area, etc.), and target values: `Heating_Load` and `Cooling_Load`.

- File used: `ENB2012_data.xlsx`
- Extracted from a `.zip` archive
- Loaded and preprocessed with `pandas`

## 🛠 Project Features

- Preprocessing using `MinMaxScaler`
- Custom OpenAI Gym environment `EnergyEnv`
- Q-learning agent for HVAC control
- Discretization of continuous input state space
- ε-greedy policy for action selection
- Training with reward tracking and epsilon decay
- Visualizations for learning performance

## 🚀 Getting Started

### 1. Clone the Repository

```bash
2. Setup Environment (Recommended for local setup)
pip install -r requirements.txt
3. Run Training
The training loop runs for 1000 episodes and optimizes the Q-table for actions like turning HVAC off, low fan (21°C), high fan (23°C), or low fan (24°C).

4. Visualize Results
Training rewards and epsilon decay are plotted to show convergence of the Q-learning algorithm.

🧠 RL Algorithm
Actions:

0: HVAC off (25°C)

1: Low fan (21°C)

2: High fan (23°C)

3: Low fan (24°C)

State: 8 feature values scaled between 0–1 and discretized

Reward Function:

Penalizes high energy usage

Adds comfort penalty if setpoint is outside 21–24°C

💾 Model Saving
Trained components saved as:
q_table.pkl   # Q-values dictionary
scaler.pkl    # MinMaxScaler object
bins.pkl      # Discretization bins
Use pickle.load() to reload them for inference or further training.

📦 Requirements
pandas
numpy
scikit-learn
matplotlib
gym
openpyxl
streamlit (optional for UI)
Install via:

bash
pip install -r requirements.txt
🖥️ Deployment
You can build a web interface using Streamlit to simulate the environment and visualize decisions made by the Q-learning agent.

🌐 Remote Access (Colab)
To share your Colab notebook:
!npm install -g localtunnel@2.0.2
!lt --port 8501
📊 Sample Output
Reward improves over episodes

Epsilon gradually decays from 1.0 to 0.01

Agent learns to keep temperature within the comfort zone while minimizing energy use

📜 License
This project is licensed under the MIT License.

✍️ Author
Puneet Sharma , Tripti Gupta

Feel free to fork or contribute!
