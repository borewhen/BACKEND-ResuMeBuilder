question_map = {
    "Frontend Engineering": {
        "Typescript": [
            {
                "question": "How does TypeScript improve code maintainability in large-scale applications?",
                "answer": "",
                "feedback": "Good understanding of the key benefits, mainly highlighting on static typing — and how it contributes to maintainability by catching errors early. To improve your answer, consider expanding slightly on how better tooling (like autocompletion, refactoring support, and IDE integration) enhances developer productivity, especially in collaborative environments."
            },
            {
                "question": "What are the differences between interface and type in TypeScript?",
                "answer": "",
                "feedback": "Good. You covered the basic technical differences clearly. Could be stronger by giving a use-case of when to prefer one over the other."
            },
            {
                "question": "Explain generics in TypeScript and give a practical use case.",
                "answer": "",
                "feedback": "Excellent! This showed both conceptual and practical understanding."
            }
        ],
        "Next.js": [
            {
                "question": "How does Next.js handle server-side rendering (SSR) vs. static site generation (SSG)?",
                "answer": "",
                "feedback": "Good answer. Consider adding Incremental Static Regeneration (ISR) for a more comprehensive answer."
            },
            {
                "question": "What’s the benefit of using getServerSideProps versus getStaticProps?",
                "answer": "",
                "feedback": "Solid response with correct reasoning. Could improve by mentioning SEO benefits or user experience implications."
            },
            {
                "question": "How do you implement API routes in Next.js?",
                "answer": "",
                "feedback": "Accurate and clear. Well done!"
            }
        ]
    },
    "LLM & AI System": {
        "Embeddings": [
            {
                "question": "What is an embedding in the context of language models, and how is it typically generated?",
                "answer": "",
                "feedback": "This is technically true but too vague. Expand by saying embeddings are high-dimensional vectors that capture semantic similarity, enabling tasks like clustering, search, and classification. Describe how they allow comparison between documents in a meaningful way."
            },
            {
                "question": "Why are vector similarity metrics like cosine similarity important when working with embeddings?",
                "answer": "",
                "feedback": "This lacks technical reasoning. A good answer would compare trade-offs: OpenAI for performance/convenience, SBERT for open-source and latency, and in-house for control/cost. Mention evaluation techniques like embedding similarity tests or downstream task accuracy."
            },
            {
                "question": "What are some common use cases of text embeddings in modern AI systems?",
                "answer": "",
                "feedback": "This shows no awareness of scaling challenges. Improved answers might mention chunk deduplication, hierarchical indexing (e.g., HNSW), filtering metadata, or embedding compression. Performance tuning is critical as database size grows."
            }
        ],
        "Retrieval-Augmented Generation (RAG)": [
            {
                "question": "What is Retrieval-Augmented Generation (RAG), and how does it enhance the capabilities of language models?",
                "answer": "",
                "feedback": "This shows surface-level understanding. A stronger answer would describe how RAG works: retrieving relevant documents from a knowledge base (via a retriever like a vector search), then feeding those documents as context into a generative model like GPT. Emphasize benefits like reduced hallucination and better factual grounding."
            },
            {
                "question": "What are the main components of a RAG pipeline, and how do they interact during inference?",
                "answer": "",
                "feedback": "This ignores key steps. The answer should involve converting documents to text, chunking, embedding the chunks, storing them in a vector database, then retrieving relevant chunks based on user queries before passing to the LLM. Highlighting these steps shows real understanding."
            },
            {
                "question": "How does using external knowledge in RAG mitigate hallucination in LLM outputs?",
                "answer": "",
                "feedback": "This lacks specificity. Evaluation should involve metrics like retrieval precision/recall, relevance ranking (e.g. NDCG), and answer quality (e.g. BLEU, ROUGE, human evals). Including these shows maturity in understanding system performance."
            }
        ]
    },
    "Backend Engineering": {
        "API Design": [
            {
                "question": "What are REST vs GraphQL tradeoffs for AI-based platforms?",
                "answer": "",
                "feedback": "Good comparative view. Could be improved by referencing tooling support and query complexity in GraphQL."
            },
            {
                "question": "What are the principles of RESTful API",
                "answer": "",
                "feedback": "Good job summarizing REST fundamentals."
            },
            {
                "question": "What are the most common approaches to versioning REST API?",
                "answer": "",
                "feedback": "Accurate, well done! However, to improve your response for an interview setting, I would encourage you to elaborate briefly on each method, even with just one line per approach. For example, you could mention that URI versioning (/api/v1/resource) is the most commonly used due to its simplicity and visibility, while header and media type versioning are more REST-compliant but add complexity."
            }
        ],
        "Serverless Architectures": [
            {
                "question": "What is serverless architecture, and how does it differ from traditional server-based models?",
                "answer": "",
                "feedback": "Oversimplified. Mention benefits like scalability, pay-per-use, and ease of deployment — but also limitations like execution time limits, cold starts, and resource constraints. Use examples like AWS Lambda or Google Cloud Functions."
            },
            {
                "question": "Name two popular serverless platforms and explain what they offer.",
                "answer": "",
                "feedback": "Cold starts impact latency-sensitive applications. A better response could include pre-warming strategies, using provisioned concurrency (in AWS), minimizing dependencies, or offloading tasks to background workers."
            },
            {
                "question": "Does serverless mean there are no servers involved?",
                "answer": "",
                "feedback": "Honest, but unhelpful. Even if unfamiliar, you can still describe hypothetical usage (e.g., triggering Lambda via S3 upload to process PDFs) to show conceptual understanding."
            }
        ]
    }
}

