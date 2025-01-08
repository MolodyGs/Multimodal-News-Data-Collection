<style>
   .center-image {
      display: flex;
      justify-content: center;
      width: 100%;
   }
</style>

# A Multimodal Dataset of Fact-Checked News from Chile’s Constitutional Processes: Collection, Processing and Analysis

The objective of this project is to develop multimodal models to analyze visual fake news disseminated on social media within the context of Chile's two constitutional processes. This initiative emerges as part of a broader research endeavor aimed at creating a computational framework for the extraction of multimodal narratives and the application of advanced language models, with a specific focus on detecting and understanding fake news.

The first phase of the project involves constructing an embedding model capable of effectively capturing the information contained in visual fake news. This model will facilitate the calculation of similarity metrics between such publications, enabling the identification of related events through the formation of semantic clusters. These clusters are expected to provide insights into the relationships and patterns underlying the dissemination of fake news.

This project represents a critical step towards the development of robust computational tools for analyzing and understanding the propagation of multimodal narratives in online ecosystems, with implications for combating misinformation at a societal level.

## Project Setup

To start, ensure you have **Python** version **3.11.9** or higher installed ([download Python here](https://www.python.org/downloads/)). It is recommended to use **Visual Studio Code** as the development environment.

1. Clone the Repository

   ```bash
   git clone https://github.com/MolodyGs/CapstoneProject.git

   ```

2. Create a Virtual Environment (if necessary)

   ```bash
   python -m venv .venv
   .venv/Scripts/activate
   ```

3. Install Dependencies

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Retrieve Pages - **get_pages.ipynb**
2. Text Modeling - **text_model.ipynb**
3. Text Extraction from Images - **text_extract_in_images.ipynb**
4. Hybrid Model - **hybrid_model.ipynb**
5. Multimodal Model - **multimodal_model.ipynb**

## Text Model

<div class="center-image">
   <img src="src/assets/text_model.pdf" alt="text model" width="200">
</div>

## Hybrid Model

<div class="center-image">
   <img src="src/assets/hybrid_model.pdf" alt="hybrid model" width="350">
</div>

## Multimodal Model

<div class="center-image">
   <img src="src/assets/multimodal_model.pdf" alt="multimodal model" width="350">
</div>
