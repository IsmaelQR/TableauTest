import jwt
import datetime
import uuid


from flask import Flask, render_template

app = Flask(__name__)


token = jwt.encode(
	{
		"iss": "187d3cf1-7230-4550-af40-aa041f0d40cf",
		"exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
		"jti": str(uuid.uuid4()),
		"aud": "tableau",
		"sub": "daniel.rivas@bebraven.org",
        #"sub": "peter.deweese@bebraven.org",
        #"sub": "jess.unrein@bebraven.org",
		#"sub": "aaron.buchanan@bebraven.org",
		"scp": ["tableau:views:embed", "tableau:metrics:embed"],
		"Region": "East"
	},
		"hnOFFl9e84SrA6N/8MWtOostRITqdLnPxLFlhgZnKzI=",
		algorithm = "HS256",
		headers = {
		'kid':"981a4b50-f4ff-42fd-8993-532773439a0f",
		'iss': "187d3cf1-7230-4550-af40-aa041f0d40cf"
        }
)
@app.route('/')
def index():
    # Variable que deseas enviar a HTML
    token_aux = token
    return render_template('Index.html', token_aux=token_aux)


if __name__ == '__main__':
    app.run()
print(token)

## Hi Bebraven team
# STEP1
## Generate a token with Python with jwt library.
# STEP2
## Update the token in each html.You need to generate a token each time it is entered and it has an expiration time.
# STEP3
# This could be open in a incognit page with out credentials