question_map_2 = {
  "Data Analysis & Modelling": {
    "Data Preprocessing": [
      {
        "question": "What steps would you take if your dataset has a lot of missing values?",
        "answer": "If a dataset contains many missing values, my first step is to assess the extent and distribution of the missing data. I use visualizations like heatmaps or bar plots to detect patterns. If only a few values are missing in non-critical columns, I might drop those rows. Otherwise, I consider imputing the missing data. For numerical values, I might use mean, median, or more advanced methods like KNN imputation or regression imputation. For categorical values, mode imputation or using a separate 'Missing' category can be effective. If an entire column has too many missing values and isn’t critical to the analysis, I may consider dropping it entirely.",
        "feedback": "Great job. You demonstrated a solid process with appropriate strategies. For an improvement, you might mention how domain knowledge or data collection processes can help inform imputation choices."
      },
      {
        "question": "How do you handle categorical variables in a dataset before modeling?",
        "answer": "Handling categorical variables depends on the type and the model I'm using. For nominal (unordered) categories, I typically use one-hot encoding. For ordinal (ordered) categories, I use label encoding to preserve the rank. If there are high-cardinality features, I might use target encoding or embedding techniques, especially for tree-based models or neural networks. It's also important to ensure that the encoding is consistent between training and test sets to avoid data leakage.",
        "feedback": "Excellent response. You covered both basic and advanced encoding techniques while considering model compatibility. Great mention of high-cardinality handling and data leakage prevention."
      },
      {
        "question": "What are outliers, and how do you deal with them in your data?",
        "answer": "Outliers are data points that differ significantly from the majority of the data. They can skew statistical analyses and impact model performance. I first detect outliers using visualization tools like box plots, scatter plots, or statistical methods like Z-score and IQR. Once identified, I assess whether they are data entry errors, rare but valid observations, or anomalies worth studying. Depending on the context, I might remove them, cap them (e.g., winsorization), or treat them separately during modeling.",
        "feedback": "Good explanation with a clear process. To improve, you could mention how some models like tree-based algorithms are more robust to outliers, so treatment strategies may differ by model type."
      }
    ],
    "Feature Engineering": [
      {
        "question": "What is feature engineering, and why is it important?",
        "answer": "Feature engineering is the process of creating, transforming, or selecting features from raw data to improve model performance. It’s important because the quality and relevance of features directly affect how well a machine learning model can learn patterns in the data. Good feature engineering can often compensate for simpler models and can significantly enhance predictive power.",
        "feedback": "Excellent answer. You highlighted the core purpose and impact of feature engineering. You could make it even stronger by briefly mentioning examples of techniques like binning, interaction terms, or domain-specific transformations."
      },
      {
        "question": "Can you give an example of a feature you engineered in a project?",
        "answer": "In a previous project predicting customer churn, I created a new feature called 'engagement_score' by combining variables like login frequency, average session time, and interaction count with support. This composite score better captured user behavior than the individual features and helped improve model performance by around 5% in terms of F1-score.",
        "feedback": "Great example—specific, relevant, and shows real impact. Well done on quantifying the improvement. You might also mention if you validated the feature’s importance using feature importance or SHAP values."
      },
      {
        "question": "How do you decide which features to keep and which to discard?",
        "answer": "I start with domain knowledge and correlation analysis to remove irrelevant or redundant features. Then, I apply statistical tests or feature importance methods like mutual information, recursive feature elimination, or tree-based importance scores. I also observe model performance when dropping or adding features during cross-validation. Features that consistently contribute little or lead to overfitting are usually discarded.",
        "feedback": "Solid methodology with a mix of statistical and model-based approaches. To improve, consider briefly touching on dimensionality reduction methods like PCA as another strategy, especially in high-dimensional datasets."
      }
    ],
    "Model Evaluation": [
      {
        "question": "What’s the difference between precision and recall?",
        "answer": "Precision is the ratio of true positives to the total number of positive predictions, meaning it tells us how many of the predicted positives are actually correct. Recall, on the other hand, is the ratio of true positives to the total actual positives, measuring how well the model identifies all relevant instances. For example, in a spam email detection system, high precision means that when the model flags an email as spam, it's usually correct, whereas high recall means that the model successfully identifies most of the spam emails, even if it misclassifies some non-spam ones.",
        "feedback": "Excellent explanation. You clearly articulated the mathematical intuition and also used a relatable real-world example to illustrate the trade-off. This shows a solid grasp of evaluation metrics."
      },
      {
        "question": "How do you avoid overfitting in a machine learning model?",
        "answer": "There are several strategies to avoid overfitting. First, I use cross-validation to ensure the model performs well across different subsets of the data. I also apply regularization techniques such as L1 (Lasso) or L2 (Ridge) to penalize complexity. Reducing the model complexity or number of features, and using pruning in decision trees also help. Additionally, I implement early stopping during training, especially with neural networks, and augment the dataset if needed. Finally, I monitor the gap between training and validation accuracy as a key signal of overfitting.",
        "feedback": "Good answer overall with strong coverage of key techniques. To improve, you could briefly mention how domain knowledge can help in simplifying the model or how using more data helps reduce variance, especially when high-capacity models are involved."
      },
      {
        "question": "How do you select the best model for a particular task?",
        "answer": "To select the best model, I start by understanding the problem type—classification, regression, etc.—and choose a set of candidate models accordingly. I evaluate them using cross-validation and appropriate performance metrics like accuracy, F1 score, AUC-ROC, or RMSE, depending on the context. I also consider interpretability, training time, scalability, and how well the model generalizes. For instance, if I’m working on a high-stakes medical diagnosis problem, I’d prefer models with better interpretability and high recall. Lastly, I might use automated model selection techniques like Grid Search, Random Search, or even AutoML frameworks to assist with hyperparameter tuning and model choice.",
        "feedback": "Very thorough answer with a well-rounded approach. Excellent that you included business/contextual considerations and not just technical metrics. You could slightly improve by briefly mentioning how ensemble methods or model stacking could be part of the final model selection strategy."
      }
    ]
  },

  "Data Tools & Technologies": {
    "SQL Databases": [
      {
        "question": "How do you perform a JOIN operation in SQL, and when would you use it?",
        "answer": "JOINs are used to combine data from multiple tables. I usually use JOIN when I want to connect data based on common values. Like, INNER JOIN shows only the matching values, and OUTER JOIN shows all the values. I don't remember all the types exactly, but usually I just use JOIN with ON condition and it works.",
        "feedback": "Your answer demonstrates only a surface-level understanding of JOINs. You didn’t explain the different types (INNER, LEFT, RIGHT, FULL) properly or give a concrete use case. This could hurt performance or correctness in real-world SQL tasks. Study the different JOINs and their behavior more thoroughly."
      },
      {
        "question": "What’s the difference between WHERE and HAVING clauses in SQL?",
        "answer": "Both are used to filter data. I think WHERE filters rows and HAVING filters columns. But I usually just use WHERE because HAVING seems less useful unless there’s a special case.",
        "feedback": "Unfortunately, this is incorrect. HAVING filters groups after aggregation, while WHERE filters rows before aggregation. Misunderstanding this can lead to incorrect query logic. You need to revise SQL aggregation workflows and the role of HAVING in grouped queries."
      },
      {
        "question": "What are outliers, and how do you deal with them in your data?",
        "answer": "",
        "feedback": "This answer lacks depth. While it touches on the existence of outliers, it misses methods of detection (e.g., Z-score, IQR), domain analysis, and model implications. SQL isn’t the primary tool for outlier handling, so this question feels out of place here—but your generic response shows a lack of structured thinking."
      }
    ],
    "Visualization Tools": [
      {
        "question": "How do you choose the right chart for your data?",
        "answer": "I consider the type of data and the message I want to convey. For trends over time, I use line charts. For comparisons, I use bar charts. If I'm showing part-to-whole relationships, pie or donut charts work. For distributions, histograms or box plots are helpful. I try to avoid misleading visualizations by keeping the design clean.",
        "feedback": "Excellent answer. You showed good judgment in choosing charts based on data type and purpose. Clear reasoning and practical insight were demonstrated."
      },
      {
        "question": "How would you make your dashboard user-friendly?",
        "answer": "I focus on clarity, consistency, and interactivity. I keep the layout intuitive and avoid clutter. I use filters or slicers to allow user-driven exploration, include KPIs or summary tiles at the top, and ensure visual hierarchy with appropriate font sizes and colors. I also test the dashboard with users and iterate based on feedback.",
        "feedback": "Great response. You’ve hit the key usability principles. User testing and iteration are particularly valuable and often missed—well done."
      },
      {
        "question": "What are slicers in Power BI or filters in Tableau used for?",
        "answer": "Slicers in Power BI and filters in Tableau are used to narrow down the data being viewed. They allow users to interact with the dashboard and dynamically change what is displayed. This helps make dashboards more flexible and user-driven.",
        "feedback": "Good explanation. Straight to the point and accurately describes how filters and slicers function. You might have added an example of a use case, like filtering by region or time period."
      }
    ],
    "Python for Data Science": [
        {
          "question": "What’s the difference between Pandas and NumPy?",
          "answer": "They are both Python libraries. I think Pandas is newer and more powerful than NumPy. I usually just use Pandas because it can do everything. I don't use NumPy that much.",
          "feedback": "This answer shows a limited understanding. Pandas is built on top of NumPy, and both have different purposes—NumPy for efficient numerical operations and arrays, and Pandas for tabular data. You missed this key relationship and use case distinction."
        },
        {
          "question": "How do you handle large datasets in Python?",
          "answer": "I just read them with Pandas and try not to load everything at once. Sometimes I use Excel or split the CSV file into smaller parts. I haven’t really worked with very large datasets, so I’m not sure.",
          "feedback": "Your answer lacks the techniques expected at an intermediate level. Consider learning about Dask, chunking, using efficient file formats like Parquet, or leveraging databases and generators for memory-efficient processing."
        },
        {
          "question": "What are your go-to libraries for a full data science project in Python?",
          "answer": "I mainly use Pandas and Matplotlib. Sometimes Scikit-learn if I need to train something. But mostly I just explore the data manually and use Excel too if needed.",
          "feedback": "You missed the broader stack expected for end-to-end data science workflows. Libraries like NumPy, Pandas, Scikit-learn, Matplotlib/Seaborn, XGBoost, TensorFlow/PyTorch, and tools like MLflow or FastAPI for deployment are expected. The reliance on Excel hints at gaps in production-level readiness."
        }
    ],
  }
}

