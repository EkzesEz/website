#!/home/nik/.local/share/virtualenvs/website-sVgNdJ-5/bin/python
import os

print("Content-Type: text/html")
print()

print("<title>Test</title>")

query = os.getenv("QUERY_STRING")

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
else:
    print("query is not string!!!")
    exit(0)
print(f"""
<!DOCTYPE html> 
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test</title>
</head>
<body>
    <form action="/cgi-bin/script.py" method="get">
        <ol><div style="width: 25%; background: {'green' if '1' in passed_questions else 'red'}">
            <li>QUESTION 1</li>
            <input type="radio" value="1.1" name="answer1" {'checked' if '1.1' in given_answers else ''}> ANSWER1.1<br>
            <input type="radio" value="1.2" name="answer1" {'checked' if '1.2' in given_answers else ''}> ANSWER1.2<br>
            <input type="radio" value="1.3" name="answer1" {'checked' if '1.3' in given_answers else ''}> ANSWER1.3<br>
            </div>
            <div style="width: 25%; background: {'green' if '2' in passed_questions else 'red'}">
            <li>QUESTION 2</li>
            <input type="radio" value="2.1" name="answer2" {'checked' if '2.1' in given_answers else ''}> ANSWER2.1<br>
            <input type="radio" value="2.2" name="answer2" {'checked' if '2.2' in given_answers else ''}> ANSWER2.2<br>
            <input type="radio" value="2.3" name="answer2" {'checked' if '2.3' in given_answers else ''}> ANSWER2.3<br>
            </div>
            <div style="width: 25%; background: {'green' if '3' in passed_questions else 'red'}">
            <li>QUESTION 3</li>
            <input type="radio" value="3.1" name="answer3" {'checked' if '3.1' in given_answers else ''}> ANSWER3.1<br>
            <input type="radio" value="3.2" name="answer3" {'checked' if '3.2' in given_answers else ''}> ANSWER3.2<br>
            <input type="radio" value="3.3" name="answer3" {'checked' if '3.3' in given_answers else ''}> ANSWER3.3<br>
            </div>
        </ol>
        <input type="submit"> <input type="reset">
    </form>
</body>
</html>
""")

print(f"""
you have {score} right answers<br>
you answered right to {', '.join(passed_questions)} questions<br>
you so fucking stupid<br>
""")