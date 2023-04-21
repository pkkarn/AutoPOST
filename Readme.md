# AutoPOST

AutoPOST is a tool that uses the WordPress API and OpenAI API to automate blog post creation and publishing on your WordPress website. This powerful tool streamlines the process of generating content and posting it to your WordPress site with minimal effort.

## Features

- Automatically generate blog posts using the OpenAI API
- Publish posts directly to your WordPress website using the WordPress API
- Customizable post templates to suit your specific needs
- Easy installation and setup

## Installation

1. Clone this repository to your local machine:

`git clone https://github.com/yourusername/AutoPOST.git`

2. Change to the repository directory:

`cd AutoPOST`

3. Install the required dependencies:

`pip install -r requirements.txt`

4. Create a `.env` file in the root directory of the project with the following content:

```py
wp_user='your_wordpress_username'
wp_password='your_wordpress_password'
```


Replace `'your_wordpress_username'` and `'your_wordpress_password'` with your actual WordPress username and password.

5. Obtain an API key for the OpenAI API and add it to your `.env` file:

`openai_api_key='your_openai_api_key'`


Replace `'your_openai_api_key'` with your actual OpenAI API key.

## Usage

After completing the installation and setup process, you can run the main script to start generating and posting content to your WordPress website:

`python app.py`

You can customize the script to generate content based on your specific requirements and post templates.

## Support

If you encounter any issues or have questions about this tool, please feel free to open an issue on this GitHub repository.