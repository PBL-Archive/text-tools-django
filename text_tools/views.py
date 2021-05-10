from django.shortcuts import render
from text_tools import services as s
# Create your views here.

def home(request):
    input_text = ""
    select_text_tool = "False"
    output_text = "Please type in some text above to begin!"
    try:
        input_text = request.POST.get('input_text') if request.POST.get('input_text') != "" or None else ""
        select_text_tool = request.POST.get('select_text_tool') if request.POST.get('select_text_tool') != "" or None else "False"
        output_text = "Please type in some text above to begin!"
    except:
        input_text = "",
        select_text_tool = "False"
        output_text = "Please type in some text above to begin!"
    if select_text_tool == "remove_white_spaces":
        output_text = s.remove_white_spaces(input_text)
    elif select_text_tool == "remove_special_characters":
        output_text = s.remove_special_characters(input_text)
    elif select_text_tool == "remove_html_tags":
        output_text = s.remove_html_tags(input_text)
    elif select_text_tool == "remove_multiple_newlines":
        output_text = s.remove_multiple_newlines(input_text)
    elif select_text_tool == "identify_emails":
        output_text = s.identify_emails(input_text)
    elif select_text_tool == "identify_urls":
        output_text = s.identify_urls(input_text)
    elif select_text_tool == "convert_to_camelcase":
        output_text = s.convert_to_camelcase(input_text)
    elif select_text_tool == "convert_to_pascalcase":
        output_text = s.convert_to_pascalcase(input_text)
    elif select_text_tool == "convert_to_snakecase":
        output_text = s.convert_to_snakecase(input_text)
    elif select_text_tool == "uppercase_full_text":
        output_text = s.uppercase_full_text(input_text)
    elif select_text_tool == "lowercase_full_text":
        output_text = s.lowercase_full_text(input_text)
    else:
        output_text = "Please type in some text above to begin!"
    data = {
        "input_text_return": input_text,
        "select_text_tool_return": select_text_tool,
        "output_text": output_text
    }
    return render(request, 'index.html', data)