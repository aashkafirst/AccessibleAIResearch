from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_required_content(url):
    # Make an HTTP request to the website
    response = requests.get(url)

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the <div> element with class "post-detail"
    post_detail_div = soup.find('div', class_='post-detail')

    # Find all <p>, <ul>, and <ol> elements within the post-detail <div>
    return post_detail_div.find_all(['p', 'ul', 'ol', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    
def write_tech_terms_to_file(og_text, file_name, title):
    with open(file_name, 'w') as file:
        file.write(title + "\n")
        for og_text_element in og_text:
            if og_text_element.name == 'h3' or og_text_element.name == 'h4':
                file.write("\n\n" + str(og_text_element) + "\n")
                continue
            else:
                file.write(str(og_text_element) + "\n")     

def detect_language(action):
    if 'French' in action:
        return 'French'
    elif 'Hindi' in action:
        return 'Hindi'
    else:
        return 'English'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/simplifyPost1', methods=['POST'])
def simplify_post_1():
    url = "https://www.anthropic.com/index/core-views-on-ai-safety"
    action = request.form['action']
    og_text = scrape_required_content(url)
    write_tech_terms_to_file(og_text, 'templates/post1TechnicalTerms.html', '<h1> Core Views on AI Safety: When, Why, What, and How </h1><h2>In Technical Terms</h2>')
    return render_template('accessible.html', language=detect_language(action), post='Post1')

@app.route('/simplifyPost2', methods=['POST'])
def simplify_post_2():
    url = "https://www.anthropic.com/index/charting-a-path-to-ai-accountability"
    action = request.form['action']
    og_text = scrape_required_content(url)
    write_tech_terms_to_file(og_text, 'templates/post2TechnicalTerms.html', '<h1> Charting a Path to AI Accountability </h1><h2>In Technical Terms</h2>')
    return render_template('accessible.html', language=detect_language(action), post='Post2')


@app.route('/simplifyPost3', methods=['POST'])
def simplify_post_3():
    url = "https://www.anthropic.com/index/constitutional-ai-harmlessness-from-ai-feedback"
    action = request.form['action']
    og_text = scrape_required_content(url)
    write_tech_terms_to_file(og_text, 'templates/post3TechnicalTerms.html', '<h1> Constitutional AI: Harmlessness from AI Feedback </h1><h2>In Technical Terms</h2>')
    return render_template('accessible.html', language=detect_language(action), post='Post3')

@app.route('/simplifyPost4', methods=['POST'])
def simplify_post_4():
    url = "https://www.anthropic.com/index/scaling-laws-and-interpretability-of-learning-from-repeated-data"
    action = request.form['action']
    og_text = scrape_required_content(url)
    write_tech_terms_to_file(og_text, 'templates/post4TechnicalTerms.html', '<h1> Scaling Laws and Interpretability of Learning from Repeated Data </h1><h2>In Technical Terms</h2>')
    return render_template('accessible.html', language=detect_language(action), post='Post4')


if __name__ == '__main__':
    app.run(debug=True)