feedback_map = {
  'Typescript': 'The candidate shows a solid understanding of TypeScript fundamentals and demonstrates practical knowledge of generics. However, some answers could be enhanced by incorporating use cases and architectural benefits. You passed the interview',
  'Next.js': 'Responses are technically accurate and well-structured, covering SSR, SSG, and API routes. There is s a good grasp of data-fetching strategies, though some advanced concepts like ISR or SEO trade-offs were not covered. With minor improvements, you will be prepared for this topic.',
  'Embeddings': 'The answers are too vague or lack technical rigor. There is limited discussion of how embeddings function or are used at scale, and no real explanation of similarity metrics',
  'Retrieval-Augmented Generation (RAG)': ' Answers show only a surface-level understanding of RAG systems. Key concepts like chunking, vector search, and evaluation methods are missing or lightly touched.  Study end-to-end RAG pipelines — how data is chunked, embedded, retrieved, and passed to an LLM. Understand how RAG reduces hallucination and how to evaluate its performance. You did not pass this section and need to improve your knowledge significantly.',
  'API Design': 'The candidate demonstrates good knowledge of REST principles and API versioning. Comparisons with GraphQL are reasonable, though they could be stronger with deeper insights into tooling and complexity management. Very good job overall, you passed!.',
  'Serverless Architectures': 'Answers are oversimplified and often miss core trade-offs like cold starts, execution limits, and practical deployment strategies. There’s little evidence of hands-on experience with platforms like AWS Lambda or GCP. You did not pass this section and need to improve your serverless architecture skills significantly before your interview.',
  '1': 'The candidate demonstrates strong technical competency in TypeScript, Next.js, and RESTful API design, showcasing a clear understanding of type safety, component-based architecture, and modern web development best practices. However, their performance in other key areas such as embeddings, Retrieval-Augmented Generation (RAG), and serverless architectures revealed significant gaps in both conceptual depth and practical application. Their responses often lacked specificity, real-world context, or awareness of scaling and deployment considerations, suggesting limited experience beyond surface-level familiarity. Given the importance of these skills for the role, the interview does not meet the expectations for success.',
  'Data Preprocessing': 'Your answers demonstrated a solid understanding of key preprocessing techniques and trade-offs. You showed good balance between theory and practical applications. A few more advanced considerations could enhance your responses, but overall you showed you’re job-ready for this area. You will likely pass your interview',
  'Feature Engineering': 'Strong performance with practical and relevant examples. You showed a clear ability to engineer useful features and evaluate them effectively. Minor areas for enhancement include referencing dimensionality reduction techniques and deeper validation strategies. Overall, you are well-prepared for this topic.',
  'Model Evaluation': 'You demonstrated a deep understanding of evaluation metrics, model tuning, and selection strategies. Your examples were clear and relevant. A few advanced touches like ensemble modeling or uncertainty estimation would further enhance your answers. You are well-prepared for this topic.',
  'SQL Databases': 'Your understanding of SQL concepts is weak and lacked precision. Basic operations like JOINs and filtering with HAVING were poorly explained. There was also a mix-up in your terminology. You should revisit SQL fundamentals with practice on real queries. Your answers were not satisfactory and you need to improve your SQL skills significantly before your interview.',
  'Visualization Tools': 'You showed a solid understanding of effective data visualization principles and interactivity tools in Power BI/Tableau. Your answers were clear and practical, with an excellent focus on user experience. You are well-prepared for this topic.',
  'Python for Data Science': 'Your responses revealed major gaps in practical Python data science knowledge. You rely too heavily on Pandas and Excel, and are unfamiliar with large-scale or production-grade tools and workflows. This is a serious concern for data science roles. You did not pass this section and need to improve your Python skills significantly before your interview.',
  '2': 'Based on the interview performance, you demonstrated strong capabilities in data preprocessing, feature engineering, model evaluation, and data visualization—showing clear understanding of core concepts, practical application, and the ability to communicate effectively. Your answers reflected real-world experience and job readiness in those areas. However, your performance in SQL Databases and Python for Data Science was notably below expectations. Key foundational topics in SQL were misunderstood or explained inaccurately, and your responses in Python revealed a lack of familiarity with scalable, production-level data science workflows. While you clearly have potential and strength in analytical thinking and modeling, these technical gaps are significant enough to result in an overall non-passing outcome for this interview. With targeted improvement in SQL and Python proficiency, you have a strong chance of succeeding in your next attempt.'
}