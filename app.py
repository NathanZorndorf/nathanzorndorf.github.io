# imports
from flask import Blueprint, Flask, g, jsonify, render_template, request, Response, redirect, url_for, send_from_directory
import os

# custom modules
import helper

# Configure application
app = Flask(__name__)

@app.route('/test', methods=['POST', 'GET'])
def test():
    project = helper.get_portfolio_content()[1]
    return render_template('test.html', project=project)
    

@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():

    title_text = helper.get_title_content('index')

    project = helper.get_portfolio_content()[0] # get latest project

    post = helper.get_blog_posts()[0]

    return render_template('index.html',
                                title_text=title_text,
                                project=project,
                                post=post,
                                title="DATA SCIENCE & HEALTH",
                                id="index",
                                lang='en')


@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():

    # get all projects from the database
    projects = helper.get_portfolio_content()

    # get the title content for the portfolio page
    title_text = helper.get_title_content('portfolio')

    return render_template('portfolio.html',
                            title_text=title_text,
                            title="PROJECT PORTFOLIO",
                            id="portfolio",
                            projects=projects,
                            lang='en')

@app.route('/blog', methods=['POST', 'GET'])
def blog():

    # get all projects from the database
    # posts = helper.get_portfolio_content()
    posts = helper.get_blog_posts()

    # get the title content for the portfolio page
    title_text = helper.get_title_content('blog')

    return render_template('blog.html',
                            title_text=title_text,
                            title="STATISTICS & OTHER MUSINGS",
                            id="portfolio",
                            projects=posts,
                            lang='en')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))