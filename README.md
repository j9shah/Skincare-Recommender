# 🌟 Skincare Recommender

## 🛠️ Overview
The Skincare Recommender is a Python-based application designed to help users find skincare and makeup products tailored to their skin type, budget, and preferences. The project leverages a graph-based recommendation system, enabling efficient product filtering using user-defined parameters. The application features an interactive GUI built with Tkinter, providing a seamless user experience.

## ✨ Features
- **🔗 Graph-Based Recommendation System**: Utilizes a graph data structure where users and products are nodes, and reviews form the edges.
- **💻 Interactive GUI**: Built with Tkinter, enabling users to input preferences and receive real-time product recommendations.
- **📊 Data Handling**: Processes large-scale datasets of over 8000 reviews, sampled for efficient computation and compatibility.
- **🎯 Custom Filters**: Allows users to filter by skin type, budget, and product brand.

## 💡 Motivation
The Skincare Recommender addresses the inefficiency of existing platforms in providing accurate product recommendations. By focusing on personalized suggestions, it aims to enhance user confidence and satisfaction while promoting informed purchasing decisions.

## 🚀 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/skincare-recommender.git
   cd skincare-recommender
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage
1. Download the required datasets and place them in the `data/` directory:
   - `data/sample_products.csv`
   - `data/reviews/`

2. Run the main application:
   ```bash
   python main.py
   ```

3. Interact with the Tkinter GUI to input your preferences and view recommended products.

## 📂 File Structure
```
.
├── data
│   ├── sample_products.csv   # Sample product data
│   └── reviews/              # Sample review data
├── main.py                   # Entry point of the application
├── network.py                # Graph-based recommendation system implementation
├── simulation.py             # Tkinter GUI implementation
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## ⚙️ How It Works
1. **📐 Data Representation**: Products and users are represented as nodes in a graph, with reviews forming the edges.
2. **🔍 Filtering**: Filters are applied based on user inputs (skin type, budget, etc.) to find the most suitable products.
3. **📈 Popularity Ranking**: If no products match the filters, recommendations default to the most popular products based on the number of reviews.
4. **🖱️ GUI Interaction**: Users interact with the system via dropdown menus and buttons in the Tkinter GUI.

## ⚠️ Limitations
- Sampled datasets due to computational constraints.
- Skin type suitability is derived from user reviews, as direct data was unavailable.
- Lack of personalized tracking for user preferences in the current implementation.

## 🛠️ Future Work
- Incorporate a tracking mechanism for personalized recommendations based on user history.
- Suggest similar products in addition to the most relevant matches.
- Expand dataset processing capabilities to handle the full datasets without sampling.

## 👥 Contributors
- **Cailyn Kim**
- **Vivian Feng**
- **Jainam Shah**
- **Jennifer Tan**

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgments
- Data sources: [Kaggle](https://www.kaggle.com)
- Tutorials: [TutorialsPoint](https://www.tutorialspoint.com/python/python_gui_programming.htm)
