question_map = {
    "Frontend Engineering": {
        "Typescript": [
            {
                "question": "How does TypeScript improve code maintainability in large-scale applications?",
                "answer": "",
                "feedback": "good"
            },
            {
                "question": "What are the differences between interface and type in TypeScript?",
                "answer": "",
                "feedback": "good"
            },
            {
                "question": "Explain generics in TypeScript and give a practical use case.",
                "answer": "",
                "feedback": "pending"
            }
        ],
        "Next.js": [
            {
                "question": "How does Next.js handle server-side rendering (SSR) vs. static site generation (SSG)?",
                "answer": "",
                "feedback": "pending"
            },
            {
                "question": "What’s the benefit of using getServerSideProps versus getStaticProps?",
                "answer": "",
                "feedback": "pending"
            },
            {
                "question": "How do you implement API routes in Next.js?",
                "answer": "",
                "feedback": "pending"
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
                "feedback": "pending"
            },
            {
                "question": "What are the principles of RESTful API",
                "answer": "",
                "feedback": "pending"
            },
            {
                "question": "What are the most common approaches to versioning REST API?",
                "answer": "",
                "feedback": "pending"
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
        "answer": "I just delete all rows with missing values because they will ruin the model accuracy.",
        "feedback": "This approach is too aggressive and can result in significant data loss. A better answer would consider imputation techniques or understanding the pattern of missingness before deciding how to handle them."
      },
      {
        "question": "How do you handle categorical variables in a dataset before modeling?",
        "answer": "I use one-hot encoding for categorical variables because it turns them into binary features that many models can handle better. If there are too many categories, I also consider using frequency encoding or embeddings depending on the model and data size.",
        "feedback": "Great response. You’ve correctly noted that encoding depends on model type and data size, and you demonstrated awareness of alternative strategies for high-cardinality variables."
      },
      {
        "question": "What are outliers, and how do you deal with them in your data?",
        "answer": "Outliers are data points that are very different from the rest. I usually remove them from the dataset.",
        "feedback": "The answer identifies what outliers are, but simply removing them isn’t always the best practice. You should also consider methods for detecting outliers (e.g., IQR, Z-score), and whether they are errors or legitimate extreme cases before removing or transforming them."
      }
    ],

    "Feature Engineering": [
      {
        "question": "What is feature engineering, and why is it important?",
        "answer": "Feature engineering is the process of transforming raw data into features that better represent the underlying problem to the predictive models. It’s important because well-designed features can improve model accuracy and make training more efficient.",
        "feedback": "Excellent answer. It shows an understanding of both the process and why it matters in terms of model performance."
      },
      {
        "question": "Can you give an example of a feature you engineered in a project?",
        "answer": "I once added a feature by summing two columns because it looked useful.",
        "feedback": "This answer lacks depth and context. Try to provide a specific example with reasoning behind the feature and how it helped the model. For example, was it time-based? Did it capture a meaningful pattern?"
      },
      {
        "question": "How do you decide which features to keep and which to discard?",
        "answer": "I use feature importance scores from tree models like Random Forests or XGBoost, and also check for multicollinearity using correlation matrices or VIF. If two features are redundant, I may drop one."
        ,"feedback": "Good response! You've demonstrated a solid understanding of feature selection using both model-based and statistical techniques."
      }
    ],

    "Model Evaluation": [
      {
        "question": "What’s the difference between precision and recall?",
        "answer": "Precision is when the model is correct, and recall is when the model gets everything.",
        "feedback": "This answer is too vague. A more accurate explanation is: Precision is the proportion of true positives among all predicted positives, and recall is the proportion of true positives among all actual positives. Add examples for clarity."
      },
      {
        "question": "How do you avoid overfitting in a machine learning model?",
        "answer": "I usually split the dataset into training and testing. If the model performs well on both, it’s good.",
        "feedback": "Partial understanding. While dataset splitting is essential, preventing overfitting also involves techniques like regularization, pruning, early stopping, and simplifying the model. Include these methods for a more complete answer."
      },
      {
        "question": "How do you select the best model for a particular task?",
        "answer": "I train multiple models and compare them using cross-validation and relevant metrics like accuracy, F1-score, or RMSE depending on the task. I also consider computational efficiency and interpretability when selecting the final model.",
        "feedback": "Strong answer. You’ve covered both evaluation metrics and practical deployment considerations."
      }
    ]
  },

  "Data Tools & Technologies": {
    "SQL Databases": [
      {
        "question": "How do you perform a JOIN operation in SQL, and when would you use it?",
        "answer": "I use JOIN to combine tables, like INNER JOIN to get common records or LEFT JOIN when I want all rows from the first table and matching ones from the second. It's useful in normalized databases to collect related data.",
        "feedback": "Well done! Shows clear understanding of different types of JOINs and their applications."
      },
      {
        "question": "What’s the difference between WHERE and HAVING clauses in SQL?",
        "answer": "WHERE is used for filtering rows before aggregation, and HAVING is used after aggregation.",
        "feedback": "Good and concise explanation. Could be improved with a quick example to show their usage in a GROUP BY query."
      },
      {
        "question": "How would you retrieve the second highest salary from a table of employee salaries?",
        "answer": "You can sort the salaries and pick the second one.",
        "feedback": "This lacks specificity. A better answer would be: Use a subquery like SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees);"
      }
    ],

    "Visualization Tools": [
      {
        "question": "How do you choose the right chart for your data?",
        "answer": "It depends on what I want to show. I use bar charts to compare categories, line charts for trends, and histograms to show distributions.",
        "feedback": "Good understanding of common visualizations. Could be improved by mentioning pie charts, heatmaps, or dashboards for specific use cases."
      },
      {
        "question": "How would you make your dashboard user-friendly?",
        "answer": "I make sure it looks nice and has some charts.",
        "feedback": "Too vague. Consider mentioning best practices like layout consistency, use of filters/slicers, highlighting KPIs, interactivity, and user testing."
      },
      {
        "question": "What are slicers in Power BI or filters in Tableau used for?",
        "answer": "Slicers help users choose what data to view, like selecting by date or region. They make dashboards more interactive.",
        "feedback": "Great answer. Shows practical understanding of enhancing dashboard usability through user-driven filtering."
      }
    ],

    "Python for Data Science": [
      {
        "question": "What’s the difference between Pandas and NumPy?",
        "answer": "NumPy handles numerical data and arrays, while Pandas is built on top of NumPy and offers labeled data structures like Series and DataFrames. Pandas is more suitable for data wrangling and analysis of tabular data.",
        "feedback": "Excellent explanation. You correctly pointed out the relationship and use cases for both."
      },
      {
        "question": "How do you handle large datasets in Python?",
        "answer": "I load them into Pandas and work with them as usual.",
        "feedback": "Insufficient approach. Large datasets require memory-efficient handling—consider using chunking, Dask, or data type optimization."
      },
      {
        "question": "What are your go-to libraries for a full data science project in Python?",
        "answer": "",
        "feedback": "Solid stack. Shows familiarity with tools across the full data science pipeline."
      }
    ]
  }
}
