#!/home/nik/.local/share/virtualenvs/website-sVgNdJ-5/bin/python
import os
import http.cookies
import json

with open("./cgi-bin/counter.json", "r") as counter:
    data = json.load(counter)

global_counter = int(data["global.counter"])

with open("./cgi-bin/counter.json", "w") as counter:
    json.dump({"global.counter": global_counter+1}, counter)

query = os.getenv("QUERY_STRING")

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))

cookie_counter = cookie.get("LOCAL_COUNTER")
if cookie_counter is None:
    local_counter = 0
else:
    local_counter = int(cookie_counter.value)

print(f"Set-cookie: LOCAL_COUNTER={local_counter + 1}")

print("Content-Type: text/html")
print()

print("<title>Test</title>")


score = 0
right_answers = ["1.2", "2.1", "3.1"]
passed_questions = []
given_answers = []

if isinstance(query, str):
    answers = query.split("&")
    for ans in answers:
        given_answers.append(ans.split('=')[1])
        if ans.split('=')[1] in right_answers:
            score += 1
            passed_questions.append(ans[-3])

print("""<!DOCTYPE html> 
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/style.css">
</head>""")
print(f"""
<body>
    <div class="container">
        <form action="/cgi-bin/script.py" method="get">
            <ol><div class="{'right' if '1' in passed_questions else 'wrong'}">
                <li>QUESTION 1</li>
                <input type="radio" value="1.1" name="answer1" {'checked' if '1.1' in given_answers else ''} id="a11">
                    <label for="a11">ANSWER1.1</label><br>
                <input type="radio" value="1.2" name="answer1" {'checked' if '1.2' in given_answers else ''} id="a12">
                    <label for="a12">ANSWER1.2</label><br>
                <input type="radio" value="1.3" name="answer1" {'checked' if '1.3' in given_answers else ''} id="a13">
                    <label for="a13">ANSWER1.3</label><br>
                </div>
                <div class="{'right' if '2' in passed_questions else 'wrong'}">
                <li>QUESTION 2</li>
                <input type="radio" value="2.1" name="answer2" {'checked' if '2.1' in given_answers else ''} id="a21">
                    <label for="a21">ANSWER1.1</label><br>
                <input type="radio" value="2.2" name="answer2" {'checked' if '2.2' in given_answers else ''} id="a22">
                    <label for="a22">ANSWER2.2</label><br>
                <input type="radio" value="2.3" name="answer2" {'checked' if '2.3' in given_answers else ''} id="a23">
                    <label for="a23">ANSWER2.3</label><br>
                </div>
                <div class="{'right' if '3' in passed_questions else 'wrong'}">
                <li>QUESTION 3</li>
                <input type="radio" value="3.1" name="answer3" {'checked' if '3.1' in given_answers else ''} id="a31">
                    <label for="a31">ANSWER3.1</label><br>
                <input type="radio" value="3.2" name="answer3" {'checked' if '3.2' in given_answers else ''} id="a32">
                    <label for="a32">ANSWER3.2</label><br>
                <input type="radio" value="3.3" name="answer3" {'checked' if '3.3' in given_answers else ''} id="a33">
                    <label for="a33">ANSWER3.3</label><br>
                </div>
            </ol>
            <input type="submit" value="Ответить"> <input type="reset">
        </form>
        </div>
        <div class="container" style="margin-left: 20px; align-items: baseline; margin-right: 20px">
        <h1>you have {score} right answers
        <h1>you answered right to {', '.join(passed_questions)} questions
        <h1>you passed this test {local_counter+1} times!
        <h1>total quantity of people who passed: {global_counter}
        </div>
</body>
</html>
""")