from flask import Flask


app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    html= """
	
	<head>
	<link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.css" integrity="sha256-00w68NO3TLuHjKRHJmjrrgJBDtG/6OhbJEu1gtHcsuo=" crossorigin="anonymous" />
	<style> 
	body{display: table; position: absolute; height: 100%; width: 100%;}
    .middle{display: table-cell; vertical-align: middle;}
	</style>
	</head>
	
	<body>
	<div class="container middle">
	<h1 class="display-1 text-center animated pulse infinite">Coming Soon</h1>
	</div>
	</body>
	
	
	"""
    return html
	

if __name__ == '__main__':
    app.run()
