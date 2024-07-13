# Amazon Bedrock Examples

Practical examples and use cases for the Amazon Bedrock service.

## Getting Started

1. **Clone the repository:**
    ```
    git clone https://github.com/mrnexeon/amazon-bedrock-examples.git
    ```
2. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

3. **Install and configure AWS CLI:**
    - Follow the [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) to install the AWS CLI.
    - Configure the AWS CLI with your credentials:
        ```
        aws configure
        ```
    - For more details, refer to the [AWS CLI Configuration Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html).

4. Follow the steps at [Request access to a Amazon Bedrock foundation model](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html#getting-started-model-access) to request access to the following models:
    - Amazon Titan Text G1 - Lite
    - Amazon Titan Text G1 - Express
    - Mistral AI Mistral Large
    - Mistral AI Mistral Small

5. **Run the examples:**
   - Example of listing available models:
        ```
        python 01_list_models.py
        ```
   - Example of using text prompts:
        ```
        python 02_text_prompts.py
        ```
   - Example of a conversation application:
        ```
        python 03_converse.py
        ```
   - Example of context retention in conversations:
        ```
        python 04_context_retention.py
        ```
   - Example of streaming responses:
        ```
        python 05_streaming.py
        ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.