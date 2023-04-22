import prompt
import gpt_api

# Example usage
max_tokens = 500
# print(string_list)

def tags(topic):
    result = gpt_api.gpt(f'Give 6 relevant tags in comma separated format on {topic}:', max_tokens)
    return result


def writeSequenceArticle(topic):
    htmlString = f'<h1>{topic}</h1>'

    promp1 = prompt.giveMeSixHeadingOnThisTopic(topic)

    result = gpt_api.gpt(promp1, max_tokens)
    print(result)
    topic_heading = result.split(',')
    print(topic_heading)

    print(len(topic_heading))

    for heading in topic_heading:
        heading_prompt = prompt.subTopicHtmlPrompt(heading)
        heading_response = gpt_api.gpt(heading_prompt, 1250)
        htmlString += heading_response
        print(f"{heading_response}")
    
    return htmlString