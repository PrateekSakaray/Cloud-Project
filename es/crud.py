
from es import get_model
from flask import Blueprint, redirect, render_template, request, url_for


crud = Blueprint('crud', __name__)


# [START list on home page]
@crud.route("/")
def list():
    token = request.args.get('page_token', None)
    if token:
        token = token.encode('utf-8')
    list1, list2, list3 = get_model().list(cursor=token, page='default')
    return render_template(
        "home.html",
        airport=list1,
        airline=list2,
        lounge=list3
    )
# [END list]

# List on airport page
@crud.route("/airport", methods=['POST','GET'])
def airport():
    if request.method == 'POST':
        cursor=0
        dropdown = request.form.get("airport", None)
        list_item = get_model().list(cursor=cursor, page="airport_dropdown", dropdown=dropdown)
        return render_template(
            "airport.html",
            airport=list_item,
            value=dropdown
        )

    if request.method == 'GET':
        token = request.args.get('page_token', None)
        if token:
            token = token.encode('utf-8')
        list_item = get_model().list(cursor=token, page="airport")
        return render_template(
            "airport.html",
            airport=list_item,
            value="Overall_rating"
        )

# List on airline page
@crud.route("/airline", methods=['POST','GET'])
def airline():
    if request.method == 'POST':
        cursor=0
        dropdown = request.form.get("airline", None)
        list_item = get_model().list(cursor=cursor, page="airline_dropdown", dropdown=dropdown)
        return render_template(
            "airline.html",
            airline=list_item,
            value=dropdown
        )
    if request.method == 'GET':
        token = request.args.get('page_token', None)
        if token:
            token = token.encode('utf-8')
        list_item = get_model().list(cursor=token, page="airline")
        return render_template(
            "airline.html",
            airline=list_item,
            value="Overall_rating"
        )

# List on lounge page
@crud.route("/lounge", methods=['POST','GET'])
def lounge():
    if request.method == 'POST':
        cursor=0
        dropdown=request.form.get("lounge",None)
        list_item = get_model().list(cursor=cursor, page="lounge_dropdown", dropdown=dropdown)
        return render_template(
            "lounge.html",
            lounge=list_item,
            value=dropdown
        )
    if request.method == 'GET':
        token = request.args.get('page_token', None)
        if token:
            token = token.encode('utf-8')
        list_item = get_model().list(cursor=token, page="lounge")
        return render_template(
            "lounge.html",
            lounge=list_item,
            value="Overall_rating"
        )