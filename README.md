# A Multimodal Dataset of Fact-Checked News from Chile’s Constitutional Processes: Collection, Processing and Analysis

The objective of this project is to develop multimodal models to analyze visual fake news disseminated on social media within the context of Chile's two constitutional processes. This initiative emerges as part of a broader research endeavor aimed at creating a computational framework for the extraction of multimodal narratives and the application of advanced language models, with a specific focus on detecting and understanding fake news.

The first phase of the project involves constructing an embedding model capable of effectively capturing the information contained in visual fake news. This model will facilitate the calculation of similarity metrics between such publications, enabling the identification of related events through the formation of semantic clusters. These clusters are expected to provide insights into the relationships and patterns underlying the dissemination of fake news.

This project represents a critical step towards the development of robust computational tools for analyzing and understanding the propagation of multimodal narratives in online ecosystems, with implications for combating misinformation at a societal level.

## Getting Started

You need a version of **Python** equal to or greater than **3.11.9** ([download Python](https://www.python.org/downloads/)). Using **Visual Studio Code** is recommended.

1. Clone Project

   ```bash
   git clone https://github.com/MolodyGs/CapstoneProject.git
   ```

2. Create a Virtual Environment (if needed)

   ```bash
   python -m venv .venv
   .venv/Scripts/activate
   ```

3. Install Dependencies
   This procedure can take between 10 to 20 minutes depending on connectivity.
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Get Pages - `get_pages.ipynb`
2. Text Model - `text_model.ipynb`
3. Text Extraction from Images - `text_extract_in_images.ipynb`
4. Hybrid Model - `hybrid_model.ipynb`
5. Multimodal Model - `multimodal_model.ipynb`

## Conceptual Map of Models (in Spanish)

![Conceptual Map](models_conceptual_map.png)
