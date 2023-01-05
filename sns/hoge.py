{% load static %}
<!doctype html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" 
    href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" 
    crossorigin="anonymous">
</head>
<body class="container">
    <nav class="navbar navbar-expand navbar-light bg-light">
    <ul class="navbar-nav mr-auto">
        <li class="nav-item">
            <a class="nav-link" href="{% url 'index' %}">top</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="{% url 'post' %}">post</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="{% url 'groups' %}">group</a>
        </li>
    </ul>
    <span>logined: <span class="h6">"{{login_user}}".</span></span>
    </nav>

    <div>{% block header %}
        {% endblock %}</div>
    <div class="content">{% block content %}
        {% endblock %}</div>

    <hr>
    <div class="my-3">
        <span class="font-weight-bold">
            <a href="/admin/logout?next=/sns/">
                [ logout ]</a></span>
        <span class="float-right">copyright 2020 
            SYODA-Tuyano.</span>
    </div>
</body>
</html>