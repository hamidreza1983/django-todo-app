{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ user.name }}
{% endblock %}

{% block html %}
http://127.0.0.1:8000/accounts/api/V1/is-verified/{{token}}
{% endblock %}