1. Zero-shot Prompting

Definition: Asking the model to perform a task without giving any examples.
Use Case: When you want fast answers without training or in low-resource settings.

2. Few-shot Prompting

Definition: Providing a few examples within the prompt to guide the model.
Use Case: Improves accuracy when you can't fine-tune, but need context.

3. Chain-of-Thought Prompting

Definition: Encouraging the model to reason step-by-step by prompting with intermediate reasoning.
Use Case: Effective for solving complex logical or arithmetic problems.

4. Meta Prompting

Definition: Using prompts to guide how to generate other prompts.
Use Case: Useful in creating generalizable or automated prompt creation 
frameworks.

5. Self-Consistency

Definition: Sampling multiple reasoning paths and choosing the most frequent answer.
Use Case: Increases accuracy for reasoning tasks with variable outputs.

6. Generate Knowledge Prompting

Definition: Prompting the model to generate or retrieve relevant knowledge before answering.
Use Case: When context or domain knowledge is important.

7. Prompt Chaining

Definition: Using the output of one prompt as input to the next, forming a chain of reasoning or tasks.
Use Case: Useful in multi-step workflows (e.g., research, summarization).

8. Tree of Thoughts (ToT)

Definition: Exploring multiple reasoning paths as a tree and selecting the optimal path.
Use Case: Improves performance in creative or planning tasks.

9. Retrieval-Augmented Generation (RAG)

Definition: Fetching external documents (e.g., using a vector DB) to enhance model response.
Use Case: When accurate, up-to-date, or factual information is required.

10. Automatic Reasoning and Tool-use

Definition: The model decides when to use tools (e.g., calculators, code interpreters) for reasoning.
Use Case: Solves tasks requiring external capabilities (math, search, APIs).

11. Automatic Prompt Engineer

Definition: Automatically generates or optimizes prompts to maximize performance.
Use Case: When manually writing effective prompts is hard.

12. Active-Prompt

Definition: Dynamically updates prompts based on intermediate outputs or feedback.
Use Case: Good for interactive systems or agents adapting to user behavior.

13. Directional Stimulus Prompting

Definition: Nudging the model’s behavior in a desired direction using tailored stimuli.
Use Case: Helps control tone, style, or decision bias in outputs.

14. Program-Aided Language Models (PAL)

Definition: Delegating reasoning to external code (e.g., Python) and combining results with language model output.
Use Case: For tasks where symbolic reasoning is needed (e.g., calculations, algorithms).

15. ReAct (Reasoning + Acting)

Definition: Combines reasoning and actions (e.g., API calls, environment interaction) with natural language.
Use Case: Powerful for agents that need both internal reasoning and real-world actions.

16. Reflexion

Definition: The model reflects on past outputs, identifies mistakes, and self-corrects in future steps.
Use Case: Effective for debugging or learning-oriented agents.

17. Multimodal Chain-of-Thought (Multimodal CoT)

Definition: Combining chain-of-thought reasoning across multiple modalities (e.g., text + image).
Use Case: Image reasoning tasks with text outputs, like captioning or VQA.

18. Graph Prompting

Definition: Structuring prompts using graphs (e.g., nodes = tasks, edges = logic flow) to handle complex task planning.
Use Case: Effective in structured decision-making or reasoning with interdependencies.