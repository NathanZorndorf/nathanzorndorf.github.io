# imports
from flask import Blueprint, Flask, g, jsonify, render_template, request, Response, redirect, url_for, send_from_directory
import os

# custom modules
import helper

# Configure application
app = Flask(__name__)


@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():

    title_text = helper.get_title_content('index')

    return render_template('index.html',
                                title_text=title_text,
                                latest_project_name='cool project i did about dogs!',
                                latest_blog_post_name='cool blog post I made about poop!',
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))