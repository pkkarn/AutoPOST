def giveMeTopics(text):
    return f"""
    Give me topics around {text}
    """

def giveMeSixHeadingOnThisTopic(topic):
    return f"""
    Give me six subheading for article on \"Topic\" in given format:\n
    heading1, heading2, heading3,heading4, heading5, heading6\n

    Give me six subheading for article on \"Topic\" in given format:\n
    heading1, heading2, heading3,heading4, heading5, heading6\n

    Give me six subheading for article on \"{topic}\" in given format:\n
    """

def subTopicHtmlPrompt(subheading):
    return f"""
    Write 200 words of article in HTML Format on \"Topic\":\n
    <h3>Topic</h3><div>[Content Explainign in HTML format]</div>

    Write 200 words of article in HTML Format on \"{subheading}\":\n
    """